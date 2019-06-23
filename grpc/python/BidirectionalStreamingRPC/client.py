"""

gRPC client for bidirectional streaming PRC sample in Python

author: Atsushi Sakai

"""

import grpc

import addressbook_pb2
import addressbook_pb2_grpc


def main():
    print("start!!")

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = addressbook_pb2_grpc.RequestAddressBookWithBidirectionalStreamingRPCStub(channel)
        messages = [addressbook_pb2.AddressBookRequest(person_number=2),
                    addressbook_pb2.AddressBookRequest(person_number=3)]
        responses = stub.Request(iter(messages))

        for r in responses:
            print("response: ", r)

    print("done!!")


if __name__ == '__main__':
    main()
