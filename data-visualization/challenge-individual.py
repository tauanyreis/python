# Exercício Prático - Data Visualization em Python

# Importação das bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from statsmodels.tsa.seasonal import seasonal_decompose

# Desafio Prático 1: Visualizando Dados Diferentes

# 1. Carregar os dados de um arquivo CSV fornecido (saude.csv).
print("Iniciando Desafio 1")
df_saude = pd.read_csv('saude.csv')
print("Dados de saúde carregados:")
print(df_saude.head())
print("\n")

# 2. Criar um histograma da variável 'age' usando Matplotlib.
print("Gerando Histograma da Idade (Matplotlib)...")
plt.figure(figsize=(8, 6))
plt.hist(df_saude['age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribuição de Idade')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.grid(True)
plt.savefig('histograma_idade.png')
print("Histograma 'histograma_idade.png' salvo.")
plt.close() # Fecha a figura para não exibir no console interativo
print("\n")


# 3. Criar um gráfico de dispersão mostrando a relação entre 'height' e 'weight' usando Seaborn.
print("Gerando Gráfico de Dispersão Altura vs. Peso (Seaborn)...")
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_saude, x='height', y='weight', hue='gender', palette='viridis')
plt.title('Relação entre Altura e Peso')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.grid(True)
plt.savefig('dispersao_altura_peso.png')
print("Gráfico de dispersão 'dispersao_altura_peso.png' salvo.")
plt.close()
print("\n")

# 4. Criar um gráfico interativo de barras mostrando a contagem de indivíduos por 'gender' usando Plotly.
print("Gerando Gráfico de Barras Interativo por Gênero (Plotly)...")
gender_counts = df_saude['gender'].value_counts().reset_index()
gender_counts.columns = ['gender', 'count']
fig_bar_plotly = px.bar(gender_counts,
                        x='gender',
                        y='count',
                        title='Contagem de Indivíduos por Gênero',
                        labels={'gender': 'Gênero', 'count': 'Contagem'},
                        color='gender')
fig_bar_plotly.write_html("barras_genero_interativo.html")
print("Gráfico interativo 'barras_genero_interativo.html' salvo.")
print("Fim do Desafio 1\n")


# Desafio Prático 2: Séries Temporais

# 1. Carregar os dados de um arquivo CSV fornecido (vendas.csv).
print("Iniciando Desafio 2")
df_vendas = pd.read_csv('vendas.csv')
# CORREÇÃO: Convertendo a coluna 'date' (minúscula) para o formato datetime
df_vendas['date'] = pd.to_datetime(df_vendas['date'])
print("Dados de vendas carregados e processados:")
print(df_vendas.head())
print("\n")

# 2. Criar um gráfico de linhas das vendas ao longo do tempo usando Matplotlib.
print("Gerando Gráfico de Linhas de Vendas (Matplotlib)...")
plt.figure(figsize=(12, 6))
# CORREÇÃO: Usando 'date' e 'sales' (minúsculas)
plt.plot(df_vendas['date'], df_vendas['sales'], marker='o', linestyle='-')
plt.title('Vendas ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Vendas')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('vendas_ao_longo_do_tempo.png')
print("Gráfico de linhas 'vendas_ao_longo_do_tempo.png' salvo.")
plt.close()
print("\n")

# 3. Criar um gráfico de decomposição sazonal usando Seaborn (e statsmodels).
print("Gerando Gráfico de Decomposição Sazonal...")
# CORREÇÃO: Usando 'date' como índice
df_vendas_decomposicao = df_vendas.set_index('date')
# CORREÇÃO: Usando 'sales' para a decomposição
decomposicao = seasonal_decompose(df_vendas_decomposicao['sales'], model='additive', period=12)

fig_decomposicao = decomposicao.plot()
fig_decomposicao.set_size_inches(12, 8)
plt.tight_layout()
plt.savefig('decomposicao_sazonal.png')
print("Gráfico de decomposição 'decomposicao_sazonal.png' salvo.")
plt.close()
print("\n")


# 4. Criar um gráfico interativo que permita a exploração dos dados de vendas ao longo do tempo usando Plotly
print("Gerando Gráfico de Linhas Interativo de Vendas (Plotly)...")
# CORREÇÃO: Usando 'date' e 'sales' e ajustando os labels
fig_line_plotly = px.line(df_vendas,
                           x='date',
                           y='sales',
                           title='Vendas ao Longo do Tempo (Interativo)',
                           labels={'date': 'Data', 'sales': 'Vendas'})
fig_line_plotly.update_xaxes(rangeslider_visible=True)
fig_line_plotly.write_html("vendas_interativo.html")
print("Gráfico interativo 'vendas_interativo.html' salvo.")
print("Fim do Desafio 2")