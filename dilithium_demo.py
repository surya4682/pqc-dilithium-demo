import oqs

# 1. Create a Dilithium2 signature keypair
with oqs.Signature("Dilithium2") as signer:
    public_key = signer.generate_keypair()
    private_key = signer.export_secret_key()

    message = b"Surya is learning quantum-safe crypto!"

    # Export public key to file
    with open("public_key.bin", "wb") as f:
        f.write(public_key)

    # 2. Sign the message
    signature = signer.sign(message)

    # 3. Verify the signature
    with oqs.Signature("Dilithium2") as verifier:
        is_valid = verifier.verify(message, signature, public_key)
        print("✔ Signature valid?", is_valid)

    # 4. Tamper with the message
    tampered = b"Surya is hacking the matrix!"
    with oqs.Signature("Dilithium2") as verifier:
        is_valid = verifier.verify(tampered, signature, public_key)
        print("❌ Tampered message valid?", is_valid)
