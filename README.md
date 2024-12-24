# MySimplePwdManager

Simple CLI password manager written in Python.

## Description

Store, retrieve, and manage credentials (username/password) securely via the command line. It encrypts all data using `cryptography.fernet`

## Features

- **Store Credentials**
- **Retrieve Credentials**
  
## Installation

1. Clone the repository:

   ```bash
    git clone https://github.com/hmdfrds/MySimplePwdManager.git
    cd MySimplePwdManager
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script wit the desired command:

### Store a Credential

```bash
python my_simple_pwd_manager.py store <service> <username> <password>
```

### Retrieve a Credential

```bash
python my_simple_pwn_manager.py get <service>
```

### List All Services

```bash
python my_simple_pwd_manager.py list
```

### Help

```bash
python my_simple_pwd_mamager.py -h
```

## Examples

- Store credential for Gmail:

    ```bash
    python my_simple_pwd_manager.py store gmail user@gmail.com password123
    ```

- Retrieve Gmail credentials:

    ```bash
    python my_simple_pwd_manager.py get gmail -s
    ```

    Use `-s` or `--showpassword` to unobsecure the password.

- List all services:

    ```bash
    python my_simple_pwd_manager.py list
    ```

## Testing

Run tests using:

```bash
pytest
```

## Security Notes

- The encryption key (`key.txt`) is required to access stored credentials. If the key is lost, data cannot be decrypted.
- Do not share the encryption key (`key.txt`) or encrypted file (`credentials.json.enc`) with others.

## Project Status

I have implemented all the expected features for this project, and it is now considered **complete**.

## Author

This project was created for learning purposes.

## License

MIT License. See [License](LICENSE).
