
import pandas as pd
import re
from datetime import datetime


# FUNCAO 1 - Carregar os dados

def carregar_dados(caminho):
    """Ler o arquivo CSV e retornar a tabela."""
    df = pd.read_csv(caminho, encoding="utf-8")
    return df


# FUNCAO 2 - Verificar a qualidade dos dados

def mostrar_qualidade_dados(df):
    """Mostrar valores ausentes e tipos de dados."""
    print("\nValores ausentes por coluna:")
    print(df.isnull().sum())

    print("\nTipos de dados:")
    print(df.dtypes)


# FUNCAO 3 - Verificar problemas numericos

def verificar_problemas_numericos(df):
    """Verificar quantidades invalidas e problemas nos precos."""

    quantidade_invalida = (
        (df["quantidade"] <= 0)
        | ((df["quantidade"] % 1) != 0)
    )

    preco_ausente = df["preco_unitario"].isnull()
    preco_negativo = df["preco_unitario"] < 0

    pedidos_com_problema = (
        quantidade_invalida | preco_ausente | preco_negativo
    )

    print("\nProblemas numericos:")

    print("Quantidade invalida:")
    print(quantidade_invalida.sum())

    print("Preco ausente:")
    print(preco_ausente.sum())

    print("Preco negativo:")
    print(preco_negativo.sum())

    print("Total de pedidos com problema:")
    print(pedidos_com_problema.sum())

    return (
        quantidade_invalida,
        preco_ausente,
        preco_negativo,
        pedidos_com_problema
    )


# FUNCAO 4 - Padronizar categorias

def padronizar_categorias(df):
    """Limpar e padronizar os nomes das categorias."""

    categorias_vazias_preenchidas = df["categoria"].isnull().sum()
    categorias_nao_vazias_alteradas = 0
    categorias_corrigidas = []

    for categoria in df["categoria"]:

        if pd.isnull(categoria):
            categoria_corrigida = "sem categoria"

        else:
            categoria_corrigida = categoria.strip().lower()

            categoria_corrigida = re.sub(
                r"[^a-zA-Z ]", "", categoria_corrigida
            )

            if categoria_corrigida.strip() == "":
                categoria_corrigida = "sem categoria"

            if categoria_corrigida != categoria:
                categorias_nao_vazias_alteradas += 1

        categorias_corrigidas.append(categoria_corrigida)

    df["categoria"] = categorias_corrigidas

    print("\nPadronizacao das categorias:")
    print(
        "Categorias vazias preenchidas:",
        categorias_vazias_preenchidas
    )
    print(
        "Categorias nao vazias alteradas:",
        categorias_nao_vazias_alteradas
    )

    print("\nCategorias apos a limpeza:")
    print(df["categoria"].value_counts())

    return df


# FUNCAO 5 - Padronizar canais de venda

def padronizar_canais(df):
    """Padronizar os nomes dos canais de venda."""

    canais_corrigidos = []
    canais_nao_reconhecidos = 0

    for canal in df["canal_venda"]:

        if pd.isnull(canal):
            canal_corrigido = "Não informado"
            canais_nao_reconhecidos += 1

        else:
            canal_limpo = canal.strip().lower()

            if canal_limpo == "mercado":
                canal_corrigido = "Mercado"

            elif canal_limpo == "loja física":
                canal_corrigido = "Loja física"

            elif canal_limpo == "web":
                canal_corrigido = "Web"

            else:
                canal_corrigido = canal
                canais_nao_reconhecidos += 1

        canais_corrigidos.append(canal_corrigido)

    df["canal_venda"] = canais_corrigidos

    print("\nCanais de venda padronizados:")
    print(df["canal_venda"].value_counts())
    print("Canais não reconhecidos:", canais_nao_reconhecidos)

    return df


# FUNCAO 6 - Investigar datas de entrega

def investigar_entregas(df):
    """Verificar pedidos sem data de entrega e seus status."""

    sem_entrega = df["data_entrega"].isnull()

    sem_entrega_cancelados = (
        sem_entrega & (df["status_pedido"] == "Cancelado")
    )

    sem_entrega_outros_status = (
        sem_entrega & (df["status_pedido"] != "Cancelado")
    )

    print("\nVerificacao das datas de entrega:")
    print("Pedidos sem data de entrega:", sem_entrega.sum())

    print(
        "Pedidos sem entrega e cancelados:",
        sem_entrega_cancelados.sum()
    )

    print(
        "Pedidos sem entrega com outros status:",
        sem_entrega_outros_status.sum()
    )

    print("\nExemplos de pedidos sem entrega e não cancelados:")

    print(
        df.loc[
            sem_entrega_outros_status,
            ["pedido_id", "status_pedido", "data_entrega"]
        ].head(3)
    )

    if sem_entrega_outros_status.sum() == 0:
        print("Hipotese confirmada nesta base.")
    else:
        print("Hipotese falsa nesta base.")


# FUNCAO 7 - Padronizar datas de venda

