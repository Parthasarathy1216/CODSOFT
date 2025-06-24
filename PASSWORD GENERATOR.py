import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Combine letters, digits, and symbols
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# User Input
try:
    user_length = int(input("Enter the desired password length: "))
    password = generate_password(user_length)
    print(f"Generated Password: {password}")
except ValueError:
    print("Please enter a valid number.")
