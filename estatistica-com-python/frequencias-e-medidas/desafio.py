# Importando as bibliotecas necessárias
import json
import zipfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Abrir e carregar o JSON dentro do ZIP
with zipfile.ZipFile("enem_2023.zip", "r") as z:
    with z.open("enem_2023.json") as f:
        data = json.load(f)

# Converter os dados para um DataFrame do pandas
df = pd.DataFrame(data)

# Verificar as colunas para garantir que "Sexo" exista
print("Colunas no DataFrame:", df.columns)

# Mapear os valores de "Sexo" para números
sexo_mapping = {"Homem": 0, "Mulher": 1, "Não identificado": 2}
df["Sexo"] = df["Sexo"].map(sexo_mapping)

# Realizar operações numéricas
summary = {
    "Linguagens": df["Linguagens"].max() - df["Linguagens"].min(),
    "Sexo": df["Sexo"].max() - df["Sexo"].min()
}

print(summary)

# Calcular amplitude (maior nota - menor nota) para cada disciplina
amplitude = {
    "Linguagens": df["Linguagens"].max() - df["Linguagens"].min(),
    "Ciências humanas": df["Ciências humanas"].max() - df["Ciências humanas"].min(),
    "Ciências da natureza": df["Ciências da natureza"].max() - df["Ciências da natureza"].min(),
    "Matemática": df["Matemática"].max() - df["Matemática"].min(),
    "Redação": df["Redação"].max() - df["Redação"].min()
}

# 1. Qual das disciplinas tem a maior amplitude de nota?

# Mostrar a disciplina com a maior amplitude
maior_amplitude = max(amplitude, key=amplitude.get)
print(f"A disciplina com a maior amplitude de nota é: {maior_amplitude}")

# 2. Qual é a média e a mediana para cada uma das disciplinas? (Lembre-se de remover todos os valores nulos quando considerar a mediana)

# Calcular média e mediana, removendo valores nulos para a mediana
media = df.mean()
mediana = df.dropna().median()

print("\nMédia das disciplinas:")
print(media)

print("\nMediana das disciplinas (sem valores nulos):")
print(mediana)

# 3. Considerando o curso de Ciência da Computação da UFPE, onde o peso cada uma das disciplinas ponderado:

# a. Redação - 2

# b. Matemática e suas Tecnologias - 4

# c. Linguagens, Códigos e suas Tecnologias - 2

# d. Ciências Humanas e suas Tecnologias - 1

# e. Ciências da Natureza e suas Tecnologias - 1

# Qual o desvio padrão e média das notas dos 500 estudantes mais bem colocados considerando esses pesos?

# Pesos para as disciplinas
pesos = {
    'Linguagens': 2,
    'Matemática': 4,
    'Redação': 2,
    'Ciências humanas': 1,
    'Ciências da natureza': 1
}

# Para calcular a média ponderada
df['Nota ponderada'] = (df['Linguagens'] * pesos['Linguagens'] + 
                         df['Matemática'] * pesos['Matemática'] + 
                         df['Redação'] * pesos['Redação'] + 
                         df['Ciências humanas'] * pesos['Ciências humanas'] + 
                         df['Ciências da natureza'] * pesos['Ciências da natureza']) / sum(pesos.values())

# Selecionando os 500 melhores estudantes
df_top_500 = df.nlargest(500, 'Nota ponderada')

# Média e desvio padrão ponderado para os 500 melhores
media_ponderada = df_top_500['Nota ponderada'].mean()
desvio_padrao_ponderado = df_top_500['Nota ponderada'].std()

print(f"Média ponderada dos 500 melhores estudantes: {media_ponderada}")
print(f"Desvio padrão ponderado dos 500 melhores estudantes: {desvio_padrao_ponderado}")

# 4. Se todos esses estudantes aplicassem para ciência da computação e existem apenas 40 vagas, qual seria a variância e média da nota dos estudantes que entraram no curso de ciência da computação?

# Selecionando os 40 melhores estudantes
df_top_40 = df.nlargest(40, 'Nota ponderada')

# Média e variância das notas dos 40 primeiros
media_top_40 = df_top_40['Nota ponderada'].mean()
variancia_top_40 = df_top_40['Nota ponderada'].var()

