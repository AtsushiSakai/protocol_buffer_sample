package reader;

import java.io.FileInputStream;

import tutorial.Addressbook.AddressBook;

public class Reader {

    public static void main(String[] args) throws Exception {
        System.out.println("Protocol buffer reader start!!");

        AddressBook addressBook =
            AddressBook.parseFrom(new FileInputStream("pbdata_java.dat"));

        System.out.println(addressBook); // Human readable print

        System.out.println("Protocol buffer reader done!!");
    }

}
