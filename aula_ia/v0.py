import json
import os

ARQUIVO_ESTOQUE = 'estoquee.json'

def ler_estoque():
    if os.path.exists(ARQUIVO_ESTOQUE):
        with open(ARQUIVO_ESTOQUE, 'r') as arquivo:
            return json.load(arquivo)
    return {}

def salvar_estoque(estoque):
    with open(ARQUIVO_ESTOQUE, 'w') as arquivo:
        json.dump(estoque, arquivo, indent=2)

def adicionar_produto(nome, quantidade):
    estoque = ler_estoque()
    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade
    salvar_estoque(estoque)
    print(f'Produto "{nome}" adicionado. Quantidade atual: {estoque[nome]}')

def registrar_venda(nome, quantidade):
    estoque = ler_estoque()
    if nome not in estoque or estoque[nome] < quantidade:
        print(f'Erro: Estoque insuficiente para "{nome}"')
        return
    estoque[nome] -= quantidade
    salvar_estoque(estoque)
    print(f'Venda registrada para "{nome}". Quantidade restante: {estoque[nome]}')

def visualizar_estoque():
    estoque = ler_estoque()
    print('Estoque atual:')
    for produto, quantidade in estoque.items():
        print(f'{produto}: {quantidade}')

def menu():
    while True:
        print("\n1. Adicionar produto")
        print("2. Registrar venda")
        print("3. Visualizar estoque")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            adicionar_produto(nome, quantidade)
        elif opcao == '2':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade vendida: "))
            registrar_venda(nome, quantidade)
        elif opcao == '3':
            visualizar_estoque()
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()