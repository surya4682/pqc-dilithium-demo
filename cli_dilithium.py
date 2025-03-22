import argparse
import oqs
import os

KEYPAIR_DIR = "./keys"
PUB_KEY_FILE = os.path.join(KEYPAIR_DIR, "public_key.bin")

def generate_and_sign(input_file, output_sig):
    os.makedirs(KEYPAIR_DIR, exist_ok=True)

    # Read message
    with open(input_file, "rb") as f:
        message = f.read()

    # Generate keypair
    with oqs.Signature("Dilithium2") as signer:
        public_key = signer.generate_keypair()
        signature = signer.sign(message)

    # Save signature and public key
    with open(output_sig, "wb") as f:
        f.write(signature)
    with open(PUB_KEY_FILE, "wb") as f:
        f.write(public_key)

    print("🔐 Keypair generated and message signed.")

def verify(input_file, signature_file, pub_key_file):
    with open(input_file, "rb") as f:
        message = f.read()
    with open(signature_file, "rb") as f:
        signature = f.read()
    with open(pub_key_file, "rb") as f:
        pubkey = f.read()

    with oqs.Signature("Dilithium2") as verifier:
        is_valid = verifier.verify(message, signature, pubkey)
        print("✅ Signature valid?" if is_valid else "❌ Invalid signature")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🛡️ Dilithium2 File Sign & Verify CLI")
    subparsers = parser.add_subparsers(dest="command")

    # sign
    sign_parser = subparsers.add_parser("sign", help="Sign a file")
    sign_parser.add_argument("--in", dest="infile", required=True)
    sign_parser.add_argument("--out", dest="outfile", required=True)

    # verify
    verify_parser = subparsers.add_parser("verify", help="Verify a signed file")
    verify_parser.add_argument("--in", dest="infile", required=True)
    verify_parser.add_argument("--sig", dest="sigfile", required=True)
    verify_parser.add_argument("--pub", dest="pubkey", required=True)

    args = parser.parse_args()

    if args.command == "sign":
        generate_and_sign(args.infile, args.outfile)
    elif args.command == "verify":
        verify(args.infile, args.sigfile, args.pubkey)
    else:
        parser.print_help()
