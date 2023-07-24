#pragma once
#ifndef DEF_LIBRARY
#define DEF_LIBRARY

#include "Book.h"

#include <vector>
#include <string>

class Library {
	private:
		std::vector<Book*> listBook;
	
	public:
		int getBooksize() const;

		void addBook(Book *newBook);
		int removeBook(const std::string& name);

		void showBooks(std::string const &name = "None") const;
		bool checkBook(std::string const &name = "None") const;

};


#endif // !DEF_LIBRARY

