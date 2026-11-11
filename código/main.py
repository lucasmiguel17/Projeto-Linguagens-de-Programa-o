from vendas import registrar_venda
from produtos import cadastrar_produto, listar_produtos, consultar_produto, remover_produto
from arquivos import carregar_dados, salvar_dados

def mostrar_menu():
    print("\n====== GAMESTOCK ======")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Consultar produto")
    print("4 - Registrar venda")
    print("5 - Remover produtos")
    print("0 - Sair")
    print("=======================")


def main():
    
    # Carregar dados ao iniciar o programa
    produtos, vendas = carregar_dados()

    while True:
        mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1": # -- CADASTRAR

            cadastrar_produto(produtos)
            salvar_dados(produtos, vendas)

        elif opcao == "2": # -- LISTAR

            listar_produtos(produtos)
            salvar_dados(produtos, vendas)

        elif opcao == "3": # -- CONSULTAR
            
            consultar_produto(produtos)
            salvar_dados(produtos, vendas)

        elif opcao == "4": # -- REGISTRAR VENDA
            
            registrar_venda(produtos, vendas)
            salvar_dados(produtos, vendas)

        elif opcao == "5": # -- REMOVER PRODUTOS

            remover_produto(produtos)
            salvar_dados(produtos, vendas)

        elif opcao == "0": # -- SAIR

            salvar_dados(produtos, vendas)
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida! Tente novamente.")


main()