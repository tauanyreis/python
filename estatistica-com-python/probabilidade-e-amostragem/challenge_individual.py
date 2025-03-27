import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom
import math

# Carregar os dados
df = pd.read_csv(r'C:\Users\Administrador\python\estatistica-com-python\probabilidade-e-amostragem\populacao_brasileira.csv')

# 1. Considere pessoas fluentes em inglês, qual a probabilidade complementar? Ou seja, qual a probabilidade de escolhermos uma pessoa aleatória e ela não ser fluente em inglês. Considere fluente quem tem o nível avançado.
fluentes = len(df[df['nível de proficiência em inglês'] == 'Avançado'])
print(f"1. {1 - (fluentes/len(df)):.4f}")

# 2. Se uma pessoa escolhida aleatoriamente for de Alagoas ou do Pará, qual é a probabilidade de ela ter uma renda superior a 5 mil reais?
al_para = df[df['estado'].isin(['AL','PA'])]
print(f"2. {len(al_para[al_para['renda'] > 5000])/len(al_para):.4f}")

# 3. Descubra a probabilidade de uma pessoa, residente no estado do Amazonas, ter ensino superior completo (considerando apenas a escolaridade classificada como 'Superior'). Qual a probabilidade da quinta pessoa amazonense que você conversar ter ensino superior completo?
amazonas = df[df['estado'] == 'AM']
prob = len(amazonas[amazonas['escolaridade'] == 'Superior'])/len(amazonas)
prob_quinta = binom.pmf(5, 5, prob)  # Probabilidade binomial para a 5ª pessoa
print(f"3. {prob:.4f} {prob_quinta:.4f}")

# 4. Considerando a renda das pessoas do nosso conjunto, podemos dizer que a renda de uma pessoa brasileira está na sua maioria em que faixa (faça faixa de 1.500 reais)? Qual é a sua função densidade de probabilidade?
faixas = np.arange(0, df['renda'].max()+1500, 1500)
plt.hist(df['renda'], bins=faixas, density=True, edgecolor='black')
plt.title('Distribuição de Renda por Faixas de R$1.500')
plt.xlabel('Faixa de Renda (R$)')
plt.ylabel('Densidade de Probabilidade')
plt.show()
print(f"4. {pd.cut(df['renda'], bins=faixas).value_counts().idxmax()}")

# 5. Calcule a média e a variância da renda da amostra. Depois faça a distribuição normal, inclua o gráfico.
media, var = df['renda'].mean(), df['renda'].var()
x = np.linspace(df['renda'].min(), df['renda'].max(), 100)
plt.plot(x, norm.pdf(x, media, np.sqrt(var)), 'r-', lw=2)
plt.title('Distribuição Normal da Renda')
plt.xlabel('Renda (R$)')
plt.ylabel('Densidade de Probabilidade')
plt.show()
print(f"5. {media:.2f} {var:.2f}")

# 6. Primeiro considere a probabilidade encontrada no nosso conjunto de pessoas com escolaridade de pós-graduação. Considerando a amostra de população brasileira com 1 milhão de habitantes, qual a probabilidade de encontrarmos 243 mil pessoas com pós-graduação?
p_pos = (df['escolaridade'] == 'Pós-graduação').mean()
print(f"6. {binom.pmf(243000, 1000000, p_pos):.10f}")

# 7. Somando as densidades nós temos a função de densida de acumulada. Considerando a coluna 'Escolaridade' faça a função de densidade acumulada discreta para cada nível de escolaridade.
fda = df['escolaridade'].value_counts(normalize=True).sort_index().cumsum()
print("7.")
print(fda.to_string())

# 8. Qual a margem de erro amostral da proporção populacional considerando a proporção de pessoas com nível de inglês intermediário?
p = (df['nível de proficiência em inglês'] == 'Intermediário').mean()
print(f"8. {1.96*math.sqrt(p*(1-p)/len(df)):.4f}")

# 9. Calcula a renda da população. Qual a probabilidade de encontrar 60 pessoas com uma renda mil reais superior à média?
p_acima = (df['renda'] > df['renda'].mean()+1000).mean()
print(f"9. {binom.pmf(60, len(df), p_acima):.10f}")

# 10. Qual é a probabilidade de escolhermos uma pessoa residente na região Sudeste que seja homem, tenha apenas ensino fundamental completo e possua renda mensal superior a 2 mil reais?
sudeste = df[df['estado'].isin(['SP','RJ','MG','ES'])]
filtro = sudeste[(sudeste['sexo']=='M') & (sudeste['escolaridade']=='Fundamental') & (sudeste['renda']>2000)]
print(f"10. {len(filtro)/len(sudeste):.4f}")