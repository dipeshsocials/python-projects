import random
import string

print("===== Password Generator =====")

while True:
    try:
        length = int(input("Enter password length (minimum 4): "))

        if length < 4:
            print("Password length must be at least 4.\n")
            continue

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = "".join(random.choice(characters) for _ in range(length))

        print("\nGenerated Password:")
        print(password)
        break

    except ValueError:
        print("Please enter a valid number.\n")
