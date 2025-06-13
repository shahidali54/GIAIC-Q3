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
print("\nThank you for using the Password Generator!")


#     for round_number in range(1, NUM_ROUNDS + 1):
#         secret_number = random.randint(MIN_VALUE, MAX_VALUE)
#         guess = int(input(f"Round {round_number}: Guess a number between {MIN_VALUE} and {MAX_VALUE}: "))
#         if guess == secret_number:
#             print("Correct! You guessed the number.")