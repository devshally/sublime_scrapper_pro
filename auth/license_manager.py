# 3e5db78ec67641fc688850c995cdc2c8
import os
import requests
import uuid
from cryptography.fernet import Fernet
from typing import Optional

SERVER_URL = "https://sublime-license-validator.onrender.com/validate"
LICENSE_FILE = "license.enc"
KEY_FILE = "key.key"

class Licensor:
    def __init__(self):
        if not os.path.exists(KEY_FILE):
            self.key = Fernet.generate_key()
            with open(KEY_FILE, "wb") as key_file:
                key_file.write(self.key)
        else:
            with open(KEY_FILE, "rb") as key_file:
                self.key = key_file.read()
        self.cipher_suite = Fernet(self.key)

    def get_hardware_id(self) -> str:
        return str(uuid.getnode())

    def validate_license(self, license_key: str) -> bool:
        payload = {
            "license_key": license_key,
            "user_id": self.get_hardware_id()
        }
        try:
            response = requests.post(SERVER_URL, json=payload)
            response.raise_for_status()
            result = response.json()
            return result.get("status") == "success"
        except Exception:
            return False

    def encrypt_license_key(self, license_key: str) -> None:
        encrypted_key = self.cipher_suite.encrypt(license_key.encode())
        with open(LICENSE_FILE, "wb") as license_file:
            license_file.write(encrypted_key)

    def decrypt_license_key(self) -> Optional[str]:
        if not os.path.exists(LICENSE_FILE):
            return None
        try:
            with open(LICENSE_FILE, "rb") as license_file:
                encrypted_key = license_file.read()
            return self.cipher_suite.decrypt(encrypted_key).decode()
        except Exception as e:
            print(f"Decryption error: {e}")
            return None

    def check_license(self) -> bool:
        if not os.path.exists(LICENSE_FILE):
            return False
        license_key = self.decrypt_license_key()
        if not license_key:
            print("Invalid or corrupted license file.")
            os.remove(LICENSE_FILE)
            return False
        if self.validate_license(license_key):
            print("✅ License validated.")
            return True
        else:
            print("❌ License invalid.")
            os.remove(LICENSE_FILE)
            return False

    def run_license_flow(self, parent=None) -> bool:
        if self.check_license():
            return True
        return False
