""" 

Protocol buffer reader in Python

author: Atsushi Sakai

"""

import addressbook_pb2


def main():
    print("start!!")

    address_book = addressbook_pb2.AddressBook()

    # Read the existing address book.
    f = open("pbdata.dat", "rb")
    address_book.ParseFromString(f.read())
    f.close()

    print(address_book)

    print("done!!")


if __name__ == '__main__':
    main()
