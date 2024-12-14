import json
import os
from datetime import datetime

class GestorEstoque:
    def __init__(self, arquivo_estoque='estoque.json'):
        self.arquivo_estoque = arquivo_estoque
        self.estoque = self.carregar_estoque()

    def carregar_estoque(self):
        """Carrega o estoque do arquivo JSON ou cria um novo se não existir."""
        if os.path.exists(self.arquivo_estoque):
            with open(self.arquivo_estoque, 'r') as arquivo:
                return json.load(arquivo)
        else:
            return []

    def salvar_estoque(self):
        """Salva o estoque atualizado no arquivo JSON."""
        with open(self.arquivo_estoque, 'w') as arquivo:
            json.dump(self.estoque, arquivo, indent=4, ensure_ascii=False)

    def adicionar_produto(self, nome, quantidade, preco):
        """Adiciona um novo produto ao estoque."""
        for produto in self.estoque:
            if produto['nome'].lower() == nome.lower():
                print(f"Produto {nome} já existe no estoque.")
                return False

        novo_produto = {
            'nome': nome,
            'quantidade': quantidade,
            'preco': preco,
            'historico': [{
                'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'tipo': 'Adição',
                'quantidade': quantidade
            }]
        }
        
        self.estoque.append(novo_produto)
        self.salvar_estoque()
        print(f"Produto {nome} adicionado com sucesso!")
        return True

    def realizar_venda(self, nome, quantidade):
        """Realiza uma venda, atualizando a quantidade em estoque."""
        for produto in self.estoque:
            if produto['nome'].lower() == nome.lower():
                if produto['quantidade'] >= quantidade:
                    produto['quantidade'] -= quantidade
                    
                    # Registra o histórico da venda
                    produto['historico'].append({
                        'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'tipo': 'Venda',
                        'quantidade': quantidade
                    })
                    
                    self.salvar_estoque()
                    valor_total = quantidade * produto['preco']
                    print(f"Venda realizada: {quantidade} {nome}(s) - Valor total: R${valor_total:.2f}")
                    return True
                else:
                    print(f"Erro: Quantidade indisponível. Estoque atual de {nome}: {produto['quantidade']}")
                    return False
        
        print(f"Produto {nome} não encontrado no estoque.")
        return False

    def listar_estoque(self):
        """Lista todos os produtos em estoque."""
        if not self.estoque:
            print("Estoque vazio.")
            return

        print("\n--- INVENTÁRIO ATUAL ---")
        for produto in self.estoque:
            print(f"Produto: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Preço: R${produto['preco']:.2f}")
            print("--------------------")

    def buscar_produto(self, nome):
        """Busca um produto específico no estoque."""
        for produto in self.estoque:
            if produto['nome'].lower() == nome.lower():
                print("\n--- DETALHES DO PRODUTO ---")
                print(f"Nome: {produto['nome']}")
                print(f"Quantidade em Estoque: {produto['quantidade']}")
                print(f"Preço: R${produto['preco']:.2f}")
                
                print("\nHistórico:")
                for registro in produto['historico']:
                    print(f"Data: {registro['data']} - Tipo: {registro['tipo']} - Quantidade: {registro['quantidade']}")
                
                return produto
        
        print(f"Produto {nome} não encontrado.")
        return None

def menu_principal():
    gestor = GestorEstoque()

    while True:
        print("\n--- SISTEMA DE CONTROLE DE ESTOQUE ---")
        print("1. Adicionar Produto")
        print("2. Realizar Venda")
        print("3. Listar Estoque")
        print("4. Buscar Produto")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade inicial: "))
            preco = float(input("Preço do produto: "))
            gestor.adicionar_produto(nome, quantidade, preco)

        elif opcao == '2':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade a vender: "))
            gestor.realizar_venda(nome, quantidade)

        elif opcao == '3':
            gestor.listar_estoque()

        elif opcao == '4':
            nome = input("Nome do produto a buscar: ")
            gestor.buscar_produto(nome)

        elif opcao == '5':
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()