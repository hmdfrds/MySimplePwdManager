from cryptography.fernet import Fernet
import json
from constants import CredentialKeys


def load_key(key_filename):
    with open(key_filename, "rb") as key_file:
        return key_file.read()


def create_key(key_filename):
    key = Fernet.generate_key()
    with open(key_filename, "wb") as key_file:
        key_file.write(key)
    return key


def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data)


def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()


def save_encrypted_json(data, key, credential_filename):
    serialized_data = json.dumps(data).encode()
    encrypted_data = encrypt_data(serialized_data, key)

    with open(credential_filename, "wb") as file:
        file.write(encrypted_data)


def load_encrypted_json(key, credential_filename):
    with open(credential_filename, "rb") as file:
        encrypted_data = file.read()

    serialized_data = decrypt_data(encrypted_data, key)
    return json.loads(serialized_data)


def create_credential(username, password):
    return {
        CredentialKeys.USERNAME: username,
        CredentialKeys.PASSWORD: password,
    }


def store_credential(service, username, password, key, credential_filename):

    try:
        credentials = load_encrypted_json(key, credential_filename)
    except FileNotFoundError:
        credentials = {}

    credentials[service.casefold()] = create_credential(username, password)
    save_encrypted_json(credentials, key, credential_filename)


def get_credential(service, key, credential_filename):
    return load_encrypted_json(key, credential_filename)[service.casefold()]


def get_all_credentials(key, credential_filename):
    return load_encrypted_json(key, credential_filename)
