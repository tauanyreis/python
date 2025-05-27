import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats

# Carregar os dados
house_data = pd.read_csv(r'C:\Users\Administrador\Documents\WoMakersCode\Estatística - Correlação e Regressão\kc_house_data.csv')
car_price_data = pd.read_csv(r'C:\Users\Administrador\Documents\WoMakersCode\Estatística - Correlação e Regressão\car_price.csv')

# Análises com kc_house_data.csv

# 1. Codifique e exiba a matriz de correlação entre as variáveis numéricas.
# Além disso, qual é a correlação entre o preço (price) e o número de quartos (bedrooms)?
# Existe alguma diferença na correlação quando consideramos apenas casas com uma área total (sqft_living) superior a 2000 pés quadrados?
house_data_numeric = house_data.select_dtypes(include=[np.number])  # Selecionando variáveis numéricas
corr_matrix_house = house_data_numeric.corr()  # Calculando a matriz de correlação
print(corr_matrix_house)

# Correlação entre preço (price) e número de quartos (bedrooms)
correlation_price_bedrooms = house_data[['price', 'bedrooms']].corr().iloc[0, 1]
print(f"Correlação entre preço e número de quartos: {correlation_price_bedrooms}")

# Filtro para casas com sqft_living > 2000
house_data_filtered = house_data[house_data['sqft_living'] > 2000] 
correlation_price_bedrooms_filtered = house_data_filtered[['price', 'bedrooms']].corr().iloc[0, 1]
print(f"Correlação entre preço e número de quartos (sqft_living > 2000): {correlation_price_bedrooms_filtered}")

# 2. Existe alguma correlação entre o preço (price) e a área total da casa (sqft_living), considerando apenas casas com pelo menos dois banheiros (bathrooms)?
house_data_filtered_bathrooms = house_data[house_data['bathrooms'] >= 2]  # Filtro para pelo menos 2 banheiros
correlation_price_sqft_bathrooms = house_data_filtered_bathrooms[['price', 'sqft_living']].corr().iloc[0, 1]
print(f"Correlação entre preço e área total (sqft_living) com pelo menos 2 banheiros: {correlation_price_sqft_bathrooms}")

# 3. Como a quantidade de banheiros (bathrooms) influencia na correlação entre a área total da casa (sqft_living) e o preço (price)?
# Vamos calcular a correlação entre todas as três variáveis: bathrooms, sqft_living, price.
corr_bathrooms_sqft_price = house_data[['bathrooms', 'sqft_living', 'price']].corr()
print(f"Correlação entre quantidade de banheiros, área total e preço:\n{corr_bathrooms_sqft_price}")

# 4. Qual é a relação entre a condição da casa (condition) e o preço (price), considerando apenas casas com uma área total (sqft_living) superior a 3000 pés quadrados?
house_data_filtered_condition = house_data[house_data['sqft_living'] > 3000]  # Filtro para casas com sqft_living > 3000
correlation_condition_price = house_data_filtered_condition[['condition', 'price']].corr().iloc[0, 1]
print(f"Correlação entre condição da casa e preço (sqft_living > 3000): {correlation_condition_price}")

# 5. Existe alguma correlação entre a localização geográfica (lat, long) e o preço (price) para casas com pelo menos três quartos (bedrooms)?
house_data_filtered_bedrooms = house_data[house_data['bedrooms'] >= 3]  # Filtro para casas com pelo menos 3 quartos
correlation_lat_long_price = house_data_filtered_bedrooms[['lat', 'long', 'price']].corr()
print(f"Correlação entre localização (lat, long) e preço (≥3 quartos):\n{correlation_lat_long_price}")

# 6. Calcule a correlação entre uma variável categórica (waterfront) e uma variável numérica (price) usando ANOVA.
# 'waterfront' é uma variável categórica e 'price' é numérica.
waterfront_1 = house_data[house_data['waterfront'] == 1]['price']
waterfront_0 = house_data[house_data['waterfront'] == 0]['price']

# Verifica se há dados suficientes para realizar a ANOVA
if len(waterfront_1) > 1 and len(waterfront_0) > 1:
    anova_result = stats.f_oneway(waterfront_1, waterfront_0)  # Realizando ANOVA
    print(f"ANOVA - waterfront vs price: F = {anova_result.statistic:.2f}, p = {anova_result.pvalue:.4f}")
else:
    print("Amostras pequenas demais para realizar ANOVA.")

# Análises com car_price.csv

