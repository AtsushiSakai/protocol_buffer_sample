


"""

Protocol buffer reader in Python

author: Atsushi Sakai

"""

import addressbook_pb2


def main():
    print("start!!")

    address_book = addressbook_pb2.AddressBook()

    # Read the existing address book.
    f = open("pbdata_py.dat", "rb")  # read data from python code
    # f = open("../cpp/pbdata_cpp.dat", "rb")  # read data from cpp code

    address_book.ParseFromString(f.read())
    f.close()

    print(address_book)

    print("done!!")


if __name__ == '__main__':
    main()

