# Relatório — Análise dos pedidos de Halloween

## Objetivo

Analisar 1.500 pedidos fictícios da loja Festa em Cena, registrados entre agosto e novembro de 2024 e 2025. O trabalho verifica a qualidade dos dados e compara os pedidos por canal de venda e período.

## Tratamento dos dados

A base foi lida com Pandas, sem alterar o arquivo CSV original. Na coluna `categoria`, 18 valores vazios foram preenchidos com “sem categoria” e 1.482 categorias não vazias tiveram o texto alterado durante a limpeza. Foram utilizados `.strip()`, `.lower()` e `re.sub()` para padronizar os textos.

A validação identificou 7 pedidos com quantidade inválida, 12 com preço unitário ausente e nenhum preço negativo. Ao considerar os registros afetados sem contar o mesmo pedido duas vezes, foram identificados 19 pedidos com problemas numéricos.

Os canais foram padronizados para Web, Loja física e Mercado, sem canais não reconhecidos. Na análise das datas de venda, 1.496 foram consideradas válidas e 4 inválidas. O texto original foi preservado, e das datas válidas foram extraídos ano, mês, dia e hora.

## Descoberta 1 — Canais de venda

O canal Web apresentou o maior volume, com 666 pedidos, equivalente a 44,4% do total. Loja física registrou 551 pedidos (36,7%) e Mercado, 283 (18,9%).

A diferença mostra que o canal Web concentra a maior parcela dos registros nesta base. Como a contagem inclui todos os status de pedido, ela não representa necessariamente vendas concluídas nem permite concluir qual canal é mais rentável.

## Descoberta 2 — Pedidos por período

Outubro foi o mês com mais pedidos nos dois anos analisados: 393 em outubro de 2024 e 410 em outubro de 2025. Houve aumento de 17 pedidos, aproximadamente 4,3%.

Essa comparação considera as datas de venda válidas e todos os status de pedido. Ela mostra uma diferença no volume registrado, mas não explica suas causas.

## Investigação das entregas

Foram encontrados 143 pedidos sem data de entrega. Desses, 109 estavam com status “Cancelado” e 34 tinham outros status. Portanto, a hipótese de que todos os pedidos sem data de entrega foram cancelados não foi confirmada.

## Conclusão e limitações

A análise mostra a importância de validar e padronizar os dados antes de compará-los. Os resultados se referem a uma base fictícia, incluem diferentes status de pedido e não permitem medir diretamente a receita ou a rentabilidade. Em Machine Learning, a preparação dos dados é uma etapa importante, mas a qualidade das previsões também depende da escolha do modelo e de sua avaliação, considerando riscos como overfitting e underfitting.