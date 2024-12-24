import pytest
from cryptography.fernet import Fernet
from utils import encrypt_data, decrypt_data, create_credential


def test_encrypt_decrypt_data():
    key = Fernet.generate_key()
    data = "Test Data"
    encrypted = encrypt_data(data.encode(), key)
    decrypt = decrypt_data(encrypted, key)
    assert decrypt == data
