# 🔐 PQC Dilithium Signature Demo

A simple, working demo of post-quantum digital signatures using [**Dilithium2**](https://csrc.nist.gov/projects/post-quantum-cryptography) from the [Open Quantum Safe](https://openquantumsafe.org) project. Built with Python and Docker.

---

## 🚀 What This Project Does

- 🛡 Generates a quantum-safe Dilithium2 keypair  
- ✍ Signs a message using the private key  
- ✅ Verifies the message using the public key  
- ❌ Detects tampered messages  
- 💾 Exports the public key to `public_key.bin`

---

## 🐳 How to Run (in 2 Steps)

1. **Build the Docker image**

```bash
docker build -t pqc-dilithium-demo .
```

2. **Run the demo**

```bash
docker run --rm -v "$PWD":/app pqc-dilithium-demo
```

> ℹ On Windows with WSL, make sure Docker Desktop is running.

---

## 💡 Expected Output

```
✔ Signature valid? True  
❌ Tampered message valid? False
```

A file called `public_key.bin` will also be created in your current directory.

---

## 📦 Tech Stack

- Python 3.10 (inside Docker)
- [liboqs](https://github.com/open-quantum-safe/liboqs)
- [liboqs-python](https://github.com/open-quantum-safe/liboqs-python)
- Docker

---

## 📁 Files

| File              | Description                                  |
|-------------------|----------------------------------------------|
| `dilithium_demo.py` | Main script with signing + verification logic |
| `Dockerfile`      | Builds the container with all dependencies   |
| `README.md`       | You’re reading it                            |
| `public_key.bin`  | Exported public key from the signature demo  |

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

---

Built by **Surya** 🔐💻
