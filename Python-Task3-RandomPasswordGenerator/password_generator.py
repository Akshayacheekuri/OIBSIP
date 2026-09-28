import random
import string

print("===== Random Password Generator =====")

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Please enter a positive password length.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        print("\nGenerated Password:", password)

except ValueError:
    print("Invalid input. Please enter a whole number.")
