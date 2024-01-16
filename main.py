# Обробіть виняток IndexError,
# коли програма намагається отримати доступ до неправильного індексу в списку.
"""list1 = ["banan", "orange", "fruits"]
try:
    print(list1[4])
except IndexError:
    print("Немає слова за таким індесом")"""

# Створіть функцію, яка приймає два числа від користувача та обробляє помилку,
# якщо введені дані не є числами.
"""def inp():
    try:
        x = int(input("x"))
    except ValueError:
        x = 3
    try:
        y = int(input("y"))
    except ValueError:
        y = 4
        return x + y
    print(x + y)


rep = inp()
print(rep)"""

# Напишіть програму, яка відкриває файл для читання та обробляє помилку
# FileNotFoundError, якщо файл не знайдено.
"""try:
    file = open("example.txt" 'r')
except FileNotFoundError:
    print("Ваш файл пустий або його не існує")"""

# Реалізуйте функцію, яка ділить два числа, але обробляє помилку
# **`ZeroDivisionError`**, якщо друге число дорівнює нулю.
"""fir = int(input("Write int"))
fir2 = int(input("Write int"))


def dill(a, b):

    try:

        x = a / b

    except ZeroDivisionError:
        x = 0
        print("на нуль не можна ділити")
    return x


print(dill(fir, fir2))"""


# Напишіть програму, яка читає вміст текстового файлу та виводить кількість слів у ньому.
"""filename = "example.txt"

f = open(filename, 'r')

print(len(f.read()))

f.close()"""

# Створіть функцію, яка приймає рядок від користувача та записує його у файл.
"""import os

filename = "example.txt"
string = input("Write some text: ")
f = open(filename, 'w')


def conk():

    f.write(string)


conk()
f.close()"""

# Реалізуйте програму, яка копіює вміст одного файлу в інший.
"""filename = "example.txt"
filename2 = "copy.txt"

f = open(filename, 'r')
f2 = open(filename2, 'w+')

file1 = f.read()
file2 = f2.write(file1)

print(file1)

print(file2)

f.close()
f2.close()"""


# Напишіть програму, яка відкриває два файли для читання та
# порівнює їх вміст, виводячи рядки, які є у першому файлі, але відсутні у другому.
"""filename = "example.txt"
filename2 = "copy.txt"

f = open(filename, 'r')
f2 = open(filename2, 'r')

file1 = set(f.read().split())
file2 = set(f2.read().split())
diference = file1 - file2

print(file1)
print(file2)
print('\n'.join(diference))

f.close()
f2.close()"""


# Створіть функцію, яка видаляє вказаний рядок з текстового файлу.


"""def dell():
    filename = "example.txt"
    f = open(filename, 'r')
    lines = f.readlines()
    
    str = "дощ"

    pattern = re.compile(re.escape(str))
    f = open(filename, 'w')
    for line in lines:
        result = pattern.search(line)
        if result is None:
            f.write(line)
        return result

dell()
"""


# Створіть клас Rectangle для представлення прямокутника.
# Додайте методи для обчислення площі та периметра прямокутника.
# Створіть об'єкт Rectangle і викличте ці методи
"""class Rectangle:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def area(self, height, weight):
        return height * weight

    def perim(self, height, weight):
        return (height * weight) * 2


cub1 = Rectangle()
print(cub1.area(2, 3))
print(cub1.perim(4,4))"""


# Розробіть клас BankAccount для представлення банківського рахунку.
# Додайте методи для зняття та поповнення коштів на рахунку.
# Використовуйте магічний метод __str__ для виведення інформації про рахунок.
"""class BankAccount:
    def __init__(self, name, surname, balance):
        self.name = name
        self.surname = surname
        self.balance = balance

    def withdraw(self, other):
        self.balance -= other
        return f'{self.balance} З вашого рахунку знято {other}'

    def depo(self, other):
        self.balance += other
        return f'{self.balance} Ваш рахунок поповнено на {other}'

    def __str__(self):
        print(f'{self.name} {self.surname} На вашому рахунку {self.balance}!')


bunk1 = BankAccount("Yong", "Milioner", 10000)
BankAccount.__str__(bunk1)
print(bunk1.withdraw(300))
print(bunk1.depo(10000))"""


