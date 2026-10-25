class Contact_Book:
    def __init__(self, name , phonenum , email):
        self.name = name
        self.phonenum = phonenum
        self.email = email

    def __str__(self):
        return(f"{self.name};{self.phonenum};{self.email}")
    
    @classmethod
    def data_string(cls, date_str):
        name , phonenum , email = date_str.split(';')
        return cls(name , phonenum, email)
    
def add_contact(contact , filename="contacts.txt"):
    try:
        with open(filename , 'a') as file:
            file.write(str(contact) + "\n")
    except Exception as e:
        print("Error saving contact:", e)

def load_contacts(filename="contacts.txt"):
    contacts = []
    try:
        with open(filename , 'r') as file:
            for line in file:
                contacts.append(Contact_Book.data_string(line))
    except FileNotFoundError:
        open(filename , 'w').close()
    except Exception as e:
        print("Error saving contact:", e)
    return contacts

def search_contact(conta):
    contact = load_contacts()
    try:
        for idx , cont in enumerate(contact):
            if conta == cont.name:
                return f"{idx} : {cont.name}; {cont.phonenum}; {cont.email}"
        else:
            return f"contact does not exist."
    except Exception as e:
        print("Error saving contact:", e) 

def delete_contact(index , filename="contacts.txt"):
    contact = load_contacts()
    try:
        contact.pop(index)
        with open(filename ,'w') as file:
            for line in contact:
                file.write(str(line) + '\n')
            
    except IndexError:
        print("Invalid index.")
    except Exception as e:
        print("Error deleting contact:", e)

def options():
    print("==== Contacts ====")
    print("1 - Add new contact")
    print("2 - View all contacts")
    print("3 - Search for a contact by name")
    print("4 - Delete a contact")
    print("5 - exit")

def main():
    while True:
        options()
        choice = int(input("enter a number:" ))
        if choice == 1 :
            name = input("enter the name : ")
            phonenum = input("enter the phon enumber: ")
            email = input("enter the email: ")
            contact = Contact_Book(name, phonenum , email)
            print("the COntact Added Successafully")
            add_contact(contact)
        
        elif choice == 2:
            contacts = load_contacts()
            try:
                if not contacts:
                    print("No contact Exist.")
                else:
                    for idx, line in enumerate(contacts):
                        print(f"{idx}-name : {line.name} - phone number: {line.phonenum} -Email : {line.email}")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == 3:
            contact = load_contacts()
            conta = input("enter the name of contact you want to find: ")
            try:
                if not contacts:
                    print("No contact Exist.")
                else:
                    print(search_contact(conta))
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == 4:
            contact = load_contacts()
            index = int(input("enter the name of contact you want to delete: "))
            try:
                if not contacts:
                    print("No contact Exist.")
                else:
                    delete_contact(index)
                    print("the contact deleted successfully")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == 5 :
            print("thank you for using our application.")
            break
        else:
            print("enter a valid number")

if __name__ =="__main__":
    main()
    
        
