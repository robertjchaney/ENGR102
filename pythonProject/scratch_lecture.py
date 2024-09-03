from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def debug(self):
        pass

class Employee(User):
    def __init__(self):
        print("New Employee Added")