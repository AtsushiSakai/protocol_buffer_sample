"
    Protocol buffer data reader in Julia 

    author: Atsushi Sakai
"

using ProtoBuf

include("tutorial.jl")
include("addressbook_pb.jl")

function main()
    println(PROGRAM_FILE," start!!")

    stream = UInt8[]
    open( "pddata_julia.dat", "r" ) do fp
        stream = read( fp )
    end
    iob = PipeBuffer(stream)
    address_book = readproto(iob, AddressBook())

    println(address_book)  # Human readable print

    println(PROGRAM_FILE," Done!!")
end


main()



