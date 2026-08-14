class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


student1 = Student("Ayyan", 17, "Python")

student1.display()
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        self.balance -= amount
        print("Withdraw:", amount)

    def show_balance(self):
        print("Current Balance:", self.balance)


account = BankAccount("Ayyan", 5000)

account.deposit(1000)

account.withdraw(500)

account.show_balance()
class Teacher:

    school = "APSACS"

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def introduce(self):
        print(f"My name is {self.name}")
        print(f"I teach {self.subject}")
        print(f"School: {Teacher.school}")


teacher = Teacher("Sir Ali", "Python")

teacher.introduce()
class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):

    def drive(self):
        print("Car is Driving")


car = Car()

car.start()

car.drive()
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog says Woof")


class Cat(Animal):

    def sound(self):
        print("Cat says Meow")


dog = Dog()

cat = Cat()

dog.sound()

cat.sound()
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount("Ayyan", 5000)

account.deposit(1000)

account.show_balance()
