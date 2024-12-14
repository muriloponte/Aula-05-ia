import json
import os

# Função para carregar o estoque do arquivo JSON
def carregar_estoque():
    if os.path.exists("estoque.json"):
        with open("estoque.json", "r") as file:
            estoque = json.load(file)
        return estoque
    else:
        # Caso o arquivo não exista, criamos um estoque inicial
        return {}

# Função para salvar o estoque de volta no arquivo JSON
def salvar_estoque(estoque):
    with open("estoque.json", "w") as file:
        json.dump(estoque, file, indent=4)

# Função para listar o estoque
def listar_estoque(estoque):
    if not estoque:
        print("O estoque está vazio.")
    else:
        print("Estoque atual:")
        for item, dados in estoque.items():
            print(f"Produto: {item}, Quantidade: {dados['quantidade']}, Preço: R${dados['preco']:.2f}")

# Função para registrar uma venda
def registrar_venda(estoque):
    produto = input("Digite o nome do produto vendido: ").strip()
    
    if produto in estoque:
        quantidade_vendida = int(input(f"Digite a quantidade de {produto} vendida: "))
        if quantidade_vendida <= estoque[produto]["quantidade"]:
            # Atualiza a quantidade no estoque
            estoque[produto]["quantidade"] -= quantidade_vendida
            print(f"Venda registrada! {quantidade_vendida} unidades de {produto} foram vendidas.")
        else:
            print("Quantidade solicitada é maior do que a disponível no estoque.")
    else:
        print("Produto não encontrado no estoque.")

# Função para adicionar ou editar produtos no estoque
def adicionar_produto(estoque):
    produto = input("Digite o nome do produto: ").strip()
    
    if produto in estoque:
        print("Produto já existe no estoque. Você pode editar a quantidade.")
    else:
        preco = float(input("Digite o preço do produto: R$"))
        quantidade = int(input("Digite a quantidade do produto: "))
        estoque[produto] = {"quantidade": quantidade, "preco": preco}
        print(f"Produto {produto} adicionado ao estoque.")

# Função principal
def main():
    estoque = carregar_estoque()
    
    while True:
        print("\nMenu de Opções:")
        print("1. Listar estoque")
        print("2. Registrar venda")
        print("3. Adicionar produto")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            listar_estoque(estoque)
        elif opcao == "2":
            registrar_venda(estoque)
        elif opcao == "3":
            adicionar_produto(estoque)
        elif opcao == "4":
            salvar_estoque(estoque)
            print("Estoque salvo. Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
