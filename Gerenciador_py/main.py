import functions as func
import os
from time import sleep


func.apagar()

while True:
    
    escolha = func.Menu()
    
    if escolha == '1':
        func.apagar()
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        func.Conta.add_conta(nome, email, senha)
        print("\nConta adicionada com sucesso!")
        sleep(1)
        func.apagar()

    elif escolha == '2':
        func.apagar()
        nome = input("Nome: ")
        func.Conta.remove_conta(nome)
        print("\nConta removida com sucesso!")
        sleep(1)
        func.apagar()
    
    elif escolha == '3':
        func.apagar()
        func.Conta.show_lista()
        continuar = input("Para voltar ao menu aperte enter.")
        func.apagar()
        
        

    elif escolha == '0':
        func.apagar()
        print('-' * 20)
        print("Programa finalizado!")
        print('-' * 20)
        break
    
    else:
        print("-" * 22)
        print("Essa opção não existe!")
        print("-" * 22)
        
        