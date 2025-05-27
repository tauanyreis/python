

# "Cadastrar produto e retornar"

# 1.rodar a função sem chamar
# 2.variáveis das funções não saem dela. Testar "produto".

def cadastrar_produto(produto):
    # produto = input('Digite o nome do produto que deseja cadastrar')
    produto = produto.casefold()
    produto = produto.strip()
    return produto

# produto_cadastrado = cadastrar_produto()

# print(produto)
nome_produto = (cadastrar_produto("biscoito"))
print(nome_produto)
