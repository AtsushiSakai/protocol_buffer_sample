


"""
Protocol buffer reader in Python

author: Atsushi Sakai
"""

import addressbook_pb2


def main():
    """
    main func
    """
    print("start!!")

    address_book = addressbook_pb2.AddressBook()

    # Read the existing address book.
    file_path = open("pbdata_py.dat", "rb")  # read
    # file_path = open("../../sample1/python/pbdata_py.dat",
    # "rb")  # read old data

    address_book.ParseFromString(file_path.read())
    file_path.close()

    print(address_book)

    print("done!!")


if __name__ == '__main__':
    main()

