Pure Python Blockchain Engine ⛓️
A First-Principles Implementation of a Cryptographic Ledger
📌 Overview
This project is a functional blockchain engine built entirely from scratch in pure Python. Instead of relying on external frameworks, this engine was developed to demonstrate a ground-up understanding of decentralized systems, cryptographic hashing, and consensus mechanisms.
⚙️ Core Architecture
The Block Class
Each block in the chain serves as an immutable record containing:
Index & Timestamp: For sequential tracking.
Miner ID: To identify the node/user that successfully mined the block.
Data Payload: The core transaction data or message stored in the block.
Cryptographic Hash (SHA-256): The unique digital signature of the current block.
Previous Hash: The cryptographic link to the preceding block, ensuring chain integrity.
Nonce: The mathematical variable adjusted during the Proof-of-Work process.
The Blockchain Class
The ledger manager that maintains the integrity of the chain:
Genesis Block Generation: Automatically instantiates the foundational block upon chain creation.
Chain Validation: Ensures every new block's previous hash perfectly matches the actual hash of the prior block.
Proof of Work (Mining)
Implemented a dynamic mining system where blocks cannot be instantly added. The system requires computational work (adjusting the nonce) until a valid hash meeting the difficulty target is generated.
🚀 Technical Stack
Language: Python 3.x
Libraries: hashlib (Standard Library) - No third-party dependencies used.
Paradigm: Object-Oriented Programming (OOP)
💡 Key Learnings
Constructing secure, linked data structures.
Understanding how state changes affect cryptographic signatures.
Implementing localized Proof-of-Work algorithms.
