class Phone:
    def __init__(self, brand, model_name, price):
        self._brand = brand
        self._model_name = model_name
        self._price = price

    def __str__(self):
        return (f"{self._brand} {self._model_name}")
    
    @staticmethod
    def make_a_call(phone_num):
        print(f"Ligando para {phone_num}")

class SmartPhone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, back_cam):
        super().__init__(brand, model_name, price)
        
        self.ram = ram
        self.internal_memory = internal_memory
        self.back_cam = back_cam

Moto = Phone('Moto', 'G7', 1200)
print(Moto)
Moto.make_a_call('123128412')
print(f"Valor do {Moto._brand} {Moto._model_name} é R${Moto._price}.\n")

Iphone = SmartPhone("Iphone", "15", 8000, "16GB", "1TB", "60mp")
print(Iphone)
Iphone.make_a_call("123141231")
print(f"Valor do {Iphone._brand} {Iphone._model_name} é R${Iphone._price}.")
print(vars(Iphone))
