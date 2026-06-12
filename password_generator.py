import random
import string

# Get password length from user
length = int(input("Enter password length: "))

# Ensure minimum length is 2
if length < 2:
    print("Password length must be at least 2.")
else:
    # One random letter and one random digit
    password = [
        random.choice(string.ascii_letters),
        random.choice(string.digits)
    ]

    # Fill the remaining characters with letters and digits
    all_characters = string.ascii_letters + string.digits
    for _ in range(length - 2):
        password.append(random.choice(all_characters))

    # Shuffle the password so the first two characters are not predictable
    random.shuffle(password)

    # Convert list to string
    final_password = "".join(password)

    print("Generated Password:", final_password)