# 1. Using self 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s = Student("Shahid", 95)
s.display()


# 2. Using cls
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

Counter.increment()
Counter.increment()
Counter.display_count()


# 3. Public Variables and Methods
class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} car started!")

my_car = Car("Toyota")
print(my_car.brand)  
my_car.start() 


# 4. Class Variables and Class Methods
class Bank:
    bank_name = "State Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1 = Bank()
print(b1.bank_name) 

Bank.change_bank_name("National Bank")
b2 = Bank()
print(b2.bank_name)  
print(b1.bank_name)  


# 5. Static Variables and Static Methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
print(MathUtils.add(5, 3)) 


# 6. Constructors and Destructors
class Logger:
    def __init__(self):
        print("Logger object created!")

    def __del__(self):
        print("Logger object destroyed!")

log = Logger()
del log


# 7. Access Modifiers: Public, Private, Protected
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name              # Public
        self._salary = salary         # Protected
        self.__ssn = ssn              # Private

emp = Employee("Shahid", 50000, "123-45-6789")
print(emp.name)          # Accessible
print(emp._salary)       # Accessible but not recommended
# print(emp.__ssn)       # Not accessible, gives error
print(emp._Employee__ssn)  # Accessible with name mangling


# 8. The super() Function
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

t = Teacher("Shahid", "English")
print(t.name)
print(t.subject)


# 9. Abstract Classes and Methods
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

r = Rectangle(5, 4)
print(r.area())


# 10. Instance Methods
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

d = Dog("Tommy", "Labrador")
d.bark()


# 11. Class Methods
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

Book.increment_book_count()
Book.increment_book_count()
print("Total Books:", Book.total_books)


# 12. Static Methods
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print(TemperatureConverter.celsius_to_fahrenheit(30)) 


# 13. Composition
class Engine:
    def start(self):
        print("Engine started!")

class Car:
    def __init__(self):
        self.engine = Engine()

car = Car()
car.engine.start()  


# 14. Aggregation
class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, emp):
        self.employee = emp

emp = Employee("Shahid")
dept = Department(emp)
print(dept.employee.name)  


# 15. MRO and Diamond Inheritance
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()  
print(D.mro())  


# 16. Function Decorators
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()


# 17. Class Decorators
def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting
class Person:
    pass

p = Person()
print(p.greet()) 


# 18. Property Decorators
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

p = Product(100)
print(p.price)      # Get
p.price = 200       # Set
del p.price         # Delete


# 19. callable() and __call__
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

m = Multiplier(5)
print(callable(m))  
print(m(10))       


# 20. Creating a Custom Exception
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be >= 18")

try:
    check_age(15)
except InvalidAgeError as e:
    print(e)  


# 21. Custom Iterable Class
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current

for num in Countdown(5):
    print(num)  

