"""

gRPC server for unary PRC sample in Python

author: Atsushi Sakai

"""

import grpc

import addressbook_pb2
import addressbook_pb2_grpc


def main():
    print("start!!")

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = addressbook_pb2_grpc.RequestAddressBookWithUnaryRPCStub(channel)
        response = stub.Request(
            addressbook_pb2.AddressBookRequest(person_number=2))
        print("response: ", response)

    print("done!!")


if __name__ == '__main__':
    main()