# Розробіть клас Vehicle для представлення транспортного засобу.
# Додайте атрибути, такі як назва, швидкість і вартість.
# Реалізуйте метод __gt__, який порівнює два транспортних засоби за швидкістю.
# Створіть список транспортних засобів і відсортуйте його за швидкістю.
"""class Vehicle:
    def __init__(self, name, speed, price):
        self.name = name
        self.speed = speed
        self.price = price

    def __str__(self):
        return f"Машина {self.name}, швидкість {self.speed}, ціна {self.price}!"

    def __gt__(self, other):
        return self.speed > other.speed


car1 = Vehicle("Mercedes", 170, 5400)
car2 = Vehicle("Lexus", 220, 7000)
car3 = Vehicle("Bmw", 200, 6400)
car4 = Vehicle("Audi", 250, 10000)

cars = car1, car2, car3, car4

cars_garage = sorted(cars, key=lambda x: x.speed, reverse=True)

for i in cars_garage:
    print(i)


"""


# Створіть клас Student для представлення студента.
# Додайте атрибути, такі як ім'я, прізвище і список оцінок.
# Реалізуйте метод __len__, який повертає кількість оцінок студента.
# Створіть список студентів і відсортуйте його за кількістю оцінок.
"""class Student:
    def __init__(self, name, surname, rating_list):
        self.name = name
        self.surname = surname
        self.rl = rating_list

    def __str__(self):
        return f'{self.name} {self.surname} ___ rating list: {self.rl}'

    def __len__(self):
        return len(self.rl)


person1 = Student("Jox", "Sim", [5, 5, 5, 3, 8, 5, 6])
person2 = Student("Bor", "Fil", [6, 9, 9, 9, 3, 5, 4, 8, 7, 7, 8])
person3 = Student("Egor", "Diol", [8, 8, 8, 7])
person4 = Student("Naid", "Mac", [8, 6, 9, 4, 8, 7])

room = person1, person2, person3, person4

list_r = sorted(room, key=lambda x: len(x), reverse=True)

for i in list_r:
    print(len(i))"""


# Розробіть клас Library для представлення бібліотеки.
# А також класс Book для представлення книги.
# Класс Library повинен мати атрибут books зі списком книжок.
# Кожна книга в бібліотеці має атрибути, такі як назва, автор і рік видання.
# Додайте метод add_book, який додає нову книгу до бібліотеки.
# Реалізуйте метод __str__, який виводить список книг у бібліотеці.
# Створіть об'єкт Library і додайте кілька книг. Виведіть список книг у бібліотеці.
"""class Library:
    books = []

    def add_book(self, book):
        self.books.append(book)

    def __repr__(self):
        return f'{self.books}'

    def __str__(self):
        return self.__repr__()


class Book:
    def __init__(self,name, creator, date):

        self.name = name
        self.creator = creator
        self.date = date

    def __repr__(self):
        return f'Book {self.name} creator {self.creator} date {self.date}'

    def __str__(self):
        self.__str__()

lib = Library()
print(lib)
lib.add_book(Book("Фактор Черчилля", "Боріс Джонсон", 2019, ))
lib.add_book(Book("Ретрит","Сара Пірс", 2023))
print(lib)"""

# Створіть клас Circle, який представляє коло.
# Реалізуйте методи для обчислення площі та довжини кола.
# Використовуйте аттрибут класу для зберігання значення π (pi).
"""class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self,):
        return (self.radius ** 2) * self.pi

    def long_circle(self):
        return 2 * (self.pi * self.radius)


circle = Circle(5)
plosha = circle.area()
dovgina = circle.long_circle()
print(plosha)
print(dovgina)"""

# Створіть клас Student, який представляє студента.
# Реалізуйте атрибут класу для відстеження кількості студентів.
# Для цього змінюйте значення атрибуту класу у методі __init__ .
# Та створіть клас метод для виведення загальної кількості студентів.
"""class Student:
    count_students = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Student.count_students += 1

    def from_count(self):
        return Student.count_students


student1 = Student("John", "Walker")
student2 = Student("Ivan", "Creep")
student3 = Student("Nick", "Kila")
student4 = Student("Alef", "Fatcher")
student5 = Student("Stew", "Jobs")
student6 = Student("Boris", "Jonson")

clas = Student.from_count(student1)
print(clas)"""


