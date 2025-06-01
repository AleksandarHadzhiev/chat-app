from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


class RSAGenerator:
    """Using the cryptogrpahy library, this class generates the secrets for the application.
    The secrets are used for generating and decoding JWTs. The password is a value provided
    when the app is started via an argument to the command, so that the password is safely
    hidden from the codebase.
    """

    def __init__(self, password: str):
        self._password = password.encode()
        self._generate_private_key()
        self._encrypt_private_key()
        self._generate_public_key()
        self._generate_key()

    def _generate_private_key(self):
        self._private_key = rsa.generate_private_key(
            public_exponent=65537, key_size=2048
        )

    def _encrypt_private_key(self):
        self._encrypted_private_key = self._private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(self._password),
        )

    def _generate_public_key(self):
        self._public_key = self._private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )

    def _generate_key(self):
        self._key = serialization.load_pem_private_key(
            self._encrypted_private_key, self._password
        )

    def get_private_key(self):
        return self._key

    def get_public_key(self):
        return serialization.load_pem_public_key(self._public_key, self._password)
