class Person:

    def __init__(self, name, add, tele):
        self.__name = name
        self.__address = add
        self.__telephone = tele

    def print_person(self):
        print('Name:', self.__name)
        self.__address
        self.__telephone


class Customer(Person):

    def __init__(self, name, add, tele, cust, on_list):
        Person.__init__(self)
        self.__customer_number = cust
        self.__on_list = on_list

    def print_person(self):
        Person.print_person(self)
        print('Customer Number: ', self.__customer_number)
        if self.__on_list:
            print('Yes')
        else:
            print('No')
