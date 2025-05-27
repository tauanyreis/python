# DESAFIO FINAL - MODELOS DE CLASSIFICAÇÃO E REGRESSÃO LOGÍSTICA

# Importações gerais
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# 1. UTILIZANDO O DATASET IRIS (iris.csv)

# a. FAÇA UMA ANÁLISE INICIAL SOBRE ESSE DATASET
iris = pd.read_csv("iris.csv")

print("Primeiras linhas do dataset Iris:")
print(iris.head())

print("\nInformações do dataset:")
iris.info()

print("\nDescrição estatística:")
print(iris.describe())

print("\nEspécies encontradas:", iris["Species"].unique())

# b. USE O BOXPLOT E O HISTOGRAMA PARA CARACTERIZAR AS PROPRIEDADES DE CADA UMA DAS ESPÉCIES EXISTENTES.
features = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']

for feature in features:
    plt.figure(figsize=(12, 5))

    # Boxplot por espécie
    plt.subplot(1, 2, 1)
    sns.boxplot(data=iris, x='Species', y=feature)
    plt.title(f'Boxplot de {feature}')

    # Histograma por espécie
    plt.subplot(1, 2, 2)
    sns.histplot(data=iris, x=feature, hue='Species', kde=True, element='step')
    plt.title(f'Histograma de {feature}')

    plt.tight_layout()
    plt.show()

# c. SOMENTE OLHANDO ESSES GRÁFICOS, É POSSÍVEL AFIRMAR QUE UMA OU MAIS PROPRIEDADES 
# (SEPAL_LENGTH, SEPAL_WIDTH, PETAL_LENGTH, PETAL_WIDTH) SÃO SUFICIENTES PARA DISTINGUIR AS ESPÉCIES?
# Sim, Petal_Length e Petal_Width são claramente suficientes para distinguir setosa das demais,
# e ajudam significativamente na distinção entre versicolor e virginica.

# d. APLIQUE A REGRESSÃO LOGÍSTICA PARA AVALIAR O MODELO DE CLASSIFICAÇÃO
le = LabelEncoder()
iris['Species_encoded'] = le.fit_transform(iris['Species'])

X = iris[features]
y = iris['Species_encoded']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# e. CALCULE A ACURÁCIA, PRECISÃO E RECALL
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, average='weighted')
rec = recall_score(y_test, y_pred, average='weighted')

print(f"\nMétricas do modelo - IRIS")
print(f"Acurácia: {acc:.4f}")
print(f"Precisão: {prec:.4f}")
print(f"Recall: {rec:.4f}")

# f. PLOTE A MATRIZ DE CONFUSÃO COM MATPLOTLIB OU SEABORN
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=le.classes_, yticklabels=le.classes_)
plt.title("Matriz de Confusão - Iris")
plt.xlabel("Previsto")
plt.ylabel("Real")
plt.show()

# 2. UTILIZANDO O DATASET LOAD_DIGITS

from sklearn.datasets import load_digits

# a. FAÇA UMA ANÁLISE INICIAL SOBRE ESSE DATASET
digits = load_digits()
X_digits = digits.data
y_digits = digits.target

print("\nNúmero de amostras:", X_digits.shape[0])
print("Número de colunas (pixels):", X_digits.shape[1])
print("Valores nulos:", pd.DataFrame(X_digits).isnull().sum().sum())
print("Tipos de dados:", pd.DataFrame(X_digits).dtypes.unique())

# b. APLIQUE A REGRESSÃO LOGÍSTICA PARA CONSTRUIR E AVALIAR O MODELO DE CLASSIFICAÇÃO
X_train_d, X_test_d, y_train_d, y_test_d = train_test_split(X_digits, y_digits, test_size=0.3, random_state=42)

model_digits = LogisticRegression(max_iter=10000)
model_digits.fit(X_train_d, y_train_d)
y_pred_d = model_digits.predict(X_test_d)

# c. CALCULE A ACURÁCIA, PRECISÃO E RECALL COM BASE NO DESEMPENHO DO MODELO
acc_d = accuracy_score(y_test_d, y_pred_d)
prec_d = precision_score(y_test_d, y_pred_d, average='weighted')
rec_d = recall_score(y_test_d, y_pred_d, average='weighted')

print(f"\nMétricas do modelo - DIGITS")
print(f"Acurácia: {acc_d:.4f}")
print(f"Precisão: {prec_d:.4f}")
print(f"Recall: {rec_d:.4f}")

# d. PLOTE A MATRIZ DE CONFUSÃO DOS RESULTADOS DO MODELO UTILIZANDO MATPLOTLIB OU SEABORN
cm_d = confusion_matrix(y_test_d, y_pred_d)
plt.figure(figsize=(8, 6))
sns.heatmap(cm_d, annot=True, fmt='d', cmap='Oranges')
plt.title("Matriz de Confusão - Digits")
plt.xlabel("Previsto")
plt.ylabel("Real")
plt.show()

# e. APLIQUE A REGRESSÃO LOGÍSTICA PARA AVALIAR O MODELO DE CLASSIFICAÇÃO DOS DÍGITOS DE 0 A 9 
# UTILIZANDO O CONJUNTO DE DADOS ESPECÍFICO PARA ESSE PROBLEMA (MNIST)
# -> A base `load_digits` já é para classificação de dígitos de 0 a 9

# f. CALCULE A ACURÁCIA, PRECISÃO E RECALL COM BASE NO DESEMPENHO DO MODELO PARA A CLASSIFICAÇÃO DOS DÍGITOS DE 0 A 9
# -> Já realizado nos passos anteriores usando `load_digits`

# g. PLOTE A MATRIZ DE CONFUSÃO DOS RESULTADOS DA CLASSIFICAÇÃO DOS DÍGITOS DE 0 A 9
# -> Também já realizado acima com seaborn