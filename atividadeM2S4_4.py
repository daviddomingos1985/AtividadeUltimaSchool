'''
Criar, atualizar e excluir um TODO;
Criar,atualizar e excluir categorias;
Listar todos os afazeres de um dia específico;
Listar todas as categorias;Marcar uma tarefa como concluída.

'''


import sqlite3
conexao = sqlite3.connect('atividade.sqlite3')
cursor = conexao.cursor()

sql = 'select tarefas from Tarefas where data = current_date'

consulta = cursor.execute(sql)
for resultado in consulta:
    print (resultado)

conexao.commit()
conexao.close()