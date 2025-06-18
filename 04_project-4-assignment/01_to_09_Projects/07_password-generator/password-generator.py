import random

print("Welcome to the Password Generator!")

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+;:,.~"

number = int(input("Enter the number of passwords to generate: "))

password_length = int(input("Enter the number of characters: "))

print('\nYour Passwords:')

for pwd in range(number):
    passwords = ''
    for c in range(password_length):
        passwords += random.choice(characters)

    print(passwords)
print("\nPasswords generated successfully!")
print("You can now use these passwords for your accounts.")
print("\nThank you for using the Password Generator!") 

# This code generates a specified number of random passwords with a given length using a mix of characters.