# Створіть клас Book який має такі атрибути як рік видання,
# назву, автор та кількість сторінок.
# Створіть статік метод який буде приймати список книжок та рік,
# та повертати кількість книжок з цього списку
# які були опубліковані у цьому році.
"""class Book:
    def __init__(self, year, name, creator, pages):
        self.year = year
        self.name = name
        self.creator = creator
        self.pages = pages

    @staticmethod
    def libri(books, year):
        count = 0
        for book in books:
            if book.year == year:
                count += 1
        return count


book = [
    Book(1993, "Kriminal", "Bandera", 447),
    Book(1654, "Race", "Gamer", 143),
    Book(1768, "Live", "Human", 743),
    Book(1878, "Water", "Man", 132),
    Book(1993, "Iron Man", "Stark", 148),
    Book(1923, "Tesla", "Ilon", 843),
    Book(1993, "Geto", "Shevchenko", 1934)

]

print(Book.libri(book, 1993))"""


# Реалізувати менеджер контексту Timer, який вимірює час виконання блоку коду.
# Контекстний менеджер повинен виводити час, що минув, при виході з контексту.
# Використовуйте контекстний менеджер для вимірювання часу виконання певного фрагменту коду.
# Реалізувати контекстний менеджер потрібно 2 способами, за допомогою декоратора contextmanager та за допомогою класу.
"""from time import time


class ContextManager:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __enter__(self):
        start = time()
        print(start,  self.name)

    def __exit__(self, exc_type, exc_value, traceback):
        end = time()
        print(end, self.age)


with ContextManager("Alex", 19):
    print(ContextManager)

print(100*"*")

from contextlib import contextmanager


@contextmanager
def my_context():
    start = time()
    print(f'My name - Alex {start}')

    try:
        
        yield

    finally:
        end = time()
        print(f'My age -19 {end}')


with my_context():
    print(f'My name - Alex my age - 19')


# 1 Створіть контекстний менеджер DividerContext,
# який буде прінтити символ, який ми до нього передамо як розділитель
# для основного блоку коду до та після його виконання.
# 2 Реалізувати контекстний менеджер потрібно 2 способами,
# за допомогою декоратора contextmanager та за допомогою класу.
# (приклад можно знайти у презентації)
"""

"""class ContMan:
    def __init__(self, anyx, mnog):
        self.anyx = anyx
        self.mnog = mnog


    def __enter__(self):
        print(f'{self.anyx}' * self.mnog)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'{self.anyx}' * self.mnog)


with ContMan((input("write rozdilnyk")), 35):

    print(f'Dobri den every body')

from contextlib import contextmanager

@contextmanager
def my_context():
    rozdil = input("Write rozdil")
    print(rozdil * 35)
    try:

        yield

    finally:
        print(rozdil * 35)


with my_context():
    print(f'Dobri den every body')


# Створіть простий декоратор логування log_func, який буде прінтити
# будь яке повідомлення перед визовом декорованої функції, та після.
"""
"""def decorator(func):

    def log_func():
        print("Enter your login")
        func()
        print("Login successful")
    return log_func


@decorator
def login():
    print("login@gmail.com")


login()"""
# Реалізувати декоратор timeit, який вимірює час виконання декорованої
# функції і виводить його. Для отримання часу роботи скористуйтесь модулем
# time і функцією time.time()
"""from time import time

def decorator(func):
    def timeit():
        start = time()
        print(start)
        func()
        end = time()
        print(end - start)
    return timeit


@decorator
def timer():
    print("Times going")


timer()"""


# Створіть декоратор retry який приймає першим аргументом число -
# кількість разів, яку потрібно буде повторити виконання функції у
# разі викидання нею помилки. (приклад можно знайти у презентації)
"""def decorator_retry(max_retry):
    def retry(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retry:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Attempt {retries + 1}/{max_retry} failed: {e}")
                    retries += 1
            raise Exception(f"Function '{func.__name__}' failed after {max_retry} attempts.")
        return wrapper()
    return retry


@decorator_retry(3)
def pomilka():
    import random
    if random.random() < 0.8:
        raise ValueError("Connection error")
    print("Request successful")


pomilka()"""

# Реалізувати декоратор кешування memoize, який кешує результати
# декорованої функції для покращення продуктивності при повторних
# викликах з тими самими аргументами.
# Тобто він повинен запамʼятовувати аргументи з
# якими функція визивалась і результат роботи функції
# з цими аргументами.
# І у випадку, якщо ми вже маємо результат для цих аргументів,
# просто повернути закешований результат, замість виклику функції.
"""def memoize(func):
    cache = {}

    def memory(*args, **kwargs):
        key = args + tuple(kwargs.items())
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return memory

# Використання декоратора
@memoize
def repeat(x, y):
    print(f"Рахуємо {x},* {y}")
    return x * y


print(repeat(2, 3))
print(repeat(2, 3))
print(repeat(4, 5))
print(repeat(4, 5))"""


