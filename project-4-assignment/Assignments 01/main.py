# <======================== 01_basics Assignments: ==================================>

# Assignment 00 Basics: A simple joke bot that responds to "Joke" (case-insensitive) or prints a sorry message.

PROMPT: str = "What do you want? "
JOKE: str = ("Here is a joke for you! Sophia is heading out to the grocery store. "
             "A programmer tells her: get a liter of milk, and if they have eggs, get 12. "
             "Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'")
SORRY: str = "Sorry I only tell jokes."

def main():
    user_input = input(PROMPT).strip().lower()
    
    if user_input == "joke":
        print(JOKE)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()


# Assignment 01 Basics: Doubles the input number until it reaches 100 or more.

def main():
    curr_value = int(input("Enter a number: "))  
    
    while curr_value < 100:
        curr_value *= 2 
        print(curr_value, end=" ") 

if __name__ == '__main__':
    main()


# Assignment 02 Basics: Prints a countdown from 10 to 1, followed by "Liftoff".

def main():
    for i in range(10, 0, -1): 
        print(i, end=" ")
    print("Liftoff")  

if __name__ == '__main__':
    main()


# Assignment 03 Basics: Selects a random number between 1 and 99 and asks the user to guess it.

import random
def main():
    secret_number = random.randint(1, 99)
    guess = int(input("I am thinking of a number between 1 and 99... Enter a guess: "))  
    
    while guess != secret_number:
        if guess > secret_number:
            print("Your guess is too high")
        else:
            print("Your guess is too low")

        guess = int(input("Enter a new number: "))
    
    print(f"Congrats! The number was: {secret_number}")
if __name__ == '__main__':
    main()


# Assignment 04 Basics: Generates and prints 10 random numbers between 1 and 100

import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")

if __name__ == '__main__':
    main()



# <======================= 02_intermediate Assignments: ============================>
# Assignments 01 intermediate: High-Low game Guess higher or lower

import random

NUM_ROUNDS = 5 
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    score = 0

    for round_number in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_number}")
        user_number = random.randint(MIN_VALUE, MAX_VALUE)
        computer_number = random.randint(MIN_VALUE, MAX_VALUE)
        print(f"Your number is {user_number}")
        
        while True:
            user_guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
            if user_guess in ["higher", "lower"]:
                break
            print("Invalid input! Please enter either 'higher' or 'lower'.")
        
        if (user_guess == "higher" and user_number > computer_number) or (user_guess == "lower" and user_number < computer_number):
            print("You were right!", end=" ")
            score += 1
        else:
            print("Aww, that's incorrect.", end=" ")
        
        print(f"The computer's number was {computer_number}")
        print(f"Your score is now {score}\n")
    
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == '__main__':
    main()


# Assignments 02 intermediate: Planetary Weight Calculator

MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():

    earth_weight_str = input("Enter a weight on Earth: ")
    earth_weight = float(earth_weight_str)
    
    planet = input("Enter a planet: ").capitalize()
    
    if planet == "Mercury":
        planetary_weight = earth_weight * MERCURY_GRAVITY
    elif planet == "Venus":
        planetary_weight = earth_weight * VENUS_GRAVITY
    elif planet == "Mars":
        planetary_weight = earth_weight * MARS_GRAVITY
    elif planet == "Jupiter":
        planetary_weight = earth_weight * JUPITER_GRAVITY
    elif planet == "Saturn":
        planetary_weight = earth_weight * SATURN_GRAVITY
    elif planet == "Uranus":
        planetary_weight = earth_weight * URANUS_GRAVITY
    elif planet == "Neptune":
        planetary_weight = earth_weight * NEPTUNE_GRAVITY
    else:
        print("Invalid planet name.")
        return 
    
    rounded_weight = round(planetary_weight, 2)
    print("The equivalent weight on " + planet + ": " + str(rounded_weight))

if __name__ == "__main__":
    main()


# Assignments 03 intermediate: List Practice

def main():
    fruit_list = ["apple", "banana", "orange", "grape", "pineapple"]
    print(len(fruit_list))
    fruit_list.append("mango")
    print(fruit_list)
    print(len(fruit_list))

if __name__ == "__main__":
    main()


# Assignments 04 intermediate: Index Game

def access_element(lst, index):

    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range."

def modify_element(lst, index, new_value):
    
    if 0 <= index < len(lst):
        lst[index] = new_value
        return lst
    else:
        return "Index out of range."

def slice_list(lst, start, end):
    
    if 0 <= start < len(lst) and 0 <= end <= len(lst) and start < end:
        return lst[start:end]
    else:
        return "Invalid range."
    
def main():
    my_list = [10, 20, 30, 40, 50]
    
    while True:
        print("\nChoose an operation:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice list")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            index = int(input("Enter index to access: "))
            print("Element:", access_element(my_list, index))
        
        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print("Updated list:", modify_element(my_list, index, new_value))
        
        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced list:", slice_list(my_list, start, end))
        
        elif choice == '4':
            print("Exiting game.")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
