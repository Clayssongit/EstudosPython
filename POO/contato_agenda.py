class ContactBook:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        self.contacts.append(contact)
    
    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def display_contact(self):
        if not self.contacts:
            print("Lista de Contatos está Vazia")
        else:
            for contact in self.contacts:
                print(contact)
                print("-------------------------")

    def seach_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                return contact
        print("Contato não foi encontrado")