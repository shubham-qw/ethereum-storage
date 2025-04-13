
# 🛡️ Ethereum Blockchain Log Storage System

A secure and transparent system for storing and retrieving log files using Ethereum smart contracts. This project uses Web3, Solidity, and Python to interact with a local blockchain (Ganache).

---

## 📋 Table of Contents

- [🚀 Quick Start](#-quick-start)
- [⚙️ Prerequisites](#-prerequisites)
- [💻 Installation](#-installation)
- [🛠️ Usage](#-usage)
- [📂 File Structure](#-file-structure)
- [🧠 Smart Contract](#-smart-contract)
- [🐞 Troubleshooting](#-troubleshooting)
- [📄 License](#-license)

---

## 🚀 Quick Start

### 1. Activate Virtual Environment

```bash
source myenv/bin/activate
```

### 2. Deploy the Smart Contract

```bash
python3 smartContract.py
```

> 📌 **Note:** Copy the deployed contract address (e.g., `0x123...`) from the output and update it inside `storage.py`.

### 3. Store Logs on the Blockchain

```bash
python3 storage.py
```

---

## ⚙️ Prerequisites

Ensure the following dependencies are installed:

- ✅ Python `3.8+`
- ✅ Node.js `v14+`
- ✅ `npm`
- ✅ Ganache CLI (for local blockchain testing)

---

## 💻 Installation

### Python Dependencies

```bash
pip install web3 py-solc-x
```

### Ganache CLI (Local Blockchain)

```bash
npm install -g ganache
```

---

## 🛠️ Usage

### Start the Local Blockchain

```bash
ganache --port=7545
```

> Open a new terminal for the next steps.

### Deploy the Smart Contract

```bash
source myenv/bin/activate
python3 smartContract.py
```

### Store Logs

```bash
python3 storage.py
```

### Retrieve Logs from Blockchain

```bash
python3 fetch_stored_logs.py
```

### Verify Log Hashes

```bash
python3 get_hashed_logs.py
```

---

## 📂 File Structure

```text
.
├── smartContract.py       # Smart contract deployment logic
├── storage.py             # Logs storage to blockchain
├── fetch_logs.py          # Read logs from local files
├── fetch_stored_logs.py   # Retrieve stored logs from blockchain
├── get_hashed_logs.py     # Generate & verify log hashes
├── LogStorage.sol         # Solidity smart contract
└── README.md              # This file
```

---

## 🧠 Smart Contract

**`LogStorage.sol`** provides two main functionalities:

```solidity
// Store a log entry on the blockchain
function storeLog(string memory log) public

// Retrieve all stored log entries
function getLogs() public view returns (string[] memory)
```

The smart contract ensures logs are tamper-proof and traceable on the Ethereum network.

---

## 🐞 Troubleshooting

| ❌ Error              | ✅ Solution                           |
|----------------------|----------------------------------------|
| `Connection refused` | Ensure Ganache CLI is running properly |
| `Module not found`   | Reinstall Python dependencies          |
| `Permission denied`  | Use `sudo` if accessing system logs    |
| `Empty results`      | Confirm that the contract is deployed  |

---

## 📄 License

This project is licensed under the **MIT License**.