print(f"Média das notas dos 40 primeiros estudantes: {media_top_40}")
print(f"Variância das notas dos 40 primeiros estudantes: {variancia_top_40}")

# 5. Qual o valor do teto do terceiro quartil para as disciplinas de matemática e linguagens?

# Teto do terceiro quartil para Matemática
q3_matematica = df['Matemática'].quantile(0.75)

# Teto do terceiro quartil para Linguagens
q3_linguagens = df['Linguagens'].quantile(0.75)

print(f"Teto do terceiro quartil para Matemática: {q3_matematica}")
print(f"Teto do terceiro quartil para Linguagens: {q3_linguagens}")

# 6. Faça o histograma de Redação e Linguagens, de 20 em 20 pontos. Podemos dizer que são histogramas simétricos, justifique e classifique se não assimétricas?

import matplotlib.pyplot as plt

# Gerar histogramas
# plt.figure(figsize=(12, 6))

# Histograma de Redação
# plt.subplot(1, 2, 1)
# plt.hist(df['Redação'], bins=range(0, 1001, 20), edgecolor='black')
# plt.title('Histograma de Redação')
# plt.xlabel('Notas')
# plt.ylabel('Frequência')

# Histograma de Linguagens
# plt.subplot(1, 2, 2)
# plt.hist(df['Linguagens'], bins=range(0, 1001, 20), edgecolor='black')
# plt.title('Histograma de Linguagens')
# plt.xlabel('Notas')
# plt.ylabel('Frequência')

# plt.tight_layout()
# plt.show()

from scipy.stats import skew

# Calcular a assimetria para Redação e Linguagens
# assimetria_redacao = skew(df['Redação'], nan_policy='omit')
# assimetria_linguagens = skew(df['Linguagens'], nan_policy='omit')

# print(f"\nAssimetria de Redação: {assimetria_redacao}")
# print(f"Assimetria de Linguagens: {assimetria_linguagens}")

# Os histogramas de Redação e Linguagens apresentam leve assimetria positiva, com cauda à direita, indicando que as notas mais altas são menos frequentes. As distribuições podem ser consideradas relativamente simétricas.

# 7. Agora coloque um range fixo de 0 até 1000, você ainda tem a mesma opinião quanto a simetria? [plt.hist(dado, bins=_, range=[0, 1000])

# Gerar histogramas com range de 0 até 1000
# plt.hist(df['Redação'], bins=20, range=[0, 1000], alpha=0.5, label='Redação')
# plt.hist(df['Linguagens'], bins=20, range=[0, 1000], alpha=0.5, label='Linguagens')
# plt.legend()
# plt.show()

# Calcular a assimetria para Redação e Linguagens
assimetria_redacao = skew(df['Redação'].dropna())
assimetria_linguagens = skew(df['Linguagens'].dropna())

print(f"\nAssimetria de Redação: {assimetria_redacao}")
print(f"Assimetria de Linguagens: {assimetria_linguagens}")

# Após ajustar o range para 0 até 1000, a opinião sobre a simetria não muda. Ambas as distribuições ainda têm leve assimetria positiva, mas continuam sendo relativamente simétricas.

# 8. Faça um boxplot para as notas de Ciências da Natureza e Redação, analisando os quartis e identificando possíveis outliers. Utilize o método IQR (Intervalo Interquartílico) para essa análise.

# Calcular o IQR para Ciências da Natureza e Redação
# q1_ciencias_natureza = df['Ciências da natureza'].quantile(0.25)
# q3_ciencias_natureza = df['Ciências da natureza'].quantile(0.75)
# iqr_ciencias_natureza = q3_ciencias_natureza - q1_ciencias_natureza

# q1_redacao = df['Redação'].quantile(0.25)
# q3_redacao = df['Redação'].quantile(0.75)
# iqr_redacao = q3_redacao - q1_redacao

# Identificar limites superior e inferior para outliers
# limite_inferior_ciencias_natureza = q1_ciencias_natureza - 1.5 * iqr_ciencias_natureza
# limite_superior_ciencias_natureza = q3_ciencias_natureza + 1.5 * iqr_ciencias_natureza

