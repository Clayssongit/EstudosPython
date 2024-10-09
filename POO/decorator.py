def my_decoretor(func):
    def wrapper():
        print("Antes de executar a função")
        func()
        print("Depois de executar a função")
    return wrapper

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def slip_string(function):
    def wrapper():
        func = function()
        sliptted_string = func.split()
        return sliptted_string
    return wrapper
