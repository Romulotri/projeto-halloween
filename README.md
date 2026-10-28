# Projeto Halloween — Análise de Vendas

## 1. Objetivo

Analisar 1.500 pedidos fictícios da loja Festa em Cena usando Python e Pandas, verificando a qualidade dos dados e comparando os pedidos por canal de venda e período.

## 2. Arquivos

- `main.py`: código da análise.
- `halloween_vendas.csv`: base de dados utilizada.

## 3. Tratamento dos dados

O programa verifica valores ausentes, tipos de dados, quantidades e preços inválidos. Também padroniza categorias e canais de venda, investiga pedidos sem data de entrega e valida as datas de venda, preservando o texto original.

Foram encontradas 7 quantidades inválidas, 12 preços ausentes e nenhum preço negativo. Ao todo, 19 pedidos apresentaram pelo menos um desses problemas. Na coluna de categorias, 18 valores vazios foram preenchidos com `sem categoria`.

## 4. Principais resultados

- **Canais:** Web teve 666 pedidos (44,4%), Loja física teve 551 (36,7%) e Mercado teve 283 (18,9%).
- **Período:** outubro foi o mês com mais pedidos nos dois anos analisados: 393 em 2024 e 410 em 2025, aumento de 17 pedidos.
- **Entregas:** 143 pedidos não tinham data de entrega. Desses, 109 estavam cancelados e 34 tinham outros status.
- **Datas de venda:** 1.496 datas foram consideradas válidas e 4 inválidas.

Os pedidos por canal incluem todos os status. A contagem mensal considera as datas de venda válidas. Portanto, os resultados representam registros da base, não necessariamente vendas concluídas ou receita.

## 5. Como executar

É necessário ter Python e Pandas instalados. Mantenha `main.py` e `halloween_vendas.csv` na mesma pasta. No terminal, execute:

```bash
python main.py
```

## 6. Conclusão

A análise identificou problemas de qualidade dos dados e diferenças no volume de pedidos entre canais e meses. Os resultados mostram a importância de validar e padronizar os dados antes de tirar conclusões. Em projetos de Machine Learning, essa preparação é importante, mas também é necessário escolher e avaliar adequadamente o modelo para reduzir problemas como overfitting e underfitting.