from produtos import cadastrar_produto, listar_produtos

def mostrar_menu():
    print("\n====== GAMESTOCK ======")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Consultar produto")
    print("4 - Registrar venda")
    print("5 - Relatórios")
    print("0 - Sair")
    print("=======================")


def main():
    produtos = []

    while True:
        mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1": # -- CADASTRAR

            cadastrar_produto(produtos)

        elif opcao == "2": # -- LISTAR

            listar_produtos(produtos)

        elif opcao == "3":
            print("Consulta de produtos")

        elif opcao == "4":
            print("Registro de vendas")

        elif opcao == "5":
            print("Relatórios")

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida! Tente novamente.")


main()