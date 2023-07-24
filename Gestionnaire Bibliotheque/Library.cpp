#include "Library.h"
#include "Book.h"

#include <iostream>
#include <string>

using namespace std;

int Library::getBooksize() const {
    return listBook.size();
}

void Library::addBook(Book *newBook) {
	listBook.push_back(newBook);
	
}

void Library::showBooks() const {
	for (const Book *element : this->listBook) {
		cout << *element << endl;
	}
}

int Library::removeBook(const string& name) {
    int countRemovedBook(0);

    for (auto it = listBook.begin(); it != listBook.end();) {
        Book* element = *it; // this is the object "Book"
        if (element->getName() == name) {
            delete element; 
            it = listBook.erase(it); // we have to keep the "it" to don't have an invalid pointer (erase return the adress of the next adress Book in vector != null )

            ++countRemovedBook;
        }
        else {
            ++it; // increase the adresse of one book
        }
    }

    return countRemovedBook;
}


bool Library::checkBook(string const& name) const {
    for (Book const* element : listBook) {
        if (element->getName() == name) { return true; } // if the book name called is in the vector
    } return false;
}