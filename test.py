import datetime


def rate_limit(max_calls, period):
    def decorator_rate_limit(func):
        calls = []  # Список для зберігання часів викликів функції

        def wrapper(*args, **kwargs):
            now = datetime.datetime.now()
            calls_within_period = [call for call in calls if now - call < datetime.timedelta(seconds=period)]

            if len(calls_within_period) >= max_calls:
                time_until_reset = (calls_within_period[0] + datetime.timedelta(seconds=period) - now).total_seconds()
                raise Exception(f"Rate limit exceeded. Try again in {time_until_reset:.2f} seconds.")

            calls.append(now)
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_rate_limit

# Використання декоратора
@rate_limit(max_calls=5, period=10)
def limited_function():
    print("Function called")

# Виклик декорованої функції
for _ in range(7):
    try:
        limited_function()
    except Exception as e:
        print(e)











class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print(f"Color: {self.color}")

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def display_dimensions(self):
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")

class Square(Rectangle):
    def __init__(self, color, side_length):
        super().__init__(color, side_length, side_length)
        self.side_length = side_length

    def display_dimensions(self):
        print(f"Side Length: {self.side_length}")
        print(f"Width: {self.side_length}")
        print(f"Height: {self.side_length}")

# Створення об'єкта класу "Square"
my_square = Square("red", 8)

# Виведення розмірів квадрата
my_square.display_dimensions()