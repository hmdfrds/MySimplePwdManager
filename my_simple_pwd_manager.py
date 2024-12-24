import argparse
import json
from constants import CredentialKeys
from password_manager import PasswordManager


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
    parser.add_argument(
        "-s", "--showpassword", action="store_true", help="Enable to show password."
    )
    return parser


def main():
    parser = initialize_parser()

    args = parser.parse_args()

    pm = PasswordManager()
    if args.command == "store":
        pm.store(args.service, args.username, args.password)

    elif args.command == "get":
        credential = pm.get(args.service)
        print(f"Username:    {credential[CredentialKeys.USERNAME]}")
        if args.showpassword:
            print(f"Password:    {credential[CredentialKeys.PASSWORD]}")
        else:
            print(f"Password:    ********")
    elif args.command == "list":
        credentials = pm.list()
        for service, credential in credentials.items():
            print(service)
            print(f"Username:    {credential[CredentialKeys.USERNAME]}")
        if args.s:
            print(f"Password:    {credential[CredentialKeys.PASSWORD]}")
        else:
            print(f"Password:    ********")


if __name__ == "__main__":
    main()
