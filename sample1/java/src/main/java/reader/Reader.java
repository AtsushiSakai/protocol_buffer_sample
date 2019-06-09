package reader;

import java.io.FileInputStream;

import tutorial.Addressbook.AddressBook;
import tutorial.Addressbook.Person;
import tutorial.Addressbook.Person.PhoneNumber;
import static tutorial.Addressbook.Person.PhoneType.*;

public class Reader {

    public static void main(String[] args) throws Exception {
        System.out.println("Protocol buffer reader start!!");

        AddressBook addressBook =
            AddressBook.parseFrom(new FileInputStream("pbdata_java.dat"));

        System.out.println(addressBook); // Human readable print

        System.out.println("Protocol buffer reader done!!");
    }

}
