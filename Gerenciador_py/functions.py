import os

class Conta():
    contas = {}         # Dicionário que faz o papel de um DB.

    # Método construtor da classe.
    def __init__(self, name, email, senha):
        self.__name = name
        self.__email = email
        self.__senha = senha
    
    # Getter_nome
    @property
    def name(self):
        return self.__name
    
    # Setter_nome
    @name.setter
    def name(self, nome):
        self.__name = nome        
    
    # Getter_email
    @property
    def email(self):
        return self.__email
    
    # Setter_email
    @email.setter
    def email(self, email):
        self.__email = email
    
    # Getter_senha
    @property
    def senha(self):
        return self.__senha
    
    # Setter_senha
    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    # Método de adição de uma conta no dicionário.
    @staticmethod
    def add_conta(nome, email, senha):
        Conta.contas[nome] = {'email': email, 'senha': senha}
    
    # Método que remove uma conta do dicionário.
    @staticmethod
    def remove_conta(nome):
        if nome in Conta.contas:
            del Conta.contas[nome]
        else:
            print("Conta não encontrada!")
    
    # Método de apresentação da lista.
    def show_lista():
        for nome, dados in Conta.contas.items():
            print(f"Nome: {nome}, Email: {dados['email']}, Senha: {dados['senha']}")


@staticmethod
def apagar():
    os.system('cls')

def Menu():
    print("[1]Adicionar conta")
    print("[2]Remover conta")
    print("[3]Lista de contas")
    escolha = input("Escolha: ")
    return escolha