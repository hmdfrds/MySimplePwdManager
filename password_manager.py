from constants import KEY_FILE_NAME, CREDENTIAL_FILE_NAME, CredentialKeys
from utils import (
    load_key,
    create_key,
    store_credential,
    get_credential,
    get_all_credentials,
)
from cryptography.fernet import InvalidToken


class PasswordManager:
    def __init__(
        self, key_filename=KEY_FILE_NAME, credential_filename=CREDENTIAL_FILE_NAME
    ):
        self.key_filename = key_filename
        self.credential_filename = credential_filename
        self.key = self._create_or_load_key()

    def _create_or_load_key(self):
        try:
            key = load_key(self.key_filename)
        except FileNotFoundError:
            key = create_key(self.key_filename)
        return key

    def store(self, service, username, password):
        try:
            credentials = get_all_credentials(self.key, self.credential_filename)
            exist = service.casefold() in credentials
        except:
            exist = False
        try:

            if exist:
                confirm = input(f"Service '{service}' already exists. Ovewrite? (y/n):")
                if confirm.strip().lower() != "y":
                    print("Operation canceled.")
                    return
            store_credential(
                service, username, password, self.key, self.credential_filename
            )
            print(f"Credentials for '{service}' stored successfully.")
        except Exception as e:
            print(f"Error while storing credential: {e}")

    def get(self, service):
        try:
            return get_credential(service, self.key, self.credential_filename)
        except KeyError:
            print(f"Service '{service}' not found.")
        except InvalidToken:
            print(f"Invalid encryption key or corrupted data.")
        except FileNotFoundError:
            print("Credential file not found. Please store a credential first.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def list(self):
        try:
            return get_all_credentials(self.key, self.credential_filename)
        except InvalidToken:
            print(f"Invalid encryption key or corrupted data.")
        except FileNotFoundError:
            print("Credential file not found. Please store a credential first.")
        except Exception as e:
            print(f"Unexpected error: {e}")
