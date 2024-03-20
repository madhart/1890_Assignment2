# import the classes for use in the program

from Question_1_classes import Customer, Employee


# title, enough said
def title():
    print("Customer/Employee Data Entry\n")


# create an employee function that takes user inputs and makes an object for them and returns it
def employee():
    print("DATA ENTRY")
    first = input("First name: ")
    last = input("Last name: ")
    email = input("Email: ")
    num = input("SSN: ")
    return Employee(f_name=first, l_name=last, email=email, ssn=num)


# create a customer function that takes user inputs and returns an object for them
def custom():
    print("DATA ENTRY")
    first = input("First name: ")
    last = input("Last name: ")
    email = input("Email: ")
    num = input("Number: ")
    return Customer(f_name=first, l_name=last, email=email, num=num)


# make a function that will use the isinstance to test weather it is a customer or employee and return the proper
# information
def show_person(human):
    w = 10
    if isinstance(human, Employee):
        print(f"{'Name':{w}} {human.fullName()}")
        print(f"{'Email':{w}} {human.email}")
        print(f"{'SSN':{w}} {human.ssn}")
        print()
    elif isinstance(human, Customer):
        print(f"{'Name':{w}} {human.fullName()}")
        print(f"{'Email':{w}} {human.email}")
        print(f"{'Number':{w}} {human.num}")
        print()
    print()


# make a main to take an input to access customer or the employee, then uses the respective function
# and assign's it to the variable human to be returned to the show_person function
def main():
    title()

    cont = "y"
    while cont == "y":
        user = input("Customer or Employee? (c/e): ")
        print()
        if user == "c":
            human = custom()
            print()
            print("CUSTOMER")
            show_person(human)
            cont = input("Continue?: ")
        elif user == "e":
            human = employee()
            print()
            print("EMPLOYEE")
            show_person(human)
            cont = input("Continue?: ")
        else:
            print("invalid, try again")

    print("Bye!")


if __name__ == "__main__":
    main()
