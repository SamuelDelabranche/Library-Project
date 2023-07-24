#include "Library.h"
#include "Book.h"

#include <iostream>
#include <string>
#include <Windows.h>

using namespace std;

void clearCommandByOs() { // Clear terminal depending of the os
	#if __linux__ 
		system("clear");
	#elif _WIN32
		system("cls");
	#else
	#endif
}



Book* createBook() {
	clearCommandByOs();
	cout << "###- Adding Book -###" << endl;

	string name, author, date;
	double price(0);

	cin.ignore(); // Clear for the terminal


	cout << "Name: ";
	getline(cin, name);

	cout << "Author: ";
	getline(cin, author);

	cout << "Date: ";
	getline(cin, date);

	do {
		if (cin.fail()) { // if price !double
			cin.clear(); // clear the error status of cin
			cin.ignore(); // clear the cin of characters

			cout
				<< "\x1b[1A" // Move cursor up one
				<< "\x1b[2K"; // Delete the entire line
		}

		cout << "Price: ";
	} while (!(cin >> price)); // while input isn't a number


	clearCommandByOs();
	Book* newBook = new Book(name, author, date, price); // create new Book
	return newBook;
}

void showGUI(bool error = false, int errorCode = -1) {

	clearCommandByOs();

	if (error) { cout << "Fonctionality not included! [" << errorCode << "]" << endl; } // if Error, it show this line

	// GUI
	cout << "###- Library Project -###" << endl;
	cout << "[1] Add Book " << endl;
	cout << "[2] Remove Book " << endl;
	cout << "[3] Show Book {With name}" << endl;
	cout << "[4] Show all Books " << endl;
	cout << "[0] Quit the program " << endl;
	cout << endl;



}

int main() {
	string tempNameRemove, showByName;
	char temp;
	int choice;
	showGUI();




	Library mainLibrary;

	do {
		cout << "Your choice: ";
		cin >> choice;

		switch (choice) {
		default: 
			showGUI(true, choice);
			break;

		case 1: // Add a book
			mainLibrary.addBook(createBook());
			clearCommandByOs();
			showGUI();

			break;
		case 2: // Remove book by his name
			clearCommandByOs();

			cout << "Name: ";
			cin.ignore(); // Clear the input buffer to avoid issues.
			getline(cin, tempNameRemove); // Take all the line ( with space ) 

			// If book in library
			if (mainLibrary.checkBook(tempNameRemove)) { cout << "Count of books removed: " << mainLibrary.removeBook(tempNameRemove); }
			else { cout << "No book [" << tempNameRemove << "] was found! "; }

			Sleep(2000); // Wait 2s to see the response
			clearCommandByOs();
			showGUI();

			break;
		case 3: // Show books by their name
			clearCommandByOs();


			cout << "Search by Name: ";
			cin.ignore();
			getline(cin, showByName);

			mainLibrary.showBooks(showByName);

			cout << endl << "Continue [enter any char]: ";
			cin >> temp;

			clearCommandByOs();
			showGUI();

			break;

		case 4: // Show all books
			clearCommandByOs();

			if (mainLibrary.getBooksize() == 0) { cout << "The Library is empty"; }
			else { mainLibrary.showBooks(); }

			cout << endl << "Continue [enter any char]: ";
			cin >> temp;

			clearCommandByOs();
			showGUI();

			break;
		}
	} while (choice != 0);
}