import g_person as p


def main():
    name = 'John'
    add = 'Baylor'
    tele = '281-9089629'
    cust = 1234
    on_list = False

    john_person = p.Person(name, add, tele)

    john_customer = p.Customer(name, add, tele, cust, on_list)

    john_person.print_person()


main()
