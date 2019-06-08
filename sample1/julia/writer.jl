"
    Protocol buffer data writer in Julia 

    author: Atsushi Sakai
"

using ProtoBuf

include("tutorial.jl")
include("addressbook_pb.jl")

function main()
    println(PROGRAM_FILE," start!!")

    address_book = AddressBook(
                               people=Person[]
                              )

    person1 = Person(
                     id = 1234,
                     name = "John Doe",
                     email = "jdoe@example.com",
                     phones = Person_PhoneNumber[]
                    )

    phone = Person_PhoneNumber(
                               number="555-4321",
                               _type = __enum_Person_PhoneType().HOME
                              )
    push!(person1.phones, phone)

    push!(address_book.people, person1)
 
    
    person2 = Person(
                     id = 4321,
                     name = "Tom Ranger",
                     email = "tranger@example.com",
                     phones = Person_PhoneNumber[]
                    )

    phone = Person_PhoneNumber(
                               number="555-4322",
                               _type = __enum_Person_PhoneType().WORK
                              )
    push!(person2.phones, phone)

    push!(address_book.people, person2)
 

    println(address_book)  # Human readable print

    iob = PipeBuffer();
    writeproto(iob, address_book)

    open( "pddata_julia.dat", "w" ) do fp
        write( fp, iob )
    end

    println(PROGRAM_FILE," Done!!")
end


main()

