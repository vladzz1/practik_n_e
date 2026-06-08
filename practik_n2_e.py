def my_decorator(func):
    def private_decorator():
        print("-----My decorator-----")
        func()
        print("-----End decoratory-----")
    return private_decorator

@my_decorator
def hello_message():
    print("Привіт козаки! Хочу в Африку :)")

hello_message()

def my_view_message(msg):
    message = msg[0:9]
    # print("message", message)
    def private_func():
        print(message)
    return private_func

closure = my_view_message("Привіт козаки і козачки. Класна погода")
closure()

def get_numbers():
    return [1, 2, 3]

print("default numbers", get_numbers())

def get_yield_numbers():
    yield 1
    yield 2
    yield 3

print("---get_yield_numbers---")
for item in get_yield_numbers():
    print(item, end="\t")

def my_counter_yield(n):
    i = 0
    while i <= n:
        yield i
        i += 2

print()
for item in my_counter_yield(7):
    print(item, end="\t")