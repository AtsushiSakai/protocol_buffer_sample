


"""

Protocol buffer writer in Python

author: Atsushi Sakai

"""

import addressbook_pb2


def main():
    print("start!!")

    address_book = addressbook_pb2.AddressBook()

    person1 = address_book.people.add()
    person1.id = 1234
    person1.name = "John Doe"
    person1.email = "jdoe@example.com"
    person1.weight = 70.0
    # person1.no_such_field = 1  # raises AttributeError
    # person1.id = "1234"        # raises TypeError

    phone = person1.phones.add()
    phone.number = "555-4321"
    phone.type = addressbook_pb2.Person.HOME

    person2 = address_book.people.add()
    person2.id = 4321
    person2.name = "Tom Ranger"
    person2.email = "tranger@example.com"
    person2.weight = 50.0
    phone = person2.phones.add()
    phone.number = "555-4322"
    phone.type = addressbook_pb2.Person.CAR

    print(address_book)  # Human readable print

    # writing the data
    f = open("pbdata_py.dat", "wb")
    f.write(address_book.SerializeToString())
    f.close()

    print("done!!")


if __name__ == '__main__':
    main()

