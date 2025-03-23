import argparse
import oqs
import os
import base64
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature

# Constants
KEY_DIR = "keys"
DILITHIUM_PUB = os.path.join(KEY_DIR, "public_dilithium.bin")
DILITHIUM_PRIV = os.path.join(KEY_DIR, "private_dilithium.bin")
ECDSA_PUB = os.path.join(KEY_DIR, "public_ecdsa.pem")
ECDSA_PRIV = os.path.join(KEY_DIR, "private_ecdsa.pem")


def ensure_key_dir():
    os.makedirs(KEY_DIR, exist_ok=True)


def generate_keys():
    ensure_key_dir()

    # Dilithium
    with oqs.Signature("Dilithium2") as sig:
        pub = sig.generate_keypair()
        priv = sig.export_secret_key()
        with open(DILITHIUM_PUB, "wb") as f:
            f.write(pub)
        with open(DILITHIUM_PRIV, "wb") as f:
            f.write(priv)

    # ECDSA
    private_key = ec.generate_private_key(ec.SECP256R1(), backend=default_backend())
    public_key = private_key.public_key()
    with open(ECDSA_PRIV, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()))
    with open(ECDSA_PUB, "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo))

    print("🔐 Keypair generated in", KEY_DIR)


def hybrid_sign(msg_file, sig_file):
    with open(msg_file, "rb") as f:
        msg = f.read()

    # Dilithium (signing and key export in same context)
    with oqs.Signature("Dilithium2") as sig:
        pub = sig.generate_keypair()
        priv = sig.export_secret_key()
        sig_d = sig.sign(msg)

    # Save keys
    ensure_key_dir()
    with open(DILITHIUM_PUB, "wb") as f:
        f.write(pub)
    with open(DILITHIUM_PRIV, "wb") as f:
        f.write(priv)

    # ECDSA
    if not os.path.exists(ECDSA_PRIV):
        generate_keys()
    with open(ECDSA_PRIV, "rb") as f:
        ecdsa_priv = serialization.load_pem_private_key(f.read(), password=None)
    sig_e = ecdsa_priv.sign(msg, ec.ECDSA(hashes.SHA256()))

    # Save hybrid signature (base64 encoded)
    combo = base64.b64encode(sig_d).decode() + ":" + base64.b64encode(sig_e).decode()
    with open(sig_file, "w") as f:
        f.write(combo)

    print("✍️ Hybrid signature written to", sig_file)


def hybrid_verify(msg_file, sig_file, dilithium_pubkey_file, ecdsa_pubkey_file):
    with open(msg_file, "rb") as f:
        msg = f.read()
    with open(sig_file, "r") as f:
        sig_d_b64, sig_e_b64 = f.read().split(":")
        sig_d = base64.b64decode(sig_d_b64)
        sig_e = base64.b64decode(sig_e_b64)

    # Verify Dilithium
    with open(dilithium_pubkey_file, "rb") as f:
        pub_d = f.read()
    with oqs.Signature("Dilithium2") as verifier:
        valid_d = verifier.verify(msg, sig_d, pub_d)
    print("✅ Dilithium signature: valid" if valid_d else "❌ Dilithium signature: invalid")

    # Verify ECDSA
    try:
        with open(ecdsa_pubkey_file, "rb") as f:
            pub_e = serialization.load_pem_public_key(f.read())
        pub_e.verify(sig_e, msg, ec.ECDSA(hashes.SHA256()))
        print("✅ ECDSA signature: valid")
    except InvalidSignature:
        print("❌ ECDSA signature: invalid")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🔐 Hybrid Dilithium + ECDSA Sign/Verify Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Generate
    subparsers.add_parser("gen", help="Generate keypairs")

    # Sign
    sign = subparsers.add_parser("sign", help="Sign a file with hybrid signature")
    sign.add_argument("--in", dest="infile", required=True)
    sign.add_argument("--out", dest="outfile", required=True)

    # Verify
    verify = subparsers.add_parser("verify", help="Verify hybrid signature")
    verify.add_argument("--in", dest="infile", required=True)
    verify.add_argument("--sig", dest="sigfile", required=True)
    verify.add_argument("--dilithium-pub", required=True)
    verify.add_argument("--ecdsa-pub", required=True)

    args = parser.parse_args()

    if args.command == "gen":
        generate_keys()
    elif args.command == "sign":
        hybrid_sign(args.infile, args.outfile)
    elif args.command == "verify":
        hybrid_verify(args.infile, args.sigfile, args.dilithium_pub, args.ecdsa_pub)
    else:
        parser.print_help()