# Створіть декоратор **`rate_limit`**, який обмежує кількість викликів
# декорованої функції протягом певного періоду часу.
# Декоратор повинен приймати два параметри `max_calls` та `period`.
# Перший парметр - максимальна кількість допустимих викликів функції.
# Другий параметр - кількість секунд у рамках яких ми можемо зробити `max_calls` викликів.
# Вам допоможе модуль `datetime` для вирішення цієї задачі.
"""import datetime


def rate_limit(max_calls=5, period=20):
    def dec_rate_limit(func):
        calls = []

        def wrapper(*args, **kwargs):
            now = datetime.datetime.now()
            calls_period = [call for call in calls if now - call < datetime.timedelta(seconds=period)]

            if len(calls_period) >= max_calls:
                time_reset = (calls_period[0] + datetime.timedelta(seconds=period) - now).total_seconds()
                raise Exception(f"Rate limit exceeded. Try again in {time_reset:.2f} seconds.")

            calls.append(now)
            result = func(*args, **kwargs)
            return result

        return wrapper

    return dec_rate_limit


@rate_limit()
def limited_function():
    print("Function called")


for i in range(7):
    try:
        limited_function()
    except Exception as e:
        print(e)"""


# Змініть функцію even_odd_generator так, щоб вона генерувала послідовність
# чисел від 1 до n з рядками "Fizz" для чисел, які діляться на 3, "Buzz" для
# чисел, які діляться на 5, і "FizzBuzz" для чисел, які діляться як на 3, так і на 5.
"""def even_odd_generator(n):
    for num in range(1, n+1):
        result = ""
        if num % 3 == 0 and num % 5 == 0:
            result += "FizzBuzz"
        elif num % 3 == 0:
            result += "Fizz"
        elif num % 5 == 0:
            result += "Buzz"
        yield result if result else num


for el in even_odd_generator(15):
    print(el)"""


# Напишіть генератор, який повертає послідовність чисел Фібоначчі.
"""def fibonacci_generator(n):
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a +b


fib_gen = fibonacci_generator(10)
for i in range(10):
    print(next(fib_gen))"""


# Створіть ітератор який буде приймати рядок та кожен виклик методу next() буде
# повертати наступний символ рядку.
"""class String:
    def __init__(self, input_string):
        self.input_string = input_string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.input_string):
            result = self.input_string[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


string = "Hello, World!"
str_iter = String(string)
for char in str_iter:
    print(char)"""

# Напишіть генератор, який видає послідовність квадратів чисел від 1 до N
"""def square_generator(n):
    for num in range(1, n+1):
        yield num ** 2


for square in square_generator(5):
    print(square)"""


# Реалізуйте ітератор для перебору всіх ключів словника.
"""class DictKeysIterator:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = list(dictionary.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.keys):
            key = self.keys[self.index]
            self.index += 1
            return key
        else:
            raise StopIteration


dictionary = {"a": 1, "b": 2, "c": 3}
dict_iter = DictKeysIterator(dictionary)
for key in dict_iter:
    print(key)"""


# Напишіть генератор, який фільтрує непарні числа з заданої послідовності.
"""def even_number_filter(sequence):
    for num in sequence:
        if num % 2 == 0:
            yield num


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = even_number_filter(numbers)
for num in even_nums:
    print(num)"""

# Створіть ітератор,
# який перебирає всі парні числа з заданого діапазону.
"""class NumbFilter:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start if start % 2 == 0 else start + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            result = self.current
            self.current += 2
            return result
        else:
            raise StopIteration()


even_nums = NumbFilter(2, 10)
for nums in even_nums:
    print(nums)"""

# Напишіть генератор, який видає послідовність простих чисел.
"""def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0:
        return False
    n = 3
    while n * n <= number:
        if number % n == 0:
            return False
        n += 2
    return True


def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


prime_gen = prime_generator()
for i in range(10):
    print(next(prime_gen))"""


