import functions as func

contas = {}

while True:
    
    escolha = func.Menu()
    
    if escolha == 1:
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        obs = input("Obs: ")
        func.Adicionar_conta(nome, email, senha, obs)
        
    elif escolha == 0:
        print('-' * 20)
        print("Programa finalizado!")
        print('-' * 20)
        break
    else:
        print("-" * 22)
        print("Essa opção não existe!")