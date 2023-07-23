#include "Library.h"
#include "Book.h"

#include <iostream>

using namespace std;

void Library::addBook(Book *newBook) {
	listBook.push_back(newBook);
	
}

void Library::showBooks() const {
	for (const Book *element : this->listBook) {
		cout << *element << endl;
	}
}