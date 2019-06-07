#!/bin/sh
# get file path
echo "compiling..."
cwd=`dirname "${0}"`
expr "${0}" : "/.*" > /dev/null || cwd=`(cd "${cwd}" && pwd)`

gcc ${cwd}/writer.cpp ${cwd}/addressbook.pb.cc -lprotobuf -lstdc++ -std=c++11 -o writer.out

echo "done"
