# import the dataclass module for use in the program

from dataclasses import dataclass


# create a class for person for variables that are universal for both child classes
@dataclass
class Person:
    f_name: str
    l_name: str
    email: str

    # create a fullName property to create a string representation for f_name and l_name
    def fullName(self):
        return f"{self.f_name} {self.l_name}"


# create a child class for Customer for info specific to Customer
@dataclass
class Customer(Person):
    num: str

    # create a property that will take and return a string representation of the input
    def get_num(self) -> str:
        return self.num


# create a child class for Employee for info specific to the Employee class
@dataclass
class Employee(Person):
    ssn: str

    # create a property that will take and return a string representation of the input
    def get_ssn(self) -> str:
        return self.ssn
