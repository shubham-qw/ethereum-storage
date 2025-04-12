# 🛡️ Log-to-Blockchain SIEM using Ethereum Smart Contracts

This project demonstrates a simple **Security Information and Event Management (SIEM)** system that reads local system logs and securely stores them on the **Ethereum blockchain** using a **Solidity smart contract**. It is built with **Python**, **Web3.py**, and runs on a **Ganache** local blockchain instance.

---

## 🚀 Features

- Reads system logs from a specified file
- Deploys a Solidity smart contract on a local Ethereum network
- Stores log entries on-chain (first 5 entries to save gas)
- Fetches and displays stored logs from the blockchain

---

## 🧠 Smart Contract

The smart contract is written in Solidity and provides simple storage and retrieval of logs:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract LogStorage {
    string[] public logs;

    function storeLog(string memory log) public {
        logs.push(log);
    }

    function getLogs() public view returns (string[] memory) {
        return logs;
    }
}
