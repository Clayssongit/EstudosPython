from decorator import my_decoretor, uppercase_decorator,slip_string

# exemplo 1
@my_decoretor
def my_funcion():
    print("Dentro da função")

my_funcion()

# exemplo 2
@uppercase_decorator
def text ():
    return "Hello World"

print(text ())

# exemplo 3
@slip_string
@uppercase_decorator
def example():
    return "Aprendendo e criando decorator"

print(example())