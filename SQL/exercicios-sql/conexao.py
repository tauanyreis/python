import sqlite3

conexao = sqlite3.connect('exercicios_sql.db')
cursor = conexao.cursor()

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).

# cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')


# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Carlos", 28, "Engenharia")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Bianca", 22, "Medicina")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "José", 35, "Administração")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Ana", 40, "Direito")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Marcia", 30, "Ciência da Computação")')


# 3. Consultas Básicas 
# Escreva consultas SQL para realizar as seguintes tarefas:

# a) Selecionar todos os registros da tabela "alunos".

# dados = cursor.execute('SELECT * FROM alunos')


# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.

# dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')


# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

# dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome')


# d) Contar o número total de alunos na tabela.

# dados = cursor.execute('SELECT COUNT(*) FROM alunos')


# 4. Atualização e Remoção

# a) Atualize a idade de um aluno específico na tabela.

# cursor.execute('UPDATE alunos SET idade="26" WHERE nome="Bianca"')


# b) Remova um aluno pelo seu ID.

# cursor.execute('DELETE FROM alunos where id=3')


# 5. Criar uma Tabela e Inserir Dados

# cursor.execute('CREATE TABLE clientes (id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')
# dados = cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(1, "Ricardo", 29, 1500.5)')
# dados = cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(2, "Fernanda", 26, 2300.75)')
# dados = cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(3, "José", 35, 1800.0)')
# dados = cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(4, "Ana", 40, 2100.25)')
# dados = cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(5, "Marcia", 30, 500.1)')


# 6. Consultas e Funções Agregadas
# Escreva consultas SQL para realizar as seguintes tarefas:

# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.

# dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')


# b) Calcule o saldo médio dos clientes.

# dados = cursor.execute('SELECT AVG(saldo) FROM clientes')


# c)Encontre o cliente com o saldo máximo.

#dados = cursor.execute('SELECT nome, saldo FROM clientes ORDER BY saldo DESC LIMIT 1')


# d) Conte quantos clientes têm saldo acima de 1000

# dados = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')


# 7. Atualização e Remoção com Condições

# a) Atualize o saldo de um cliente específico.

# dados = cursor.execute('UPDATE clientes SET saldo="3800.0" WHERE nome="Marcia"')


# b)Remova um cliente pelo seu ID

# dados = cursor.execute('DELETE FROM clientes where id=1')


# 8. Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes". Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

# cursor.execute('CREATE TABLE compras (id INT PRIMARY KEY, client_id INT, produto VARCHAR(100), valor REAL, FOREIGN KEY (client_id) REFERENCES clientes(id));')
# dados = cursor.execute('INSERT INTO compras (id, client_id, produto, valor) VALUES (1, 5, "Notebook", 3500.00)')
# dados = cursor.execute('INSERT INTO compras (id, client_id, produto, valor) VALUES (2, 4, "Smartphone", 2000.50)')
# dados = cursor.execute('INSERT INTO compras (id, client_id, produto, valor) VALUES (3, 3, "Cafeteira", 150.75)')
# dados = cursor.execute('INSERT INTO compras (id, client_id, produto, valor) VALUES (4, 2, "Mesa de escritório", 500.00)')
# dados = cursor.execute('INSERT INTO compras (id, client_id, produto, valor) VALUES (5, 1, "Monitor", 800.99)')
# dados = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM compras INNER JOIN clientes ON compras.client_id = clientes.id')


for alunos in dados:
    print(alunos)


conexao.commit()
conexao.close