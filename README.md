# 🔐 PQC Dilithium CLI Tool

A simple, working CLI demo of post-quantum digital signatures using [**Dilithium2**](https://csrc.nist.gov/projects/post-quantum-cryptography) from the [Open Quantum Safe](https://openquantumsafe.org) project. Built with Python and Docker.

---

## 🚀 What This Project Does

- 🛡 Generates a quantum-safe Dilithium2 keypair  
- ✍ Signs any file using the private key  
- ✅ Verifies a file using the public key  
- ❌ Detects tampered files  
- 💾 Exports public + private key to `./keys/`  
- 🧰 CLI-based signing & verification — no extra UI

---

## 🧩 Clone the Repo & CD Into It

```bash
git clone https://github.com/surya4682/pqc-dilithium-demo.git
cd pqc-dilithium-demo
```

---

## 🐳 How to Run (in 5 Steps)

1. **Build the Docker image**  
   ```bash
  sudo docker build -t pqc-dilithium-demo .
   ```

2. **Create a message to sign**  
   ```bash
   sudo echo "Quantum is the future." > message.txt
   ```

3. **Sign the message**  
   ```bash
   sudo docker run --rm -v "$PWD":/app pqc-dilithium-demo \
     python3 cli_dilithium.py sign --in message.txt --out message.sig
   ```

4. **Verify the message**  
   ```bash
   sudo docker run --rm -v "$PWD":/app pqc-dilithium-demo \
     python3 cli_dilithium.py verify --in message.txt --sig message.sig --pub keys/public_key.bin
   ```

5. **(Optional) Tamper and test verification failure**  
   ```bash
   echo "I changed the message" > message.txt

   sudo docker run --rm -v "$PWD":/app pqc-dilithium-demo \
     python3 cli_dilithium.py verify --in message.txt --sig message.sig --pub keys/public_key.bin
   ```

> ℹ On **Windows with WSL**, make sure **Docker Desktop** is running.

---

## 💡 Expected Output

```
🔐 Keypair generated
✍️ Message signed: message.sig
✅ Signature valid?
```

If the message is tampered:
```
❌ Invalid signature
```

---

## 📦 Tech Stack

- Python 3.10 (inside Docker)  
- [liboqs](https://github.com/open-quantum-safe/liboqs)  
- [liboqs-python](https://github.com/open-quantum-safe/liboqs-python)  
- Docker

---

## 📁 Files

| File              | Description                                    |
|-------------------|------------------------------------------------|
| `cli_dilithium.py`| CLI tool for signing and verifying files       |
| `Dockerfile`      | Builds the container with all dependencies     |
| `README.md`       | You’re reading it                              |
| `keys/`           | Folder that holds generated keypair            |
| `message.txt`     | Input message to be signed                     |
| `message.sig`     | Output signature from the input message        |

---

## 🧠 Why I Made This

I was learning about post-quantum cryptography and wanted a real working example — but found the setup hard, buggy, and confusing. So I made this:

- 🔧 Clean  
- 💡 Easy to understand  
- 🧪 Demo-ready in seconds

---

## 🙌 Credits

- Open Quantum Safe  
- liboqs  
- liboqs-python

---

## 🔗 License

MIT License. Use, fork, or build on top of it.

Built by **Surya** 🔐💻
