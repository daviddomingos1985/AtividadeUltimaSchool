'''

Crie um programa em Python que gere tabelas para uma aplicação de gerenciamento de tarefas. 
As tabelas devem compreender as seguintes funcionalidades:
As tarefas devem ser divididas em “categorias”;
Uma tarefa deve ter nome, data, categoria e status de conclusão (se foi realizada ou não); 
As restrições/relacionamentos devem fazer sentido.

'''

import sqlite3


conexao = sqlite3.connect(gerenciador_tarefas.sqlite3)

cursor  = conexao.cursor()

sql = '''
CREATE TABLE gerenciador_tarefas (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	tarefas TEXT(150),
	catergorias TEXT(150),
	data_das_tarefas TEXT(10)
);
CREATE TABLE tarefas (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome_das_tarefas TEXT(300),
	status_de_conclusao TEXT,
	CONSTRAINT tarefas_FK FOREIGN KEY (id) REFERENCES gerenciador_tarefas(id)
);
'''

cursor.execute(sql)
conexao.commit()
conexao.close()