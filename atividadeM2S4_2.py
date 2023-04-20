'''
Criar, atualizar e excluir um TODO;
Criar,atualizar e excluir categorias;
Listar todos os afazeres de um dia específico;
Listar todas as categorias;Marcar uma tarefa como concluída.

'''


import sqlite3

conexao = sqlite3.connect('atividade.sqlite3')
cursor = conexao.cursor()

print('Insira quais tarefas foram concluidas')

nome_id = input('Insira o ID do funcionario a qual a tarefa foi designada: ')

sql_id = 'select tarefas from Tarefas where nome_id = ?'
consulta = cursor.execute(sql_id, nome_id)
for resultado in consulta:
    print(resultado)


tarefas_concluidas = input('Para confirmar a execussão da tarefa escreva (tarefa concluida)! ')
valores = [tarefas_concluidas]

sql_tarefa = 'insert into Tarefas (tarefas_concluidas) values (?)'

cursor.execute(sql_tarefa, valores)
conexao.commit()
conexao.close()
