#include "Book.h"
#include <string>
#include <iostream>

using namespace std;

// Constructor
Book::Book(std::string name, std::string author, std::string date, double price) : m_name(name), m_author(author), m_date(date), m_price(price){
	cout << "New Book added! " << endl;
	cout << "Informations: " << endl;
	cout << "Name: " << m_name << endl;
	cout << "Author: " << m_author << endl;
	cout << "Date of creation: " << m_date << endl;
	cout << "Price: $" << m_price << endl;
}


ostream &operator<<(ostream& flux, Book const& book) {
	flux << book.m_name << endl;
	flux << "   Author: " << book.m_author << endl;
	flux << "   Date: " << book.m_date << endl;
	flux << "   Price: $" << book.m_price << endl;

	return flux;
}

string Book::getName() const{
	return this->m_name;
}