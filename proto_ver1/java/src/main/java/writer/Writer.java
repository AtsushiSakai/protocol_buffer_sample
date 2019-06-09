package writer;

import java.io.FileOutputStream;

import tutorial.Addressbook.AddressBook;
import tutorial.Addressbook.Person;
import tutorial.Addressbook.Person.PhoneNumber;
import static tutorial.Addressbook.Person.PhoneType.*;

public class Writer {

    public static void main(String[] args) throws Exception {
        System.out.println("Protocol buffer writer start!!");

        AddressBook.Builder addressBook = AddressBook.newBuilder();

        Person.Builder person1 = Person.newBuilder();
        person1.setId(1234);
        person1.setName("John Doe");
        person1.setEmail("jdoe@example.com");

        PhoneNumber.Builder phone = PhoneNumber.newBuilder()
                                    .setNumber("555-4321")
                                    .setType(HOME);
        person1.addPhones(phone.build());

        Person.Builder person2 = Person.newBuilder();
        person2.setId(4321);
        person2.setName("Tom Ranger");
        person2.setEmail("tranger@example.com");

        PhoneNumber.Builder phone2 = PhoneNumber.newBuilder()
                                    .setNumber("555-4322")
                                    .setType(WORK);
        person2.addPhones(phone2.build());

        addressBook.addPeople(person1.build());
        addressBook.addPeople(person2.build());


        System.out.println(addressBook); // Human readable print

        FileOutputStream output = new FileOutputStream("pbdata_java.dat");
        addressBook.build().writeTo(output);
        output.close();

        System.out.println("Protocol buffer writer done!!");
        

    }

}
