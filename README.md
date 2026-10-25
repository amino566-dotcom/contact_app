A simple command-line Contact Book application built with Python. It allows users to manage their contacts by adding, viewing, searching, and deleting contact information. Contact data is stored in a local text file, so it persists between program executions.

✨ Features

Add Contacts: Save a contact's name, phone number, and email address.

View All Contacts: Display all saved contacts with their corresponding indexes.

Search Contacts: Find a contact by name.

Delete Contacts: Remove a contact using its index.

Persistent Storage: Store contact information in contacts.txt using file handling.

Object-Oriented Design: Represent contacts using a custom Python class.

Automatic File Creation: Create the contact file if it does not already exist.

🛠️ Technologies Used

Python 3

Object-Oriented Programming (OOP)

File handling (open(), reading, and writing)

Classes, objects, and class methods

Exception handling

Lists and loops

String manipulation

📂 Project Structure

contact-book/
├── contact_book.py
├── contacts.txt
└── README.md

contact_book.py — Contains the application logic and command-line menu.

contacts.txt — Stores contact information. It is created automatically when needed.

README.md — Documentation for the project.

🚀 Getting Started

1. Clone the repository

git clone <YOUR_REPOSITORY_URL>

2. Navigate to the project directory

cd contact-book

3. Run the application

python3 contact_book.py

No external Python libraries are required.

💻 Usage

When you run the application, a menu appears:

==== Contacts ====
1 - Add new contact
2 - View all contacts
3 - Search for a contact by name
4 - Delete a contact
5 - Exit

Choose an option by entering its corresponding number.

Example: Adding a contact

Enter a number: 1
Enter the name: Amine
Enter the phone number: 0612345678
Enter the email: amine@example.com
The contact added successfully

Example: Viewing contacts

0 - Name: Amine - Phone number: 0612345678 - Email: amine@example.com

Contacts are saved in contacts.txt and can be loaded again the next time the application starts.

🧠 What I Learned

Through this project, I practiced:

Designing classes and creating objects in Python.

Using __init__() to initialize object attributes.

Implementing __str__() to represent objects as strings.

Using @classmethod to reconstruct objects from stored text.

Reading from and writing to files.

Using lists to store and manipulate collections of objects.

Searching and deleting elements by index.

Handling common file and input errors.

Organizing a small application into reusable functions.

🔮 Future Improvements

Possible enhancements include:

Validate phone numbers and email addresses.

Prevent duplicate contacts.

Support case-insensitive and partial-name searches.

Add an update-contact feature.

Replace plain-text storage with JSON or SQLite.

Improve error handling for invalid menu choices and corrupted files.

Add automated tests using unittest or pytest.

👨‍💻 Author

Amine

This project was created as part of my journey to strengthen my Python programming skills and build practical software projects.

If you find this project useful, feel free to fork the repository and improve it.
