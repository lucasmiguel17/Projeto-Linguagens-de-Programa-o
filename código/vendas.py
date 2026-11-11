# 4 -- REGISTRO DE VENDAS

def registrar_venda(produtos, vendas):
    print("\n====== REGISTRO DE VENDA (APENAS POR CÓDIGO) ======")

    if not produtos:
        print("Ainda não existem produtos cadastrados.")
        return

    codigo = input("Insira o código do produto: ")

    # -- PROCURAR O PRODUTO PELO CÓDIGO
    produto_encontrado = None

    for produto in produtos:
        if produto["codigo"] == codigo:
            produto_encontrado = produto
            break

    if produto_encontrado is None:
        print("Produto não encontrado!")
        return

    # -- QUANTOS TEM
    try:
        quantidade = int(input("Quantidade vendida: "))

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            return

    except ValueError:
        print("Digite uma quantidade válida!")
        return

    # -- EM ESTOQUE
    if quantidade > produto_encontrado["estoque"]:
        print("Estoque insuficiente!")
        print(f"Disponível: {produto_encontrado['estoque']} unidades.")
        return

    # -- CALCULO DO VALOR DA VENDA
    preco_unitario = produto_encontrado["preco"]
    total = preco_unitario * quantidade

    # -- ATUALIZA O ESTOQUE
    produto_encontrado["estoque"] -= quantidade

    # -- ARMAZENAR A VENDA EM UM DICIONÁRIO
    venda = {
        "codigo": codigo,
        "nome": produto_encontrado["nome"],
        "quantidade": quantidade,
        "preco_unitario": preco_unitario,
        "total": total
    }

    vendas.append(venda)

    print("\n====== VENDA REGISTRADA ======")
    print(f"Produto: {produto_encontrado['nome']}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço unitário: R$ {preco_unitario:.2f}")
    print(f"Total da venda: R$ {total:.2f}")
    print(f"Estoque restante: {produto_encontrado['estoque']}")
    print("=== OBRIGADO PELA COMPRA! VOLTE SEMPRE! ===")

