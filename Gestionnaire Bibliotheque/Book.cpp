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
