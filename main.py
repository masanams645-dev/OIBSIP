import random
import string

print("===== RANDOM PASSWORD GENERATOR =====")

while True:

    try:
        length = int(input("\nEnter password length (minimum 8): "))

        if length < 8:
            print("Error: Password length must be at least 8.")
            continue

        print("\nChoose character types:")
        print("1. Uppercase letters")
        print("2. Lowercase letters")
        print("3. Numbers")
        print("4. Symbols")

        choices = input("Enter your choices (example: 123): ")

        if len(choices) < 2:
            print("Error: Please select at least 2 character types.")
            continue

        characters = ""

        if "1" in choices:
            characters += string.ascii_uppercase

        if "2" in choices:
            characters += string.ascii_lowercase

        if "3" in choices:
            characters += string.digits

        if "4" in choices:
            characters += string.punctuation

        if characters == "":
            print("Error: Please select valid character types.")
            continue

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:", password)

        again = input("\nGenerate another password? (yes/no): ")

        if again.lower() != "yes":
            print("\nThank you for using the Password Generator!")
            break

    except ValueError:
        print("Error: Please enter a valid number.")