# Створіть ітератор, який перебирає всі паліндроми (слова, які читаються
# однаково зліва направо та зправа наліво) з заданого списку слів.
"""class PalindromeIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.words):
            word = self.words[self.index]
            self.index += 1
            if word == word[::-1]:
                return word
        raise StopIteration


words_list = ['level', 'racecar', 'python', 'madam']
palindrome_iter = PalindromeIterator(words_list)
for word in palindrome_iter:
    print(word)"""


# Напишіть клас "Person", який має властивості name (ім'я) і age (вік).
# Зробіть ці властивості приватними, щоб вони не могли бути змінені напряму ззовні класу.
# Забезпечте методи для доступу до цих властивостей та встановлення їх значень.
"""class Person:
    def __init__(self):
        self.__name = "Alex"
        self.__age = 22

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


person = Person()
person.set_name("John")
person.set_age(25)
print(person.get_name())
print(person.get_age()) """


# Розширте клас "Person" з попереднього завдання, додавши методи для зміни
# значень імені та віку. Зробіть так, щоб ім'я не могло містити цифр, а вік був
# обмежений в діапазоні від 0 до 120. При спробі встановити недійсне значення,
# виведіть повідомлення про помилку.
"""class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if self.__name != name.isalpha():
            print("Потрібно писати тільки букви")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age <= 0 or age >= 120:
            print("Не можливий вік")
        else:
            self.__age = age


person = Person("alex", 23)
person.set_name("John1313")
person.set_age(-25)
print(person.get_name())
print(person.get_age())"""


# Розробіть клас "Car", який містить такі властивості: make (марка автомобіля), model
# (модель автомобіля), year (рік випуску автомобіля) і mileage (пробіг автомобіля).
# Забезпечте можливість доступу до цих властивостей через методи, а також зробіть
# властивості "make" і "model" приватними.
# Додайте метод "drive" до класу "Car", який збільшує пробіг автомобіля на задане
# значення. Перевірте, чи не перевищує пробіг заданий ліміт (наприклад, 300 000
# км), і виведіть повідомлення про досягнення ліміту при спробі здійснити поїздку.
"""class Car:
    def __init__(self, make, model, year, mileage):
        self.__make = make
        self.__model = model
        self.year = year
        self.mileage = mileage

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.year

    def get_mileage(self):
        return self.mileage

    def drive(self, distance):
        if self.mileage + distance <= 300000:
            self.mileage += distance
        else:
            print("Limit mileage")


car = Car("Toyota", "Camry", 2020, 5000)
print(car.get_make()) # Виведе "Toyota"
print(car.get_model()) # Виведе "Camry"
print(car.get_year()) # Виведе 2020
print(car.get_mileage()) # Виведе 5000

car.drive(100) # Збільшення пробігу на 100
print(car.get_mileage()) # Виведе 5100

car.drive(300000) # Виведе повідомлення про досягнення ліміту"""


# Створіть базовий клас "Shape" (фігура), який має властивість color (колір) і метод
# display_color() для виведення коліру фігури. Створіть похідний клас "Rectangle"
# (прямокутник), який наслідує властивість color і додає властивості width (ширина) і
# height (висота). Забезпечте можливість встановлення значень ширини і висоти
# прямокутника та виведення їх значень.
"""class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print(f'Color: {self.color}')


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height


shape = Shape("Red")
shape.display_color()  # Виведе "Color: Red"

rectangle = Rectangle("Blue", 10, 5)
rectangle.display_color()  # Виведе "Color: Blue"
print(rectangle.width)  # Виведе 10
print(rectangle.height)  # Виведе 5"""


# Розширте клас "Rectangle" з попереднього завдання, перевизначивши метод
# display_color(). В методі display_color() виведіть повідомлення про колір
# прямокутника і додайте також виведення повідомлення про його розміри (ширину і
# висоту).
"""class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print(f'Color: {self.color}')


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def display_color(self):
        super().display_color()
        print(f'Width {self.width}')
        print(f'Height {self.height}')


rectangle = Rectangle("Blue", 10, 5)
rectangle.display_color() # Виведе "Color: Blue, Width: 10, Height: 5"""


