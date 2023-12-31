"""
Dependency Inversion Principle

Dependências devem ser feitas sobre abstrações, não sobre implementações concretas 

"""


'''class Player:
    def __init__(self, name):
        self.stats = StatsReporter(self)
        self.__name = name
        self.__hp = 100
        self.__speed = 1

    def hp(self):
        return self.__hp

    def name(self):
        return self.__name

class StatsReporter:
    def __init__(self, char: Player):
        self.char = char

    def report(self):
        print(f'Name:{self.char.name()}')
        print(f'HP:{self.char.hp()}')
        '''

##### SOLUÇÃO: agora podemos criar novas implementações de relatórios 

from abc import ABC, abstractmethod

class Reporter(ABC):
    @abstractmethod
    def report(self):
        pass

class StatsReporter(Reporter):
    def __init__(self, char):
        self.char = char

    def report(self):
        print(f'Name: {self.char.name()}')
        print(f'HP: {self.char.hp()}')

class Player:
    def __init__(self, name, stats: Reporter):
        self.stats = stats
        self.__name = name
        self.__hp = 100
        self.__speed = 1

    def hp(self):
        return self.__hp

    def name(self):
        return self.__name

