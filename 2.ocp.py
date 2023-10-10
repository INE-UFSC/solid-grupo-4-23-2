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
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass
    
    @abstractmethod
    def make_sound(self):
        print('algum barulho')

class Lion(Animal):
    def __init__(self) -> None:
        pass

    def get_name(self):
        pass

    def make_sound(self):
        print('roar')


class Mouse(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def get_name(self) -> str:
        return super().get_name()
    
    def make_sound(self):
        print('squeak')