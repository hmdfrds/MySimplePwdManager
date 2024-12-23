from cryptography.fernet import Fernet
from constants import KEY_FILE_NAME, CREDENTIAL_FILE_NAME
import json


def load_key(key_filename=KEY_FILE_NAME):
    with open(key_filename, "rb") as key_file:
        return key_file.read()


def create_key(key_filename=KEY_FILE_NAME):
    key = Fernet.generate_key()
    with open(key_filename, "wb") as key_file:
        key_file.write(key)
    return key


def create_or_load_key(key_filename=KEY_FILE_NAME):
    try:
        key = load_key(key_filename)
    except FileNotFoundError:
        key = create_key(key_filename)
    return key


def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data)


def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()


def save_encrypted_json(data, key, credential_filename=CREDENTIAL_FILE_NAME):
    serialized_data = json.dumps(data).encode()
    encrypted_data = encrypt_data(serialized_data, key)

    with open(credential_filename, "wb") as file:
        file.write(encrypted_data)


def load_encrypted_json(key, credential_filename=CREDENTIAL_FILE_NAME):
    with open(credential_filename, "rb") as file:
        encrypted_data = file.read()

    serialized_data = decrypt_data(encrypted_data, key)
    return json.loads(serialized_data)
