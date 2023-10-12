## fazer a extensão da classe animal (criar classe gato, cachorro e cada uma vai ter seu próprío metodo fazer som)


'''

"""
Open-Closed Principle

Classes devem estar fechadas para modificação, mas abertas para extensão
"""
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def make_sound(self):
        if self.name == 'lion':
            print('roar')
        elif self.name == 'mouse':
            print('squeak')
        else:
            print('...')

animals = [
    Animal('lion'),
    Animal('mouse')
]

def animal_sound(animals: list):
    for animal in animals:
        animal.make_sound()

animal_sound(animals)


"""
Outro exemplo:

Imagine que você tem uma loja que dá desconto de 20% aos seus clientes favoritos
usando essa classe abaixo. Quando você decide dar 40% de desconto a clientes VIP,
você decide mudar a classe da seguinte forma:
"""

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
            if self.customer == 'fav':
                return self.price * 0.2
            if self.customer == 'vip':
                return self.price * 0.4

'''


#######SOLUÇÃO 

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    def get_name(self) -> str:
        return self.name

class Lion(Animal):
    def make_sound(self):
        print('roar')

class Mouse(Animal):
    def make_sound(self):
        print('squeak')

animals = [
    Lion('Lion'),  
    Mouse('Mouse') 
]

def animal_sound(animals: list):
    for animal in animals:
        animal.make_sound()

animal_sound(animals)


####SOLUÇÃO 2

class Discount(ABC):
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    @abstractmethod
    def give_discount(self):
        pass
            

class DiscountVip(Discount):
    def __init__(self, customer, price):
        if customer == "vip":
            super().__init__(customer, price)
        else:
            raise TypeError("Esse desconto é apenas para clientes vips")

    def give_discount(self):
        return self.price * 0.4
    
class DiscountFav(Discount):
    def __init__(self, customer, price):
        if customer == "fav":
            super().__init__(customer, price)
        else:
            raise TypeError("Esse desconto é apenas para clientes fav")

    def give_discount(self):
        return self.price * 0.2