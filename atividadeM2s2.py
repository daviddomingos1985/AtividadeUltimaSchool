'''

Crie um programa em Python que gere tabelas para uma aplicação de eventos. 
Elas devem compreender as seguintes funcionalidades:
Eventos devem ter título, data e local, além da referência ao organizador;
O organizador deve ter nome, email e cpf;
As restrições/relacionamentos devem fazer sentido.

'''


import sqlite3

conexao = sqlite3.connect(organizador_de_eventos.sqlite3)

cursor = conexao.cursor()

sql = '''
CREATE TABLE organizador_de_eventos (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome_evento TEXT(150),
	data_evento TEXT(10),
	local_evento TEXT(200),
	referencia_organizador TEXT(150)
);

CREATE TABLE cadastro_do_organizador (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT(150),
	"e-mail" TEXT(150),
	cpf TEXT(11),
	evento_id INTEGER,
	CONSTRAINT cadastro_do_organizador_UN UNIQUE (cpf),
	CONSTRAINT cadastro_do_organizador_FK FOREIGN KEY (id) REFERENCES organizador_de_eventos(id)
);
'''

cursor.execute(sql)
conexao.commit()
conexao.close()