
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
    print("\n====== RESUMO DAS VENDAS ======")
    print(f"Quantidade de vendas: {quantidade_vendas}")
    print(f"Unidades comercializadas: {unidades_vendidas}")
    print(f"Faturamento bruto: R$ {faturamento:.2f}")

    print("===============================")
