# Assignment 01: Sum of Two Numbers.

def main():
    
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    total = num1 + num2
    
    print(f"The total is {total}.")

if __name__ == '__main__':
    main()


# Assignment 02: Favorite Animal

def main():
    animal = input("What's your favorite animal? ")

    print(f"My favorite animal is also {animal}")

if __name__ == '__main__':
    main()


# Assignment 03: Fahrenheit to Celsius Converter

def main():
    
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

    print("Temperature:", degrees_fahrenheit, "F =", degrees_celsius, "C")

if __name__ == '__main__':
    main()


# Assignment 04: Age Calculation
def main():
    
    anton = 21
    beth = anton + 6
    chen = beth + 20
    drew = chen + anton
    ethan = chen 

    print(f"Anton is {anton}")
    print(f"Beth is {beth}")
    print(f"Chen is {chen}")
    print(f"Drew is {drew}")
    print(f"Ethan is {ethan}")

if __name__ == '__main__':
    main()


# Assignment 05: Triangle Perimeter Calculation
def main():
    
    s1 = float(input("What is the length of side 1? "))
    s2 = float(input("What is the length of side 2? "))
    s3 = float(input("What is the length of side 3? "))

    perimeter = s1 + s2 + s3

    print(f"The perimeter of the triangle is {perimeter}")

if __name__ == '__main__':
    main()

