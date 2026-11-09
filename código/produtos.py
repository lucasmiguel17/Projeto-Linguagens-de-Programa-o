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
    try:
        preco = float(input("Preço: ").replace(",", "."))

        if preco <= 0:
            print("O preço deve ser maior que R$ 0,00.")
            return

    except ValueError:
        print("Preço inválido!")
        return

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