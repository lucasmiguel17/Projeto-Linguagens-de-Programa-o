
# -- RELATÓRIO FINANCEIRO E FISCAL

def gerar_relatorio(produtos, vendas):
    print("\n====== RELATÓRIO FINANCEIRO ======")

    if not vendas:
        print("Ainda não existem vendas registradas.")
        return

    # -- CALCULAR INFORMAÇÕES

    quantidade_vendas = len(vendas)

    unidades_vendidas = sum(venda["quantidade"] for venda in vendas)

    faturamento = sum(venda["total"] for venda in vendas)

    # -- EXIBIR RELATÓRIO
    print("\n====== RESUMO GERAL ======")
    print(f"Vendas realizadas: {quantidade_vendas}")
    print(f"Unidades vendidas: {unidades_vendidas}")
    print(f"Faturamento total: R$ {faturamento:.2f}")

    # -- EXIBIR VENDAS INDIVIDUAIS
    print("\n====== DETALHAMENTO DAS VENDAS ======")

    for i, venda in enumerate(vendas, start=1):
        print(f"\nVenda {i}")
        print(f"Código: {venda['codigo']}")
        print(f"Produto: {venda['nome']}")
        print(f"Quantidade: {venda['quantidade']}")
        print(f"Preço unitário: R$ {venda['preco_unitario']:.2f}")
        print(f"Total: R$ {venda['total']:.2f}")

    print("\n====================================")
