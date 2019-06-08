


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
    # file_path = open("pbdata_py.dat", "rb")  # read data from python code
    # file_path = open("../cpp/pbdata_cpp.dat", "rb")  # read data from cpp code
    file_path = open("../julia/pbdata_julia.dat",
                     "rb")  # read data from cpp code

    address_book.ParseFromString(file_path.read())
    file_path.close()

    print(address_book)

    print("done!!")


if __name__ == '__main__':
    main()

