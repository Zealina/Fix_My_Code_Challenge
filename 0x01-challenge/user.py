#!/usr/bin/python3
""" 
User class
"""

class User():
    """ Class User for OOP Project """

    def __init__(self):
        """ Instantiation of Class """
        self.__email = None

    @property
    def email(self):
        """ Email Getter """
        return self.__email

    @email.setter
    def email(self, value):
        """ Email Setter """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value
    
if __name__ == "__main__":
    """ Create instances of the class"""
    u = User()
    u.email = "john@snow.com"
    print(u.email)
