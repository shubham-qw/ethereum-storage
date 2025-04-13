from web3 import Web3
import sys
import time
import hashlib
import argparse
import json
import os

def print_error(message):
    print(f"\033[91m❌ ERROR: {message}\033[0m")

def print_success(message):
    print(f"\033[92m✅ {message}\033[0m")

def print_warning(message):
    print(f"\033[93m⚠️ {message}\033[0m")

def load_contract_address():
    """Load contract address from command line or config file"""
    parser = argparse.ArgumentParser(description='Store logs to Ethereum blockchain')
    parser.add_argument('--address', '-a', type=str, help='Direct contract address')
    parser.add_argument('--address-file', '-f', type=str, 
                      help='Path to JSON file containing contract address')
    args = parser.parse_args()

    # Command line address takes priority
    if args.address:
        if not Web3.is_address(args.address):
            print_error(f"Invalid contract address: {args.address}")
            sys.exit(1)
        return Web3.to_checksum_address(args.address)

    # Try loading from specified file
    if args.address_file:
        try:
            with open(args.address_file, 'r') as f:
                config = json.load(f)
                address = config.get('contract_address')
                
                if not address:
                    print_error("contract_address key not found in config file")
                    sys.exit(1)
                    
                if not Web3.is_address(address):
                    print_error(f"Invalid address in config: {address}")
                    sys.exit(1)
                    
                return Web3.to_checksum_address(address)
                
        except FileNotFoundError:
            print_error(f"Config file not found: {args.address_file}")
            sys.exit(1)
        except json.JSONDecodeError:
            print_error("Invalid JSON format in config file")
            sys.exit(1)

    # Fallback to default config
    if os.path.exists('config.json'):
        try:
            with open('config.json', 'r') as f:
                config = json.load(f)
                address = config.get('contract_address')
                if address and Web3.is_address(address):
                    return Web3.to_checksum_address(address)
        except Exception as e:
            print_warning(f"Error reading config.json: {str(e)}")

    print_error("No contract address provided. Use --address or --address-file")
    sys.exit(1)

def main():
    try:
        # Initialize Web3 connection
        w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
        
        if not w3.is_connected():
            print_error("Failed to connect to Ganache. Check if Ganache is running on port 7545.")
            sys.exit(1)

        # Load contract address
        contract_address = load_contract_address()
        print_success(f"Using contract address: {contract_address}")

        # Rest of main function remains the same
        contract_abi = [
            {
                "inputs": [{"internalType": "string", "name": "log", "type": "string"}],
                "name": "storeLog",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function",
            },
            {
                "inputs": [],
                "name": "getLogs",
                "outputs": [{"internalType": "string[]", "name": "", "type": "string[]"}],
                "stateMutability": "view",
                "type": "function",
            },
        ]

        contract = w3.eth.contract(
            address=contract_address,
            abi=contract_abi
        )

        # Read syslog with safety checks
        try:
            with open("/var/log/syslog", "r") as f:
                logs = [line[:500] for line in f.read().splitlines()]
                
            if not logs:
                print_warning("Syslog file is empty. No logs to store.")
                sys.exit(0)
                
        except PermissionError:
            print_error("Permission denied. Run with sudo to access system logs.")
            sys.exit(1)

        sender_address = w3.eth.accounts[0]
        total_logs = len(logs)
        success_count = 0
        failed_logs = []

        print(f"📤 Starting to store {total_logs} log entries (truncated to 500 chars)...")

        for idx, log in enumerate(logs, 1):
            if not log.strip():
                print_warning(f"Skipping empty log at line {idx}")
                continue

            try:
                gas_estimate = contract.functions.storeLog(log).estimate_gas({
                    "from": sender_address
                })
                
                tx_hash = contract.functions.storeLog(log).transact({
                    "from": sender_address,
                    "gas": gas_estimate + 20000
                })
                
                receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
                if receipt.status == 1:
                    success_count += 1
                    print_success(f"[{idx}/{total_logs}] Stored: {log[:50]}...")
                else:
                    raise ValueError("Transaction reverted")

            except Exception as e:
                try:
                    print_warning(f"Retrying with higher gas limit...")
                    tx_hash = contract.functions.storeLog(log).transact({
                        "from": sender_address,
                        "gas": 2_000_000
                    })
                    receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
                    if receipt.status == 1:
                        success_count += 1
                        print_success(f"[{idx}/{total_logs}] Stored on retry: {log[:50]}...")
                    else:
                        raise ValueError("Transaction reverted on retry")
                        
                except Exception as retry_error:
                    error_msg = f"Failed to store log line {idx}: {str(retry_error)}"
                    print_error(error_msg)
                    failed_logs.append({
                        "line": idx,
                        "log": log[:100],
                        "error": str(retry_error)
                    })
                    time.sleep(2)

        print("\n📝 Storage Summary:")
        print_success(f"Successfully stored: {success_count}/{total_logs}")
        if failed_logs:
            print_error(f"Failed to store: {len(failed_logs)} logs")
            print("💻 Failed entries (first 5):")
            for entry in failed_logs[:5]:
                print(f"  Line {entry['line']}: {entry['log']}...")
                print(f"    Error: {entry['error']}")

    except KeyboardInterrupt:
        print_error("\nOperation cancelled by user. Partial logs may have been stored.")
        sys.exit(1)

if __name__ == "__main__":
    main()
