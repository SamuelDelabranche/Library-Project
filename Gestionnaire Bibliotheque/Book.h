#pragma once
#ifndef DEF_BOOK
#define DEF_BOOK

#include <string>
#include <iostream>

class Book{
	friend std::ostream& operator<<(std::ostream& flux, Book const& book);

	public:
		// Concructor 
		Book(std::string name, std::string author, std::string date = "None", double price = 0);
		std::string getName() const;

	private:
		// Attributes
		std::string m_name;
		std::string m_author;
		std::string m_date;
		double m_price;

};


#endif // !DEF_BOOK
