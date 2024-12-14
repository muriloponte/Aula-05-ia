import json
import os

# Função para carregar o estoque do arquivo JSON
def carregar_estoque():
    if not os.path.exists('estoque.json'):
        return {"produtos": []}
    
    with open('estoque.json', 'r') as file:
        return json.load(file)

# Função para salvar o estoque no arquivo JSON
def salvar_estoque(estoque):
    with open('estoque.json', 'w') as file:
        json.dump(estoque, file, indent=4)

# Função para adicionar um produto ao estoque
def adicionar_produto(nome, quantidade, preco):
    estoque = carregar_estoque()
    produto = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }
    estoque["produtos"].append(produto)
    salvar_estoque(estoque)
    print(f'Produto {nome} adicionado ao estoque.')

# Função para realizar uma venda
def realizar_venda(nome, quantidade_vendida):
    estoque = carregar_estoque()
    for produto in estoque["produtos"]:
        if produto["nome"] == nome:
            if produto["quantidade"] >= quantidade_vendida:
                produto["quantidade"] -= quantidade_vendida
                salvar_estoque(estoque)
                print(f'Venda realizada: {quantidade_vendida} unidades de {nome}.')
                return
            else:
                print(f'Estoque insuficiente para {nome}. Disponível: {produto["quantidade"]}')
                return
    print(f'Produto {nome} não encontrado no estoque.')

# Função para exibir o estoque
def exibir_estoque():
    estoque = carregar_estoque()
    print("Estoque atual:")
    for produto in estoque["produtos"]:
        print(f'Nome: {produto["nome"]}, Quantidade: {produto["quantidade"]}, Preço: R${produto["preco"]:.2f}')

# Menu da aplicação
def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar produto")
        print("2. Realizar venda")
        print("3. Exibir estoque")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            adicionar_produto(nome, quantidade, preco)
        elif opcao == '2':
            nome = input("Nome do produto: ")
            quantidade_vendida = int(input("Quantidade vendida: "))
            realizar_venda(nome, quantidade_vendida)
        elif opcao == '3':
            exibir_estoque()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()