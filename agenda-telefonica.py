import os

class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        os.system('cls')

        if nome in self.contatos:
            print(f'O nome: {nome}, já está sendo usado em sua lista.')

        elif telefone in self.contatos.values():
            print(f'O número de telefone: {telefone}, já está sendo usado em sua lista.')

        else:
            self.contatos[nome] = telefone
            print(f'O contato {nome} foi adicionado com sucesso.')

        input('Aperte ENTER para voltar ao MENU: ')
        menu()

    def remover_contato(self, nome):
        os.system('cls')
        if nome in self.contatos:
            del self.contatos[nome]
            print(f'O contato {nome} foi removido.')
        
        else:
            print(f'O contato {nome} não foi encontrado.')

        input('Aperte ENTER para voltar ao MENU: ')
        menu()

    def pesquisar_contato(self, nome):
        os.system('cls')
        if nome in self.contatos:
            print(f'Nome: {nome} Telefone: {self.contatos[nome]}')
        
        else:
            print(f'O contato {nome} não foi encontrado.')

        input('Aperte ENTER para voltar ao MENU: ')
        menu()

    def exibir_contatos(self):
        os.system('cls')

        if not self.contatos:
            print('Sua lista de contatos está vazia.')

        else:
            for nome in self.contatos.keys():
                print(f'Nome: {nome} Telefone: {self.contatos[nome]}')

        input('Aperte ENTER para voltar ao MENU: ')
        menu()

contatos = AgendaTelefonica()

def menu():
    os.system('cls')
    print('1. Adicionar contatos \n2. Remover contatos \n3. Pesquisar contatos \n4. Lista de contatos \n5. Sair')
    opcao = int(input('Digite uma das alternativas: '))
    
    if opcao == 1:
        os.system('cls')
        nome = str(input('Digite o nome do novo contato: '))
        telefone = int(input('Digite o telefone do novo contato: '))
        contatos.adicionar_contato(nome, telefone)

    elif opcao == 2:
        os.system('cls')
        nome = str(input('Digite o nome do contato que você quer apagar: '))
        contatos.remover_contato(nome)

    elif opcao == 3:
        os.system('cls')
        nome = str(input('Digite o nome que deseja pesquisar: '))
        contatos.pesquisar_contato(nome)

    elif opcao == 4:
        os.system('cls')
        contatos.exibir_contatos()

    elif opcao == 5:
        os.system('cls')
        print('Encerrando o programa...')
        exit()

    else:
        print('Opção inválida! Tente novamente.')
        input('Aperte ENTER para voltar ao MENU: ')
        menu()
    
menu()
