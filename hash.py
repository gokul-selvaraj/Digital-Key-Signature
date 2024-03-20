import hashlib
import argparse

__authors__ = ["Elangovan", "Gajendhiran", "Hariharan", "Gokul"]
__description__ = "A Digital Key Signature Interdisciplinary Project"

parser = argparse.ArgumentParser(
    description=__description__,
    epilog="Developed by {}".format(", ".join(__authors__))
)

parser.add_argument("--hash",
                    help="Hash Algorithm to use. ie md5, sha1, sha256",
                    choices=['md5', 'sha1', 'sha256'],
                    default="sha256"
)

parser.add_argument("--encrypt",
                    help="Encryption algorithm to use. ie AES and RSA",
                    choices=['aes', 'rsa'],
                    default= "aes"
)

args = parser.parse_args()

msg = "Hello World!"
msg = hashlib.md5().hexdigest()
print(msg)

