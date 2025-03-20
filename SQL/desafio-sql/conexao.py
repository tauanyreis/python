import sqlite3

conexao = sqlite3.connect('desafio_sql.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
# cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
# cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

# cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
# cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
# cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')

# cursor.execute('DROP TABLE produtos')
# cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(1, "Isadora", "França", "isa@gmail.com", 123456)')
# cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(2, "Maria", "Salvador", "isa@gmail.com", 123456)')
# cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(3, "José", "Curitiba", "isa@gmail.com", 123456)')
# cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(4, "Marcia", "São Paulo", "isa@gmail.com", 123456)')
#cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES(8, "Cynthia", "Inglaterra", "cy@gmail.com")')

# cursor.execute('DELETE FROM usuario where id=1')
# cursor.execute('UPDATE usuario SET endereco="Minas Gerais" WHERE nome="José"')

# ORDER BY e DESC
# dados = cursor.execute('SELECT * FROM usuario ORDER BY nome, id DESC')

# LIMIT e DISTINCT
# dados = cursor.execute('SELECT * FROM usuario LIMIT 3')
# dados = cursor.execute('SELECT DISTINCT * FROM usuario LIMIT 3') 
 
# GROUP BY e HAVING
#dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id>3')
# Não dá para trabalhar com a clausula WHERE utilizando GROUP BY
# WHERE é utilizada antes do processo de agregação do GROUP BY e o HAVING depois do processo de agregação

# JOIN's
# JOIN - INNER JOIN
# dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id')

# JOIN - LEFT JOIN
# dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.nome = gerentes.nome')

# JOIN - RIGHT JOIN
# dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerentes ON usuario.nome = gerentes.nome')

# JOIN - FULL JOIN
# dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerentes ON usuario.nome = gerentes.nome')


# SUB-CONSULTAS
# dados = cursor.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerentes)')
for usuario in dados:
    print(usuario)

conexao.commit()
conexao.close