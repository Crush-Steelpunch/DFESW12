from abc import ABC, abstractmethod

class GenericWebLogin(ABC):

    def __init__(self,username,password):
        self.username = username
        self.password = password
    
    @abstractmethod
    def login(self,websiteurl):
        pass



class LoginToAll4Website(GenericWebLogin):

    def login(self,websiteurl):
        