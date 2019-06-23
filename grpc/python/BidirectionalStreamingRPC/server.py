"""

gRPC server for bidirectional streaming PRC sample in Python


author: Atsushi Sakai(@Atsushi_twi)

"""

import time
from concurrent import futures

import grpc

import addressbook_pb2
import addressbook_pb2_grpc


class AddressBookResponder(addressbook_pb2_grpc.RequestAddressBookWithBidirectionalStreamingRPCServicer):

    def Request(self, request, context):
        for r in request:
            print(r)

        address_book = addressbook_pb2.AddressBook()

        person1 = address_book.people.add()
        person1.id = 1234
        person1.name = "John Doe"
        person1.email = "jdoe@example.com"

        phone = person1.phones.add()
        phone.number = "555-4321"
        phone.type = addressbook_pb2.Person.HOME

        print(address_book)  # Human readable print

        yield address_book  # send first message

        time.sleep(5)  # wait 5 sec

        address_book = addressbook_pb2.AddressBook()

        person2 = address_book.people.add()
        person2.id = 4321
        person2.name = "Tom Ranger"
        person2.email = "tranger@example.com"
        phone = person2.phones.add()
        phone.number = "555-4322"
        phone.type = addressbook_pb2.Person.WORK

        print(address_book)  # Human readable print

        yield address_book  # send second message


def main():
    print("start!!")

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    addressbook_pb2_grpc.add_RequestAddressBookWithBidirectionalStreamingRPCServicer_to_server(
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
