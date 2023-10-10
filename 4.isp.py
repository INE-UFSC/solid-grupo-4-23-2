'''"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão
"""
from abc import ABC

class IJanela(ABC):
    def maximizar(self):
        raise NotImplementedError
    
    def minimizar(self):
        raise NotImplementedError
    
    def mostrar_menu(self):
        raise NotImplementedError
        
    def fechar(self):
        raise NotImplementedError

class JanelaTamanhoFixo(IJanela):
    def maximizar(self):
        pass

    def minimizar(self):
        pass
    
    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass

class JanelaSemMenu(IJanela):
    def maximizar(self):
        pass

    def minimizar(self):
        pass
    
    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass
'''

from abc import ABC, abstractmethod

class IMaximizavel(ABC):
    @abstractmethod
    def maximizar(self):
        pass

class IMinimizavel(ABC):
    @abstractmethod
    def minimizar(self):
        pass

class IMenuVisivel(ABC):
    @abstractmethod
    def mostrar_menu(self):
        pass

class IFechavel(ABC):
    @abstractmethod
    def fechar(self):
        pass
