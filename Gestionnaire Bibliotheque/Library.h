#pragma once
#ifndef DEF_LIBRARY
#define DEF_LIBRARY

#include "Book.h"

#include <vector>

class Library {
	private:
		std::vector<Book*> listBook;
	
	public:
		void addBook(Book *newBook);
		void showBooks() const;

};


#endif // !DEF_LIBRARY

