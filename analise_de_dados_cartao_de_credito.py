import pandas as pd

tabela = pd.read_csv("/content/ClientesBanco.xls", encoding="latin1")
tabela = tabela.drop("CLIENTNUM", axis=1) # Drop exclui a coluna ClienteNum. A Axis é o eixo (1 é coluna, 0 é linha) 
display(tabela)

"""# Resumo da Planilha e os dados estatísticos da tabela"""

tabela = tabela.dropna() # dropna exclui todas as linhas em que há um valor é vazio
display(tabela.info())

display(tabela.describe().round(1)) # describe informa sobre os dados estatísticos de uma moldura de dados.

"""# Relação entre Clientes x Cancelamentos
8.499 Clientes e 1.627 Cancelados (16%)
"""

quantidade_categoria = tabela["Categoria"].value_counts() # value_counts contou os valores
display(quantidade_categoria)                             # 8.499 Clientes e 1.627 Cancelados

quantidade_categoria_percentual = tabela["Categoria"].value_counts(normalize=True) # normalize disse o quanto representa do total
display(quantidade_categoria_percentual)                                           # 16% Cancelados

"""# Descobrindo o motivo do cancelamento

1. A maioria dos cancelamentos está abaixo de R$ 3.000 em transações
2. A maioria dos cancelamentos estão aaixo de 60 transações, entre 30 a 50 transações é um ponto critico. Programa para usar mais de 80 vezes pode diminuir os cancelamentos
3. Quanto mais vezes o cliente entra em contato, maior a chance de cancelar. Pode haver um problema de suporte e relacionamento ao cliente









"""

import plotly.express as px

for coluna in tabela: # para cada coluna na tabela. Se fosse para linhas seria .index:
  grafico = px.histogram(tabela, x=coluna, color="Categoria") # x é coluna, y é linha
  grafico.show()
