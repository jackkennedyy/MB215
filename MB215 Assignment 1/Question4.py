class EmailDirectory:
    def __init__(self):
        self.contacts = {}
    
    def run(self):
        choice = None
        while choice != "0":
            print("\nMenu Options:")
            print("0 - Exit Program")
            print("1 - Look Up an Email Address")
            print("2 - Add a New Contact")
            print("3 - Update an Existing Contact")
            print("4 - Remove a Contact")
            print("5 - Display All Contacts")
            choice = input("\nEnter your choice > ")
            if choice == "1":
                self.lookup_email()
            elif choice == "2":
                self.add_contact()
            elif choice == "3":
                self.update_contact()
            elif choice == "4":
                self.remove_contact()
            elif choice == "5":
                self.display_all_contacts()
    
    def lookup_email(self):
        name = input("Enter the name: ")
        email = self.contacts.get(name)
        if email:
            print(f"The email address is {email}")
        else:
            print("No contact found.")
    
    def add_contact(self):
        name = input("Enter the name: ")
        email = input("Enter the email: ")
        self.contacts[name] = email
        print(f"Contact added: {name}: {email}")
    
    def update_contact(self):
        name = input("Enter the name: ")
        if name in self.contacts:
            new_email = input("Enter the new email: ")
            self.contacts[name] = new_email
            print(f"Contact updated: {name}: {new_email}")
        else:
            print("No contact found.")
    
    def remove_contact(self):
        name = input("Enter the name: ")
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact removed: {name}")
        else:
            print("No contact found.")
    
    def display_all_contacts(self):
        if self.contacts:
            for name, email in self.contacts.items():
                print(f"{name}: {email}")
        else:
            print("No contacts to display.")
    

# Main execution
if __name__ == "__main__":
    directory = EmailDirectory()
    directory.run()