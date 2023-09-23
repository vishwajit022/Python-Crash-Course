import random
import string

def generate_password(length):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting characters randomly
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    
    if password_length < 8:
        print("Password length should be at least 8 characters.")
    else:
        password = generate_password(password_length)
        print("Generated password:", password)
