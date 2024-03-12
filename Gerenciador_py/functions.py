#Essa função gera o menu.
def Menu():
    print("\nGerenciador de Contas")
    print("[1]Nova conta")
    print("[2]Remover conta")
    print("[0]Sair")
    escolha = int(input('Digite uma opção: '))
    return escolha


contas = {}

#Essa classe é utilizada para criar uma conta.
class Conta:
    def __init__(self, nome, email, senha, obs):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.obs = obs
        
#Essa função adiciona uma conta.
def Adicionar_conta(nome, email, senha, obs):
    nova_conta = Conta(nome, email, senha, obs)
    contas[len(contas) + 1] = nova_conta
    return print(nova_conta)

#Essa função remove uma conta.
def Remover_conta(nomes):
    for id_contas, dado in contas.items():
        if nomes == dado.nome:
            del contas[id_contas]

#Essa função mostra todas as contas por
def Mostrar_contas():
    for id_contas, dado in contas.items():
        print(f"Nome: {dado.nome}, Email: {dado.email}, Senha:  {dado.senha}, Obs: {dado.obs}")
