# 1 -- CADASTRAR PRODUTOS

def cadastrar_produto(produtos):
    print("\n====== CADASTRO DE PRODUTO ======")

    codigo = input("Código do produto: ")

    if not codigo.isdigit() or int(codigo) <= 0:
        print("O código do produto deve ser um número positivo.")
        return

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


# 2 -- LISTAR PRODUTOS

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

# 3 -- CONSULTAR PRODUTOS

def consultar_produto(produtos):
    print("\n====== CONSULTA DE PRODUTOS ======")
    print("1 - Consultar por código")
    print("2 - Consultar por categoria")
    print("3 - Consultar por faixa de preço")
    print("0 - Voltar")

    opcao = input("Escolha uma opção: ")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    encontrados = []

    if opcao == "1": # -- POR CÓDIGO 
        codigo = input("Digite o código do produto: ")

        for produto in produtos:
            if produto["codigo"] == codigo:
                encontrados.append(produto)

    elif opcao == "2": # -- POR CATEGORIA
        categoria = input("Digite a categoria: ").strip().lower()

        for produto in produtos:
            if produto["categoria"].lower() == categoria:
                encontrados.append(produto)

    elif opcao == "3": # -- POR PREÇO
        try:
            preco_min = float(input("Preço mínimo: R$ ").replace(",", "."))
            preco_max = float(input("Preço máximo: R$ ").replace(",", "."))

            if preco_min < 0 or preco_max < 0:
                print("Os preços não podem ser negativos. Ponha um valor válido.")
                return

            if preco_min > preco_max:
                print("O preço mínimo não pode ser maior que o máximo. Ponha um valor válido.")
                return

            for produto in produtos:
                if preco_min <= produto["preco"] <= preco_max:
                    encontrados.append(produto)

        except ValueError:
            print("Digite valores numéricos válidos!")
            return

    elif opcao == "0":  # -- VOLTAR
        return

    else:
        print("Opção inválida!")
        return

    # -- RESULTADOS DA CONSULTA
    if encontrados:
        print("\n====== RESULTADOS DA CONSULTA ======")

        for produto in encontrados:
            print(f"\nCódigo: {produto['codigo']}")
            print(f"Nome: {produto['nome']}")
            print(f"Categoria: {produto['categoria']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print(f"Estoque: {produto['estoque']} unidades")
            print("-------------------------------")

        print(f"Total encontrado: {len(encontrados)}")

    else:
        print("\nNenhum produto encontrado.")


