class Contact:
    phone_directory = []

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        Contact.phone_directory.append(self)

    def show_contact(self):
        return f"Name: {self.name}, Phone Number: {self.phone_number}"
    
    @classmethod
    def show_all_contacts(cls):
        if len(cls.phone_directory) == 0:
            return "No contacts in the directory."
        else:
            print("Phone Directory:")
            for contact in cls.phone_directory:
                print(contact.show_contact())

    @classmethod
    def find_contact_by_name(cls, name):
        for contact in cls.phone_directory:
            if contact.name.lower() == name.lower():
                return contact.show_contact()
        return "Contact not found."
    
    @staticmethod
    def is_valid_phone_number(phone_number):
        return phone_number.isdigit() and len(phone_number) in [10, 11, 12]
    


print("Welcome to the Phone Directory")
while True:
    print("\nMenu:")
    print("1. Add Contact")
    print("2. Show All Contacts")
    print("3. Find Contact by Name")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        name = input("Enter contact name: ")
        phone_number = input("Enter phone number: ")
        if Contact.is_valid_phone_number(phone_number):
            Contact(name, phone_number)
            print("Contact added successfully.")
        else:
            print("Invalid phone number. Please enter a valid number.")
    
    elif choice == '2':
        Contact.show_all_contacts()
    
    elif choice == '3':
        name = input("Enter the name to search: ")
        result = Contact.find_contact_by_name(name)
        print(result)
    
    elif choice == '4':
        print("Exiting the Phone Directory. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")