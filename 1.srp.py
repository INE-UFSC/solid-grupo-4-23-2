"""
Single Responsibility Principle

Uma classe deve ter somente uma responsabilidade
ou
Uma classe deve ter somente um motivo para mudar
"""

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass


## a classe animal não deve ter o método save. Uma classe deve ser criada para isso

class Save:
    def __init__(self) -> None:
        pass

    def save(self):
        pass