import secrets
import string

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def generate_bulk_passwords(num_passwords, length):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

if __name__ == "__main__":
    num_passwords = int(input("Enter the number of passwords: "))
    length = int(input("Enter the length of each password: "))
    passwords = generate_bulk_passwords(num_passwords, length)
    for password in passwords:
        print(password)

