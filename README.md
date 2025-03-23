# 🔐 Hybrid Dilithium + ECDSA CLI Tool

A working CLI demo of hybrid digital signatures using [**Dilithium2**](https://csrc.nist.gov/projects/post-quantum-cryptography) (post-quantum) from the [Open Quantum Safe](https://openquantumsafe.org) project and [**ECDSA**](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm) (classical) cryptography. Built with Python, [liboqs](https://github.com/open-quantum-safe/liboqs), and Docker.

---

## 🚀 What This Project Does

- 🔐 Generates both Dilithium2 and ECDSA keypairs  
- ✍️ Creates a hybrid signature with both algorithms  
- ✅ Verifies each signature independently  
- ❌ Detects tampered messages  
- 📦 Saves signatures as base64-encoded strings  
- 📂 Stores key files inside `./keys/` folder  

---

## 🧩 Clone the Repo & CD Into It

```bash
git clone https://github.com/surya4682/pqc-dilithium-demo.git
```
```bash
cd pqc-dilithium-demo
```

---

## 🐳 How to Run 

1. **Build the Docker image**  
   ```bash
   sudo docker build -t pqc-dilithium-demo .
   ```

2. **Create a message to sign**  
   ```bash
   echo "Quantum + Classical = Hybrid Secure" > message.txt
   ```

3. **Key generation**  
   ```bash
   sudo docker run --rm -v "$PWD":/app pqc-dilithium-demo python3 cli_hybrid.py gen
   ```

4. **Sign the file with a hybrid signature**  
   ```bash
   sudo docker run --rm -v "$PWD":/app pqc-dilithium-demo python3 cli_hybrid.py sign --in message.txt --out hybrid.sig
   ```

5. **Verify the hybrid signature**  
   ```bash
   sudo docker run --rm -v "$PWD":/app pqc-dilithium-demo python3 cli_hybrid.py verify --in message.txt --sig hybrid.sig --dilithium-pub keys/public_dilithium.bin --ecdsa-pub keys/public_ecdsa.pem
   ```

6. **(Optional) Tamper and test verification failure**  
   ```bash
   echo "I changed the message" > message.txt
   ```
   ```bash
   sudo docker run --rm -v "$PWD":/app pqc-dilithium-demo python3 cli_hybrid.py verify --in message.txt --sig hybrid.sig --dilithium-pub keys/public_dilithium.bin --ecdsa-pub keys/public_ecdsa.pem
   ```
---

## 💡 Expected Output

```
🔐 Keypair generated in keys
✍ Hybrid signature written to hybrid.sig
✅ Dilithium signature: valid
✅ ECDSA signature: valid

```

If the message is tampered:

```
❌ Dilithium signature: invalid
❌ ECDSA signature: invalid

```

---

## 📦 Tech Stack

- Python 3.10 (inside Docker)  
- [liboqs](https://github.com/open-quantum-safe/liboqs)  
- [liboqs-python](https://github.com/open-quantum-safe/liboqs-python)
- [Python Cryptography (for ECDSA)](https://cryptography.io/en/latest/)
- Docker

---

## 📁 Files

| File              | Description                                    |
|-------------------|------------------------------------------------|
| `cli_hybrid.py`   | CLI tool for hybrid signing and verification   |
| `Dockerfile`      | Builds the container with all dependencies     |
| `README.md`       | You’re reading it                              |
| `keys/`           | Folder that holds generated keypair files      |
| `message.txt`     | Input message to be signed                     |
| `hybrid.sig	`    | Output signature combining Dilithium + ECDSA   |

---

## 🧠 Why I Made This

Hybrid signatures are essential during the transition to post-quantum cryptography. This tool shows how you can combine PQC and classical crypto into one simple, verifiable signature — easy to run, test, and learn.

- 🔧 Clean  
- 💡 Easy to understand  
- 🧪 Demo-ready in seconds

---

## 🙌 Credits

- Open Quantum Safe  
- liboqs  
- liboqs-python
- Python Cryptography

---

## 🔗 License

MIT License. Use, fork, or build on top of it.

---

Built by **Surya** 🔐💻
