# Ethereum Blockchain Log Storage System

![Ethereum](https://img.shields.io/badge/Ethereum-3C3C3D?style=for-the-badge&logo=Ethereum&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

A decentralized log storage system using Ethereum (Ganache) and Python for tamper-proof log management.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [1. Start Ganache](#1-start-ganache)
  - [2. Deploy the Contract](#2-deploy-the-contract)
  - [3. Store Logs](#3-store-logs)
  - [4. Retrieve Logs](#4-retrieve-logs)
  - [5. Verify Logs](#5-verify-logs)
- [Script Reference](#script-reference)
- [Smart Contract](#smart-contract)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Features
- ✔️ Store system logs on Ethereum blockchain
- ✔️ Retrieve logs with complete history
- ✔️ Cryptographic hash verification (SHA-256)
- ✔️ Local development with Ganache CLI
- ✔️ Simple Python Web3 interface

## Prerequisites

### System Requirements
- Linux OS (or WSL on Windows)
- Python 3.8+
- Node.js v14+
- npm

### Python Packages
```bash
pip install web3 py-solc-x
