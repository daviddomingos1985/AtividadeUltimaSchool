'''
Criar, atualizar e excluir um TODO;
Criar,atualizar e excluir categorias;
Listar todos os afazeres de um dia específico;
Listar todas as categorias;Marcar uma tarefa como concluída.

'''


import sqlite3
conexao = sqlite3.connect('atividade.sqlite3')
cursor = conexao.cursor()

print('Insira os dados dos funcionarios: ')

nome = input('Qual o nome do funcionario? ')
cpf = input('Qual o CPF do funcionario? ')

valores = [nome, cpf]

sql_inserir = 'insert into Dados_funcionarios (nome, cpf) values (?, ?)'

cursor.execute(sql_inserir, valores)
conexao.commit()
conexao.close()