# -- GUARDAR DADOS AO FECHAR O PROGRAMA

import json
from pathlib import Path

# Localização do arquivo de dados
ARQUIVO_DADOS = Path(__file__).parent / "dados.json"


# -- CARREGAR DADOS

def carregar_dados():
    if not ARQUIVO_DADOS.exists():
        return [], []

    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

            produtos = dados.get("produtos", [])
            vendas = dados.get("vendas", [])

            return produtos, vendas

    except (json.JSONDecodeError, OSError):
        print("Erro ao carregar os dados.")
        return [], []


# -- SALVAR DADOS

def salvar_dados(produtos, vendas):
    dados = {
        "produtos": produtos,
        "vendas": vendas
    }

    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
