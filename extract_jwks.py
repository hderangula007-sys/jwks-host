from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import base64

with open("private.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())

pub = private_key.public_key()
pub_numbers = pub.public_numbers()

def b64url(n):
    length = (n.bit_length() + 7) // 8
    return base64.urlsafe_b64encode(n.to_bytes(length, 'big')).rstrip(b'=').decode()

print("n:", b64url(pub_numbers.n))
print("e:", b64url(pub_numbers.e))
