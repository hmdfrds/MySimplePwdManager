import argparse
import json
from utils import save_encrypted_json, create_or_load_key, load_key, load_encrypted_json
from cryptography.fernet import InvalidToken


def initialize_parser():
    parser = argparse.ArgumentParser(description="Manage your credentials securely.")

    parser.add_argument(
        "command", choices=["store", "get", "list"], help="Command to execute."
    )
    parser.add_argument(
        "service", nargs="?", help="Service name for storeing or retrieving."
    )
    parser.add_argument("username", nargs="?", help="Username for storing credentials.")
    parser.add_argument("password", nargs="?", help="Password for storing credentials.")

    return parser


def store(service, username, password):
    try:
        credentials = {
            service: {
                "username": username,
                "password": password,
            }
        }
        key = create_or_load_key()
        save_encrypted_json(credentials, key)

    except Exception as e:
        print(f"Error while storing credential: {e}")


def get(service):
    try:
        key = load_key()
        credential = load_encrypted_json(key)[service.casefold()]
        print(service)
        print(f"Username:    {credential['username']}")
        print(f"Password:    {credential['password']}")
    except InvalidToken as e:
        print(f"Error while getting credential: {e}")
    except Exception as e:
        print(f"Error while getting credential: {e}")


def list():
    try:
        key = load_key()
        credentials = load_encrypted_json(key)
        for service, credential in credentials.items():
            print(service)
            print(f"Username:    {credential['username']}")
            print(f"Password:    {credential['password']}")
    except InvalidToken as e:
        print(f"Error while getting credential: {e}")
    except Exception as e:
        print(f"Error while getting credential: {e}")


def main():
    parser = initialize_parser()

    args = parser.parse_args()

    if args.command == "store":
        store(args.service, args.username, args.password)
    elif args.command == "get":
        get(args.service)
    elif args.command == "list":
        list()


if __name__ == "__main__":
    main()
