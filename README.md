# 🔐 PQC Dilithium Signature Demo

A simple, working demo of post-quantum digital signatures using [Dilithium2](https://csrc.nist.gov/Projects/post-quantum-cryptography) from the [Open Quantum Safe](https://openquantumsafe.org/) project. Built with Python and Docker.

> Created by Surya — so you don’t have to go through the painful setup I did. This one **just works**.

---

## 🚀 What This Project Does

- 🛡️ Generates a quantum-safe Dilithium2 keypair
- ✍️ Signs a message using the private key
- ✅ Verifies the message using the public key
- ❌ Detects tampered messages

---

## 🐳 How to Run (in 2 Steps)

### 1. Build the Docker image

```bash
docker build -t pqc-dilithium .
```

### 2. Run the demo

```bash
docker run --rm pqc-dilithium
```

---

## 💡 Expected Output

```bash
✔ Signature valid? True
❌ Tampered message valid? False
```

---

## 📦 Tech Stack

- Python 3.10 (inside Docker)
- [liboqs](https://github.com/open-quantum-safe/liboqs)
- [liboqs-python](https://github.com/open-quantum-safe/liboqs-python)
- Docker

---

## 📁 Files

| File               | Description                                  |
|--------------------|----------------------------------------------|
| `dilithium_demo.py`| Main script with signing + verification logic|
| `Dockerfile`       | Builds the container with all dependencies   |
| `README.md`        | You’re reading it                            |

---

## 🧠 Why I Made This

I was learning about post-quantum cryptography and wanted a **real working example** — but found the setup hard, buggy, and confusing.

So I made this:
- 🔧 Clean
- 💡 Easy to understand
- 🧪 Demo-ready in seconds

Now you don’t have to waste time — you can just run it and learn.

---

## ⚠️ Troubleshooting

If you get Docker permission issues on Linux, try:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

Then log out and log back in.

---

## 📌 Coming Soon

- ✅ File signing/verification
- 🗝️ Export/import public keys
- 🧰 CLI tool (sign + verify commands)

---

## 🙌 Credits

- [Open Quantum Safe](https://github.com/open-quantum-safe)
- [liboqs](https://github.com/open-quantum-safe/liboqs)
- [liboqs-python](https://github.com/open-quantum-safe/liboqs-python)

---

## 🔗 License

MIT License. Use, fork, or build on top of it.

---

Built with love (and frustration) by Surya 🔐💻
