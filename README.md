
# Ethereum Blockchain Log Storage System

## 📋 Table of Contents
- [Quick Start](#-quick-start)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [File Structure](#-file-structure)
- [Smart Contract](#-smart-contract)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)

## 🚀 Quick Start

### 1. Activate Virtual Environment
```bash
source myenv/bin/activate

2. Deploy Smart Contract
bash

python3 smartContract.py

Copy the output contract address (e.g. 0x123...) and update in storage.py
3. Store Logs on Blockchain
bash
python3 storage.py

⚙️ Prerequisites

    Python 3.8+

    Node.js v14+

    npm

    Ganache CLI

💻 Installation
Python Dependencies
bash

pip install web3 py-solc-x

Ganache CLI
bash
npm install -g ganache

🛠️ Usage
Start Local Blockchain
bash
ganache --port=7545

Deploy Contract (in another terminal)
bash

source myenv/bin/activate
python3 smartContract.py

Store Logs
bash

python3 storage.py

Retrieve Logs
bash

python3 fetch_stored_logs.py

Verify Log Hashes
bash

python3 get_hashed_logs.py

📂 File Structure

.
├── smartContract.py       # Contract deployment
├── storage.py            # Log storage
├── fetch_logs.py         # Local log reader
├── fetch_stored_logs.py  # Blockchain log fetcher
├── get_hashed_logs.py    # Hash verification
├── LogStorage.sol        # Smart contract
└── README.md             # This file

📜 Smart Contract

LogStorage.sol provides:
solidity

// Store a log
function storeLog(string memory log) public

// Retrieve all logs
function getLogs() public view returns (string[] memory)

⚠️ Troubleshooting
Error	Solution
Connection refused	Ensure Ganache is running
Module not found	Reinstall dependencies
Permission denied	Use sudo for system logs
Empty results	Verify contract deployment
