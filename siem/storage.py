contract = w3.eth.contract(
    address=contract_address, abi=contract_interface["abi"]
)

# Read logs
with open("/var/log/syslog", "r") as f:
    logs = f.readlines()

# Store logs on Ethereum
for log in logs[:5]:  # Store only first 5 logs to save gas fees
    tx = contract.functions.storeLog(log[:200]).transact({"from": w3.eth.accounts[0]})
    w3.eth.wait_for_transaction_receipt(tx)
    print(f"Log stored: {log[:200]}")
