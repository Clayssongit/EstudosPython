from contato import Contact
from contato_agenda import ContactBook

contato_agenda = ContactBook()

while True:
    print("\n --- Opções Agenda da Contatos --- ")
    print(" 1. Adicionar Contato")
    print(" 2. Remover Contato")
    print(" 3. Listar Contato")
    print(" 4. Buscar Contato")
    print(" 5. Sair")

    choice = input(">")

    if choice == "1":
        name = input("Digite o nome: ")
        phone = input("Digite o telefone: ")
        email = input("Digite o email: ")

        contact = Contact(name, phone, email)
        contato_agenda.add_contact(contact)
        print("Contato adicionado com sucesso.")
    
    elif choice == "2":
        name = input("Digite o nome para remover: ")
        contact = contato_agenda.seach_contact(name)
        if contact:
            contato_agenda.remove_contact(contact)
            print("Contato removido com sucesso")

    elif choice == "3":
        contato_agenda.display_contact()
    
    elif choice == "4":
        name = input("Digite o nome para pesquisar: ")
        contact = contato_agenda.seach_contact(name)
    
    elif choice == "5":
        break

    else:
        print("Opção Inválida. Utilize uma opção de 1 a 5")