"""

gRPC client for client streaming PRC sample in Python

author: Atsushi Sakai

"""

import addressbook_pb2
import addressbook_pb2_grpc
import grpc


def main():
    print("start!!")

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = addressbook_pb2_grpc.RequestAddressBookWithClientStreamingRPCStub(channel)
        messages = [addressbook_pb2.AddressBookRequest(person_number=2),
                    addressbook_pb2.AddressBookRequest(person_number=3)]
        responses = stub.Request(iter(messages))

    print("done!!")


if __name__ == '__main__':
    main()
