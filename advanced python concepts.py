def login_required(func):

    def wrapper():
        print("Checking Login...")
        func()

    return wrapper


@login_required
def dashboard():
    print("Welcome to Dashboard")


dashboard()
squares = [x**2 for x in range(1, 6)]

print(squares)
students = {x: x**2 for x in range(1, 6)}

print(students)
numbers = {x for x in [1, 2, 2, 3, 4, 4, 5]}

print(numbers)
numbers = [1, 2, 3, 4, 5]

double = list(map(lambda x: x * 2, numbers))

print(double)
numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)
names = ["Ayyan", "Ali", "Ahmed"]

marks = [90, 85, 95]

students = list(zip(names, marks))

print(students)
multiply = lambda a, b: a * b

print(multiply(10, 5))