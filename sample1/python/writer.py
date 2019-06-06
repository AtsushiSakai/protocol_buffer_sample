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
    phone = person1.phones.add()
    phone.number = "555-4321"
    phone.type = addressbook_pb2.Person.HOME

    # person1.no_such_field = 1  # raises AttributeError
    # person1.id = "1234"        # raises TypeError

    person2 = address_book.people.add()
    person2.id = 4321
    person2.name = "Tom Ranger"
    person2.email = "tranger@example.com"
    phone = person2.phones.add()
    phone.number = "555-4322"
    phone.type = addressbook_pb2.Person.WORK

    print(address_book)  # Human readerble print

    # writing the data
    f = open("pbdata.dat", "wb")
    f.write(address_book.SerializeToString())
    f.close()

    print("done!!")


if __name__ == '__main__':
    main()