# Багаторівневе наслідування
"""class Animal:
    def __init__(self, animal, species):
        self.animal = animal
        self.species = species


class Mammal(Animal):
    def __init__(self, animal, species, diet_type):
        super().__init__(animal, species)
        self.diet_type = diet_type

    def display_info(self):
        print(
            f'Animal: {self.animal} \n'
            f'Species: {self.species} \n'
            f'Diet type: {self.diet_type} \n'
        )


class Carnivore(Mammal):
    def __init__(self, animal, species, diet_type, teeth):
        super().__init__(animal, species, diet_type,)
        self.teeth = teeth

    def display_info(self):
        super().display_info()
        print(f'Teeth Count: {self.teeth}')


class Lion(Carnivore):
    def __init__(self, animal, species, diet_type, teeth, mane):
        super().__init__(animal, species, diet_type, teeth,)
        self.mane = mane

    def display_info(self):
        super().display_info()
        print(f'Mane size: {self.mane}')


lion = Lion("Simba", "Lion", "Carnivore", 30, "Large")
carnivore = Carnivore("Tiger", "Carnivore", "Carnivore", 40)
mammal = Mammal("Elephant", "Mammal", "Herbivore")

lion.display_info()
print("---------------------")
carnivore.display_info()
print("**********************")
mammal.display_info()"""


# Розробіть клас "Square", який успадковує властивості і методи з класу "Rectangle".
# Додайте властивість side_length (довжина сторони) і перевизначте методи, які
# використовують властивості width і height класу "Rectangle", щоб вони
# використовували властивість side_length класу "Square". Виведіть значення
# ширини, висоти і довжини сторони для об'єкта класу "Square".
"""class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print(f'Color: {self.color}')


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def side_length(self):
        print(f'Height: {self.height}')
        print(f'Width: {self.width}')


class Square(Rectangle):

    def __init__(self, color, length):
        super().__init__(color, length, length)
        self.length = length

    def side_length(self):
        print(f'Side length: {self.length}')
        print(f'Width: {self.length}')
        print(f'Height: {self.length}')


square = Square("Green", 8)
square.display_color()
square.side_length()"""


# Ви розробляєте програму для автосалону, яка обробляє інформацію про
# різні автомобілі. У вас є базовий абстрактний клас Car (автомобіль), який містить
# загальну інформацію про автомобіль, таку як марка та модель. У додаткових
# класах, які успадковують від Car , ви розширюєте функціональність для конкретних
# типів автомобілів
"""class Car:
    def __init__(self, car, model):
        self.car = car
        self.model = model

    def display_info(self):
        print(f'Car: {self.car}, {self.model}')


class Sedan(Car):
    def __init__(self, car, model, doors):
        super().__init__(car, model)
        self.doors = doors

    def display_info(self):
        super().display_info()
        print(f'Doors: {self.doors}')


class SUV(Car):
    def __init__(self, car, model, seats):
        super().__init__(car, model)
        self.seats = seats

    def display_info(self):
        super().display_info()
        print(f'Seats: {self.seats}')


class SportsCar(Car):
    def __init__(self, car, model, max_speed):
        super().__init__(car, model)
        self.max_speed = max_speed

    def display_info(self):
        super().display_info()
        print(f'Max Speed: {self.max_speed}')


sedan = Sedan("Toyota", "Corolla", 4)
suv = SUV("Ford", "Explorer", 7)
sport = SportsCar("Ferrari", "488 GTB", 330)

sedan.display_info()
print("************************")
suv.display_info()
print("************************")
sport.display_info()"""



# Напишіть функцію, яка отримує URL API та повертає відповідь
# з нього в форматі JSON. Виведіть цю відповідь на екран.

"""import requests


def get_weather(api_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?q={city}&key={api_key}"
    response = requests.get(url)
    data = response.json()

    if 'error' in data:
        print('Помилка: Неможливо отримати погодні дані')
        return

    temperature = data['current']['temp_c']

    print(f'Температура: {temperature}°C')


api_key = "d0147e7e25444a1a9d4124438230710"
city = input()

get_weather(api_key, city)
"""

# Використовуючи API курсів валют, розробіть програму, яка запитує
# у користувача вихідну валюту, потрібну валюту та суму,
# і обчислює конвертацію з однієї валюти в іншу.
# Виведіть отриманий результат на екран.

"""import requests
name = input()
summa = int(input())

def money(api_key, currency):
    url = ""
    responce = requests.get(url)
    data = responce.json()

    try:
        cash = data['']['']
        print(f"Вхідна валюта {name} сума {summa} конвертовано в {cash} ")
    except:
"""


name = str(input("Write your name!"))
print(f'Радий тебе бачити, {name}!')

age = int(input("Write your age!"))

if age < 18:
    print("Неповнолітній!")
else:
    print("Повнолітній!")


























