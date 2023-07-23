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

void loadingText(const int& time) {
	cout << "Loading";
	for (int i(0); i < 3; i++) {
		Sleep(time * 1000);
		cout << ".";
	}
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
	loadingText(2); // Make 3 '.' in 6secs
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

		case 1:
			mainLibrary.addBook(createBook());
			clearCommandByOs();
			showGUI();

			break;
		case 2:
			break;
		case 3:
			break;

		case 4:
			clearCommandByOs();
			mainLibrary.showBooks();

			char temp;
			cout << endl << "Continue [enter any char]: ";
			cin >> temp;

			clearCommandByOs();
			showGUI();

			break;
		}
	} while (choice != 0);
}