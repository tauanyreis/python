import pandas as pd
import numpy as np
import scipy.stats as stats

# Carregar os dados
df_ab = pd.read_csv(r"C:\Users\Administrador\Documents\WoMakersCode\Estatística - Testes de Hipóteses/experimento_test_ab.csv")
df_pacientes = pd.read_csv(r"C:\Users\Administrador\Documents\WoMakersCode\Estatística - Testes de Hipóteses/pacientes.csv")

# 1. Qual dos cenários tem a maior taxa de conversão?
taxa_conversao = df_ab.groupby('Versão_Página').apply(lambda x: x['Conversões'].sum() / len(x))
print("Taxa de Conversão por Cenário:\n", taxa_conversao)

# 2. Calcule qual o tamanho da amostra necessária para o desenvolvimento de um teste A/B
alpha = 0.05  # Nível de significância
beta = 0.2    # Poder de 80%
p1 = 0.105  # Taxa de conversão do cenário A (pode ser ajustado com base na base de dados)
p2 = 0.115  # Taxa de conversão do cenário B (10% de aumento)

# Cálculo do tamanho da amostra necessário
z_alpha = stats.norm.ppf(1 - alpha / 2)
z_beta = stats.norm.ppf(1 - beta)
tamanho_necessario = ((z_alpha * np.sqrt(2 * p1 * (1 - p1)) + z_beta * np.sqrt(p1 * (1 - p1) + p2 * (1 - p2)))**2) / (p2 - p1)**2
print(f"Tamanho da amostra necessário: {tamanho_necessario:.0f}")

# 3. A idade média das pessoas com problemas cardíacos é maior que 50 anos?
indices_amostra = [909, 751, 402, 400, 726, 39, 184, 269, 255, 769, 209, 715, 677, 381, 793, 697, 89, 280, 232, 756, 358, 36, 439, 768, 967, 699, 473, 222, 89, 639, 883, 558, 757, 84, 907, 895, 217, 224, 311, 348, 146, 505, 273, 957, 362]
amostra = df_pacientes.loc[df_pacientes.index.isin(indices_amostra), 'Idade']

# Teste t para verificar se a idade média é maior que 50 anos
t_stat, p_val = stats.ttest_1samp(amostra, 50)
print(f"p-valor para a idade média ser maior que 50 anos: {p_val}")

# 4. A amostra é dependente ou independente ao dividir os conjuntos entre pessoas com e sem condições de saúde adicionais?
print("A amostra é independente, pois estamos comparando dois grupos distintos.")

# 5. A pressão arterial média para pacientes com e sem condições de saúde adicionais é igual?
indices_saude_adicional = [690, 894, 67, 201, 364, 19, 60, 319, 588, 643, 855, 623, 530, 174, 105, 693, 6, 462, 973, 607, 811, 346, 354, 966, 943, 372]
amostra_saude_adicional = df_pacientes.loc[df_pacientes.index.isin(indices_saude_adicional), 'Pressao_Arterial']
amostra_sem_saude_adicional = df_pacientes.loc[~df_pacientes.index.isin(indices_saude_adicional), 'Pressao_Arterial']

# Teste t para comparar as médias de pressão arterial
t_stat, p_val = stats.ttest_ind(amostra_saude_adicional, amostra_sem_saude_adicional)
print(f"p-valor para comparar pressões arteriais médias: {p_val}")

# 6. Existe uma diferença significativa na pressão arterial média entre diferentes grupos étnicos?
etnias = df_pacientes['Etnia'].unique()
amostras_etnias = [df_pacientes[df_pacientes['Etnia'] == etnia]['Pressao_Arterial'] for etnia in etnias]
anova_stat, anova_p_val = stats.f_oneway(*amostras_etnias)
print(f"p-valor da ANOVA: {anova_p_val}")

# 7. Existe uma relação entre o sexo e as condições de saúde adicionais?
contingencia_sexo_saude = pd.crosstab(df_pacientes['Genero'], df_pacientes['Estado_Saude'])
chi2_stat, p_val_chi2, dof, expected = stats.chi2_contingency(contingencia_sexo_saude)
print(f"p-valor do teste Qui-quadrado: {p_val_chi2}")

# 8. Existe uma associação entre a idade dos pacientes e sua pressão arterial?
correlacao, p_val_correlacao = stats.pearsonr(df_pacientes['Idade'], df_pacientes['Pressao_Arterial'])
print(f"p-valor para a correlação entre idade e pressão arterial: {p_val_correlacao}")

# 9. Qual é o intervalo de confiança para a média da pressão arterial entre os pacientes com condições de saúde adicionais?
pacientes_com_condicoes = df_pacientes[df_pacientes['Estado_Saude'] == 'Com condições de saúde adicionais']

# Intervalo de confiança para a pressão arterial de pacientes com condições de saúde adicionais
conf_int_com_condicoes = stats.t.interval(
    0.95, 
    len(pacientes_com_condicoes['Pressao_Arterial'])-1, 
    loc=pacientes_com_condicoes['Pressao_Arterial'].mean(),
    scale=stats.sem(pacientes_com_condicoes['Pressao_Arterial'])
)
print(f"Intervalo de confiança para a pressão arterial (95%) dos pacientes com condições de saúde adicionais: {conf_int_com_condicoes}")

# 10. A distribuição da pressão arterial na população segue uma distribuição normal?
stat, p_val_normalidade = stats.shapiro(df_pacientes['Pressao_Arterial'])
print(f"p-valor do teste de normalidade (Shapiro-Wilk): {p_val_normalidade}")
if p_val_normalidade > 0.05:
    print("A distribuição da pressão arterial na população segue uma distribuição normal (não rejeitamos H0).")
else:
    print("A distribuição da pressão arterial na população não segue uma distribuição normal (rejeitamos H0).")