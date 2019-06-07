/**
 * Protocol buffer data writer in cpp
 *
 * @author Atsushi Sakai
 **/
#include <fstream>
#include <iostream>
#include <string>

#include "addressbook.pb.h"

using namespace std;

int main(void) {
  cout << "Start Protocol buffers writer sample" << endl;
  tutorial::AddressBook address_book;

  tutorial::Person *person1 = address_book.add_people();
  person1->set_id(1234);
  person1->set_name("John Doe");
  person1->set_email("jdoe@example.com");

  tutorial::Person::PhoneNumber *phone = person1->add_phones();
  phone->set_number("555-4321");
  phone->set_type(tutorial::Person::HOME);

  tutorial::Person *person2 = address_book.add_people();
  person2->set_id(4321);
  person2->set_name("Tom Ranger");
  person2->set_email("tranger@example.com");

  tutorial::Person::PhoneNumber *phone2 = person2->add_phones();
  phone2->set_number("555-4322");
  phone2->set_type(tutorial::Person::WORK);

  // Human readable print
  cout << address_book.DebugString() << endl;

  ofstream stream("pbdata_cpp.dat");
  if (!stream.bad()) {
    address_book.SerializeToOstream(&stream);
    stream.close();
  }

  cout << "Done" << endl;
}
