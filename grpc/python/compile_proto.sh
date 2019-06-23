#!/bin/bash
echo "$(basename $0) start!"
python -m grpc_tools.protoc -I. --python_out=UnaryRPC --grpc_python_out=UnaryRPC ./addressbook.proto
python -m grpc_tools.protoc -I. --python_out=ClientStreamingRPC --grpc_python_out=ClientStreamingRPC ./addressbook.proto
python -m grpc_tools.protoc -I. --python_out=ServerStreamingRPC --grpc_python_out=ServerStreamingRPC ./addressbook.proto
python -m grpc_tools.protoc -I. --python_out=BidirectionalStreamingRPC --grpc_python_out=BidirectionalStreamingRPC ./addressbook.proto
echo "$(basename $0) done!"
exit 0

