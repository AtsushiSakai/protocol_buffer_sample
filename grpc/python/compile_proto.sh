#!/bin/bash
echo "$(basename $0) start!"
python -m grpc_tools.protoc -I.. --python_out=. --grpc_python_out=. ../addressbook.proto
echo "$(basename $0) done!"
exit 0

