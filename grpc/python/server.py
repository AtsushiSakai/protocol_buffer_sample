


"""


author: Atsushi Sakai

"""

from concurrent import futures
import time

import grpc


import addressbook_pb2
import addressbook_pb2_grpc


class AddressBookResponder(addressbook_pb2_grpc.RequestAddressBookServicer):

    def Request(self, request, context):
        print(request)
        print(context)

        address_book = addressbook_pb2.AddressBook()

        person1 = address_book.people.add()
        person1.id = 1234
        person1.name = "John Doe"
        person1.email = "jdoe@example.com"

        phone = person1.phones.add()
        phone.number = "555-4321"
        phone.type = addressbook_pb2.Person.HOME

        person2 = address_book.people.add()
        person2.id = 4321
        person2.name = "Tom Ranger"
        person2.email = "tranger@example.com"
        phone = person2.phones.add()
        phone.number = "555-4322"
        phone.type = addressbook_pb2.Person.WORK

        print(address_book)  # Human readable print

        return address_book


def main():
    print("start!!")

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    addressbook_pb2_grpc.add_RequestAddressBookServicer_to_server(
        AddressBookResponder(),
        server)
    server.add_insecure_port('[::]:50051')
    server.start()

    _ONE_DAY_IN_SECONDS = 60 * 60 * 24
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

    print("done!!")


if __name__ == '__main__':
    main()

