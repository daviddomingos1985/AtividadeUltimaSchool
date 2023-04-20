'''
Criar, atualizar e excluir um TODO;
Criar,atualizar e excluir categorias;
Listar todos os afazeres de um dia específico;
Listar todas as categorias;Marcar uma tarefa como concluída.

'''

import sqlite3
import datetime

conexao = sqlite3.connect('atividade.sqlite3')
cursor = conexao.cursor()

print('Insira os dados das tarefas a serem executadas')

nome_id = input('Insira o ID do funcionario a qual sera designada a tarefa: ')
data = datetime.date.today()
quantidade_de_tarefas = input('insira a quantidade de tarefas: ')
quantidade_de_tarefas = int(quantidade_de_tarefas)

for i in range(quantidade_de_tarefas):
    tarefas = input('Insira a Tarefa: ')
    valores = [nome_id, data, tarefas]

    sql_tarefa = 'insert into tarefas (nome_id, data, tarefas) values (?, ?, ?)'

cursor.execute(sql_tarefa, valores)
conexao.commit()
conexao.close()