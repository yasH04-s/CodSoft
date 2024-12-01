class Contactbook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = {
            'Name': name,
            'Phone': phone,
            'Email': email,
            'Address': address
        }
        self.contacts.append(contact)
        print(f"Contact added: {name}")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print('\nContact List:')
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. {contact['Name']} - {contact['Phone']}")

    def search_contact(self, case):
        results = []
        for contact in self.contacts:
            if case.lower() in contact['Name'].lower() or case in contact['Phone']:
                results.append(contact)
        return results

    def update_contact(self, index, name=None, phone=None, email=None, address=None):
        if 1 <= index <= len(self.contacts):
            contact = self.contacts[index - 1]
            contact['Name'] = name if name else contact['Name']
            contact['Phone'] = phone if phone else contact['Phone']
            contact['Email'] = email if email else contact['Email']
            contact['Address'] = address if address else contact['Address']
            print(f"Contact updated: {contact['Name']}")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 1 <= index <= len(self.contacts):
            deleted_contact = self.contacts.pop(index - 1)
            print(f"Contact deleted: {deleted_contact['Name']}")
        else:
            print("Invalid contact index.")

def main():
    contact_book = Contactbook()

    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        opt = input("Enter your choice: ")

        if opt == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            contact_book.add_contact(name, phone, email, address)

        elif opt == '2':
            contact_book.view_contacts()

        elif opt == '3':
            keyword = input("Enter Name or Phone Number to search: ")
            search_results = contact_book.search_contact(keyword)
            if search_results:
                print("\nSearch Results:")
                for result in search_results:
                    print(f"{result['Name']} - {result['Phone']}")
            else:
                print("No matching contacts found.")

        elif opt == '4':
            index = int(input("Enter the index of the contact to update: "))
            contact_book.update_contact(index)

        elif opt == '5':
            index = int(input("Enter the index of the contact to delete: "))
            contact_book.delete_contact(index)

        elif opt == '6':
            print("Exiting the Contact Management System.")
            break

        else:
            print("Invalid choice, Try again.")

if __name__ == "__main__":
    main()
