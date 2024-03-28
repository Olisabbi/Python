class Node:
    def __init__(self, codigo_produto, proximo=None):
        self.codigo_produto = codigo_produto
        self.proximo = proximo

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserir_final(self, codigo_produto):
        novo_node = Node(codigo_produto)
        if self.cabeca is None:
            self.cabeca = novo_node
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_node

    def __str__(self):
        produtos = []
        atual = self.cabeca
        while atual:
            produtos.append(str(atual.codigo_produto))
            atual = atual.proximo
        return ' -> '.join(produtos)

def ler_codigo_barras():
   
    return input("Por favor, escaneie o código de barras ou digite o código do produto: ")

def menu():
    estoque = ListaEncadeada()
    while True:
        print("\nMenu de Gestão de Estoque:")
        print("1 - Inserir produto via leitor de código de barras")
        print("2 - Exibir estoque atual")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            codigo_produto = ler_codigo_barras()
            estoque.inserir_final(codigo_produto)
            print("Produto inserido com sucesso!")
        elif opcao == '2':
            print("Estoque atual:", estoque)
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Por favor, tente novamente.")

menu()