# 7. Codifique e exiba a Matriz de correlação para as variáveis numéricas e dê exemplos de correlações positivas, negativas e neutras.
car_price_data_numeric = car_price_data.select_dtypes(include=[np.number])  # Selecionando variáveis numéricas
corr_matrix_car = car_price_data_numeric.corr()  # Calculando a matriz de correlação
print(corr_matrix_car)

# Exemplo de correlações:
positive_corr = car_price_data[['Price', 'Year']].corr().iloc[0, 1]  # Correlação positiva
negative_corr = car_price_data[['Price', 'Kilometer']].corr().iloc[0, 1]  # Correlação negativa
neutral_corr = (
    car_price_data[['Price', 'Owner']].corr().iloc[0, 1]
    if 'Owner' in car_price_data.select_dtypes(include=[np.number]).columns
    else 'N/A'
)
print(f"Correlação positiva (Price vs Year): {positive_corr}")
print(f"Correlação negativa (Price vs Kilometer): {negative_corr}")
print(f"Correlação neutra (Price vs Owner): {neutral_corr}")

# 8. Codifique e exiba Gráficos de Dispersão para cada uma das variáveis numéricas em relação à variável de interesse (Price).
sns.pairplot(car_price_data[['Price', 'Kilometer', 'Year', 'Owner']])  # Gráficos de dispersão
plt.show()

# 9. Crie um modelo de Regressão Linear Simples, exiba a Tabela de Regressão e exiba o plot da Reta Estimada.
# Regressão Linear Simples: Price ~ Kilometer
X_car = pd.to_numeric(car_price_data['Kilometer'], errors='coerce').dropna()  # Variável independente
Y_car = pd.to_numeric(car_price_data['Price'], errors='coerce').dropna()  # Variável dependente
common_index = X_car.index.intersection(Y_car.index)  # Alinhando índices
X_car = X_car.loc[common_index]
Y_car = Y_car.loc[common_index]

X_car_with_const = sm.add_constant(X_car)  # Adicionando constante ao modelo
model_car = sm.OLS(Y_car, X_car_with_const).fit()  # Modelo de regressão linear
print(model_car.summary())  # Exibindo a tabela de regressão

# Plot da reta estimada
plt.scatter(X_car, Y_car, alpha=0.5)  # Dispersão dos dados
plt.plot(X_car, model_car.predict(X_car_with_const), color='red', linewidth=2)  # Reta estimada
plt.title('Reta Estimada - Regressão Linear Simples')
plt.xlabel('Kilometragem')
plt.ylabel('Preço')
plt.show()

# 10. Codifique e exiba o gráfico dos resíduos do modelo de Regressão Simples.
residuals = model_car.resid  # Resíduos do modelo
plt.scatter(X_car, residuals, alpha=0.5)  # Gráfico de dispersão dos resíduos
plt.axhline(0, color='red', linestyle='--')  # Linha no valor zero
plt.title('Resíduos - Regressão Linear Simples')
plt.xlabel('Kilometragem')
plt.ylabel('Resíduos')
plt.show()

# 11. Crie um modelo de Regressão Multivariada, exiba a Tabela de Regressão e exiba o gráfico dos resíduos do modelo.
# Regressão Linear Multivariada: Price ~ Kilometer + Year + Owner
X_car_multivariate = car_price_data[['Kilometer', 'Year', 'Owner']]  # Variáveis independentes
Y_car = car_price_data['Price']  # Variável dependente

# Converter para numérico e remover NaNs
X_car_multivariate = X_car_multivariate.apply(pd.to_numeric, errors='coerce').dropna()
Y_car = pd.to_numeric(Y_car, errors='coerce').dropna()

# Garantir que os índices estejam alinhados
common_index = X_car_multivariate.index.intersection(Y_car.index)
X_car_multivariate = X_car_multivariate.loc[common_index]
Y_car = Y_car.loc[common_index]

# Verificação final
if X_car_multivariate.empty or Y_car.empty:
    print("Erro: Dados insuficientes para a regressão multivariada.")
else:
    X_car_multivariate = sm.add_constant(X_car_multivariate)  # Adicionando constante
    model_car_multivariate = sm.OLS(Y_car, X_car_multivariate).fit()  # Modelo de regressão multivariada
    print(model_car_multivariate.summary())  # Exibindo a tabela de regressão

    # Gráfico dos resíduos
    residuals_multivariate = model_car_multivariate.resid  # Resíduos do modelo multivariado
    plt.scatter(Y_car, residuals_multivariate, alpha=0.5)  # Dispersão dos resíduos
    plt.axhline(0, color='red', linestyle='--')  # Linha no valor zero
    plt.title('Resíduos - Regressão Multivariada')
    plt.xlabel('Preço')
    plt.ylabel('Resíduos')
    plt.show()