# limite_inferior_redacao = q1_redacao - 1.5 * iqr_redacao
# limite_superior_redacao = q3_redacao + 1.5 * iqr_redacao

# Visualizar boxplot
# plt.figure(figsize=(10, 6))
# sns.boxplot(data=df[['Ciências da natureza', 'Redação']])

# Exibir limites para outliers
# print("Limite inferior e superior para Ciências da Natureza:", limite_inferior_ciencias_natureza, limite_superior_ciencias_natureza)
# print("Limite inferior e superior para Redação:", limite_inferior_redacao, limite_superior_redacao)

# Exibir o gráfico
# plt.title("Boxplot - Ciências da Natureza e Redação")
# plt.show()

# 9. Remova todos os outliers e verifique se eles são passíveis de alterar a média nacional significativamente? (considere significativamente um valor acima de 5%)

# Remover outliers para Ciências da Natureza e Redação
df_sem_outliers = df[
    (df['Ciências da natureza'] >= 288.65) & (df['Ciências da natureza'] <= 704.82) & 
    (df['Redação'] >= 317.19) & (df['Redação'] <= 955.27)
]

# Calcular a média antes e depois da remoção dos outliers
media_nacional_original = df[['Ciências da natureza', 'Redação']].mean().mean()
media_nacional_sem_outliers = df_sem_outliers[['Ciências da natureza', 'Redação']].mean().mean()

# Verificar a diferença percentual
diferenca_percentual = ((media_nacional_original - media_nacional_sem_outliers) / media_nacional_original) * 100

# Exibir os resultados
print(f"Média original: {media_nacional_original}")
print(f"Média sem outliers: {media_nacional_sem_outliers}")
print(f"Diferença percentual: {diferenca_percentual:.2f}%")

# A remoção dos outliers não alterou a média nacional de forma significativa. A diferença percentual entre a média original (568.55) e a média sem outliers (569.27) foi de apenas -0.13%, o que está abaixo do limite de 5%.

# 10. Considerando valores nulos, tente encontrar qual seria a melhor medida de tendência que pode substituir as notas nulas. Média, moda ou mediana? Substitua o valor por todos os três e diga qual delas altera menos a média geral e o desvio padrão.

# Calcular a média, moda e mediana para as disciplinas com valores não nulos
media_valores = df.mean()
moda_valores = df.mode().iloc[0]  # A moda é o valor mais frequente
mediana_valores = df.median()

# Substituir os valores nulos por média, moda e mediana
df_media_substituida = df.fillna(media_valores)
df_moda_substituida = df.fillna(moda_valores)
df_mediana_substituida = df.fillna(mediana_valores)

# Calcular a média e o desvio padrão para cada substituição
media_original = df.mean().mean()
desvio_padrao_original = df.std().mean()

# Média e desvio padrão após substituir os valores nulos por média
media_media = df_media_substituida.mean().mean()
desvio_padrao_media = df_media_substituida.std().mean()

# Média e desvio padrão após substituir os valores nulos por moda
media_moda = df_moda_substituida.mean().mean()
desvio_padrao_moda = df_moda_substituida.std().mean()

# Média e desvio padrão após substituir os valores nulos por mediana
media_mediana = df_mediana_substituida.mean().mean()
desvio_padrao_mediana = df_mediana_substituida.std().mean()

# Exibir os resultados
print(f"Média original: {media_original}")
print(f"Desvio padrão original: {desvio_padrao_original}")

print(f"\nMédia após substituir por média: {media_media}")
print(f"Desvio padrão após substituir por média: {desvio_padrao_media}")

print(f"\nMédia após substituir por moda: {media_moda}")
print(f"Desvio padrão após substituir por moda: {desvio_padrao_moda}")

print(f"\nMédia após substituir por mediana: {media_mediana}")
print(f"Desvio padrão após substituir por mediana: {desvio_padrao_mediana}")

# Substituindo valores nulos, a média e a mediana alteram pouco a média geral e o desvio padrão. A média mantém os valores mais próximos dos originais, com a menor alteração no desvio padrão. A moda altera mais significativamente a média e o desvio padrão. Portanto, a média é a melhor opção para substituir os valores nulos.