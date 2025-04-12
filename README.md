# 🛡️ Log-to-Blockchain SIEM with Ethereum Smart Contracts

This project is a simple **Security Information and Event Management (SIEM)** system that reads system logs from a file and stores them on the **Ethereum blockchain** using a **Solidity smart contract**. It uses **Python, Web3.py**, and **Ganache** as a local Ethereum testnet.

---

## 🚀 Features

- Reads local system logs (e.g., `/home/kali/siem/system_log.txt` or `/var/log/syslog`)
- Deploys a Solidity smart contract to store and retrieve log entries
- Stores logs securely on the blockchain to ensure tamper-proof storage
- Uses Ganache as a local Ethereum blockchain simulator

---

## 📦 Requirements

- Python 3.7+
- Ganache (running on `http://127.0.0.1:7545`)
- Dependencies:
  - `web3`
  - `py-solc-x`

⚙️ How to Run the Project
1. Start Ganache
Make sure Ganache is installed and running on your machine.

GUI: Open the Ganache desktop app and start a workspace.

CLI: If you're using the CLI version, run:

bash
Copy
Edit
ganache-cli
Ganache must be running on: http://127.0.0.1:7545

2. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/log-to-blockchain-siem.git
cd log-to-blockchain-siem
3. Run the Python Script
Make sure you're in the directory where main.py is located:

bash
Copy
Edit
python3 main.pypip install web3 py-solc-x
```