def padronizar_datas_venda(df):
    """Validar datas e extrair ano, mes, dia e hora."""

    anos = []
    meses = []
    dias = []
    horas = []
    datas_br = []
    datas_validas = []

    datas_vazias = 0
    datas_invalidas = 0

    for data_texto in df["data_venda"]:

        if pd.isnull(data_texto) or data_texto.strip() == "":
            datas_vazias += 1

            anos.append(None)
            meses.append(None)
            dias.append(None)
            horas.append(None)
            datas_br.append(None)
            datas_validas.append(False)

        else:
            try:
                data_convertida = datetime.strptime(
                    data_texto, "%Y-%m-%d %H:%M:%S"
                )

                anos.append(data_convertida.year)
                meses.append(data_convertida.month)
                dias.append(data_convertida.day)
                horas.append(data_convertida.hour)

                datas_br.append(
                    data_convertida.strftime("%d/%m/%Y")
                )

                datas_validas.append(True)

            except ValueError:
                datas_invalidas += 1

                anos.append(None)
                meses.append(None)
                dias.append(None)
                horas.append(None)
                datas_br.append(None)
                datas_validas.append(False)

    df["ano_venda"] = anos
    df["mes_venda"] = meses
    df["dia_venda"] = dias
    df["hora_venda"] = horas
    df["data_venda_br"] = datas_br
    df["data_venda_valida"] = datas_validas

    print("\nVerificacao das datas de venda:")
    print("Datas vazias:", datas_vazias)
    print("Datas invalidas:", datas_invalidas)
    print("Datas validas:", sum(datas_validas))

    print("\nExemplos de datas convertidas:")

    print(
        df[
            [
                "data_venda",
                "data_venda_br",
                "ano_venda",
                "mes_venda",
                "dia_venda",
                "hora_venda"
            ]
        ].head(5)
    )

    return df, anos, meses, datas_validas


# FUNCAO 8 - Mostrar o resumo geral

def mostrar_resumo(
    df,
    quantidade_invalida,
    preco_ausente,
    preco_negativo,
    pedidos_com_problema
):
    """Mostrar os principais resultados da analise."""

    total_cancelados = (
        df["status_pedido"] == "Cancelado"
    ).sum()

    print("\nResumo geral:")
    print("Total de pedidos:", len(df))
    print("Total de pedidos cancelados:", total_cancelados)
    print("Quantidades invalidas:", quantidade_invalida.sum())
    print("Precos ausentes:", preco_ausente.sum())
    print("Precos negativos:", preco_negativo.sum())

    print(
        "Pedidos afetados por problemas numericos:",
        pedidos_com_problema.sum()
    )


# FUNCAO 9 - Contar pedidos por canal

def contar_pedidos_por_canal(df):
    """Contar pedidos em cada canal reconhecido."""

    canais_reconhecidos = ["Mercado", "Loja física", "Web"]

    df_canais = df[
        df["canal_venda"].isin(canais_reconhecidos)
    ]

    print("\nPedidos por canal de venda:")
    print(df_canais["canal_venda"].value_counts())

    print(
        "Registros excluidos por canal nao reconhecido:",
        len(df) - len(df_canais)
    )


# FUNCAO 10 - Contar pedidos por ano e mes

def contar_pedidos_por_mes(df, anos, meses, datas_validas):
    """Contar pedidos agrupados por ano e mes."""

    anos_meses = []

    for i in range(len(df)):

        if datas_validas[i]:
            periodo = f"{int(anos[i])}-{int(meses[i]):02d}"
            anos_meses.append(periodo)

        else:
            anos_meses.append(None)

    df["ano_mes"] = anos_meses

    df_datas_validas = df[df["data_venda_valida"]]

    print("\nPedidos por ano e mes:")

    print(
        df_datas_validas["ano_mes"]
        .value_counts()
        .sort_index()
    )

    print(
        "Registros excluidos por data de venda invalida ou vazia:",
        len(df) - len(df_datas_validas)
    )


# PROGRAMA PRINCIPAL
# Sprint 1 - Leitura e verificacao inicial

df = carregar_dados("halloween_vendas.csv")

print("Quantidade de linhas e colunas:")
print(df.shape)

print("\nColunas do arquivo:")
print(df.columns.tolist())

print("\nPrimeiros tres registros:")
print(df.head(3))

mostrar_qualidade_dados(df)

(
    quantidade_invalida,
    preco_ausente,
    preco_negativo,
    pedidos_com_problema
) = verificar_problemas_numericos(df)


# Sprint 2 - Limpeza e padronizacao

print("\nCanais de venda encontrados:")
print(df["canal_venda"].value_counts(dropna=False))

df = padronizar_categorias(df)
df = padronizar_canais(df)


# Sprint 3 - Investigacao dos dados

investigar_entregas(df)


# Sprint 4 - Tratamento das datas

df, anos, meses, datas_validas = padronizar_datas_venda(df)


# Sprint 5 - Resumos finais

mostrar_resumo(
    df,
    quantidade_invalida,
    preco_ausente,
    preco_negativo,
    pedidos_com_problema
)

contar_pedidos_por_canal(df)

contar_pedidos_por_mes(
    df, anos, meses, datas_validas
)
