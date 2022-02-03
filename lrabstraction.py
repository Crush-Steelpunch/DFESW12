from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def eat(self):
        pass

class Sheep(Animal):

    def __init__(self):
        self.sound = "baa"

    def eat(self):
        print("I like grass. Nom")


shaun = Sheep()

