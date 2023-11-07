from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_noise(self) -> None:
        ...
    
    @abstractmethod
    def move(self) -> None:
        ...


class Dog(Animal):
    def make_noise(self) -> None:
        print('Au Au')
    
    def move(self) -> None:
        print('Dog está se movendo...')

dog = Dog()
dog.make_noise()
dog.move()