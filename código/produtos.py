def cadastrar_produto(produtos):
    print("\n====== CADASTRO DE PRODUTO ======")

    codigo = input("Código do produto: ")

    # --- Verifica se o código já existe
    for produto in produtos:
        if produto["codigo"] == codigo:
            print("Já existe um produto com esse código!")
            return

    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")

    # --- Validação do preço
    while True:
        try:
            preco = float(input("Preço: R$ ").replace(",", "."))

            if preco <= 0:
                print("O preço deve ser maior que R$ 0,00.")
                continue

            break

        except ValueError:
            print("Digite apenas números! Exemplo: 99.90")

    # --- Validação do estoque
    try:
        estoque = int(input("Quantidade em estoque: "))

        if estoque < 0:
            print("Este número não pode ser negativo.")
            return

    except ValueError:
        print("Quantidade inválida.")
        return

    produto = {
        "codigo": codigo,
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "estoque": estoque
    }

    produtos.append(produto)

    print("\nProduto cadastrado com sucesso!")


# -- LISTAR OS PRODUTOS

def listar_produtos(produtos):
    print("\n====== LISTA DE PRODUTOS ======")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(f"\nCódigo: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Estoque: {produto['estoque']} unidades")

        print("-------------------------------")

    print(f"Total de produtos cadastrados: {len(produtos)}")
