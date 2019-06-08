echo "Start"
# for cpp, java, python
protoc --cpp_out=cpp --java_out=java --python_out=python addressbook.proto
# for julia
julia -e "using ProtoBuf;run(ProtoBuf.protoc(\`--julia_out=julia addressbook.proto\`))"
echo "Done"
