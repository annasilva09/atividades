produtos = []

# 1. CREATE (Adicionar)

def adicionar_produto(nome):
    produtos.append(nome)
    print(f" Produto '{nome}' adicionado com sucesso!")


# 2. READ (Listar)

def listar_produtos():
    if not produtos:
        print("A lista de produtos está vazia.")
        return

    print("\n--- LISTA DE PRODUTOS ---")
    for i, nome in enumerate(produtos, start=1):
        print(f"{i}. {nome}")
    print("-------------------------")

# 3. UPDATE (Atualizar)

def atualizar_produto(nome_antigo, nome_novo):
    nome_antigo = input("Digite um produto antigo: ")
    nome_novo = input("Digite o produto novo: ")
    if nome_antigo in produtos:
        # Descobre a posição (índice) da primeira ocorrência do produto
        indice = produtos.index(nome_antigo)
        produtos[indice] = nome_novo
        print(f" Produto '{nome_antigo}' atualizado para '{nome_novo}'!")
    else:
        print(f" Erro: Produto '{nome_antigo}' não encontrado.")



# 4. DELETE (Deletar)

def deletar_produto(nome):
    if nome in produtos:
        produtos.remove(nome)
        print(f" Produto '{nome}' removido com sucesso!")
    else:
        print(f" Erro: Produto '{nome}' não encontrado.")


# Programa principal
opcao = -1
while (opcao != "sair"):
    print()
    opcao = input("Escolha uma opção: \n cadastrar \n atualizar \n  listar \n deletar \n sair \n")
    if(opcao == "cadastrar"):
        adicionar_produto(input("Digite o produto: "))
    elif(opcao == "atualizar"):
        atualizar_produto("nome_antigo", "nome_novo")
    elif(opcao == "listar"):
        listar_produtos()
    elif(opcao == "deletar"):
        deletar_produto(input("Digite o produto para deletar: "))
    elif(opcao == "sair"):
        opcao == "sair"
    else:
        print("Opção invalida")