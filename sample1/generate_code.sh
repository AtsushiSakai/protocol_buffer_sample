echo "Start"
protoc --cpp_out=cpp --java_out=java --python_out=python addressbook.proto
echo "Done"
