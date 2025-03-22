import oqs

with oqs.Signature("Dilithium2") as signer:
    public_key = signer.generate_keypair()
    private_key = signer.export_secret_key()

    message = b"Surya is learning quantum-safe crypto!"

    signature = signer.sign(message)

    with oqs.Signature("Dilithium2") as verifier:
        is_valid = verifier.verify(message, signature, public_key)
        print("✔ Signature valid?", is_valid)

    tampered = b"Surya is hacking the matrix!"
    with oqs.Signature("Dilithium2") as verifier:
        is_valid = verifier.verify(tampered, signature, public_key)
        print("❌ Tampered message valid?", is_valid)
