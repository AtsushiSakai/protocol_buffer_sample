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

  cout << "Done" << endl;
}
