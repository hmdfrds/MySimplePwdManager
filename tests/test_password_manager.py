import pytest
from password_manager import PasswordManager
from constants import CredentialKeys


@pytest.fixture
def password_manager(tmp_path):
    key_file = tmp_path / "key.txt"
    credential_file = tmp_path / "credentials.json.enc"
    return PasswordManager(key_filename=key_file, credential_filename=credential_file)


def test_store_and_get(password_manager):
    password_manager.store("gmail", "user", "pass")
    credential = password_manager.get("gmail")
    assert credential[CredentialKeys.USERNAME] == "user"
    assert credential[CredentialKeys.PASSWORD] == "pass"


def test_list(password_manager):

    password_manager.store("github", "dev", "password123")
    password_manager.store("gmail", "user", "pass")
    credentials = password_manager.list()
    assert "gmail" in credentials
    assert "github" in credentials


def test_get_nonexistent_service(password_manager):
    assert password_manager.get("nonexistent") == None
