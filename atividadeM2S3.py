'''
 Utilizando o comando INSERT, insira mais dois novos fornecedores:
 “Padaria do Pão” e “Marcenaria Martelo”, com os ids 3 e 4 respectivamente, e crie também os endereços;
- Atualize o endereço do fornecedor com id = 2 para “Rua dos Peixes, 26” com o comando UPDATE;
- Selecione todos os registros da tabela fornecedor com o comando SELECT;
- Selecione todos os registros da tabela fornecedor que tenham a coluna produto igual a Carnes;
- Remova o fornecedor que tem o id = 1 com o comando DELETE.

'''

CREATE TABLE fornecedor (
    id INT,
    nome VARCHAR(150) NOT NULL,
    endereco VARCHAR(150),
    produtos VARCHAR(20)
);

INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (1, 'Empresa de Leite ParmaLeite', 'Rua dos Leites, 23', 'leite');
INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (2, 'Peixaria Abril', 'Rua dos Leites, 25', 'peixe');
INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (3, 'Açougue Legal', 'Rua dos Leites, 30', 'carnes');
INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (4, 'Açougue Novo', 'Rua dos Leites, 35', 'carnes');
INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (5, 'Padaria do Pão', 'Rua dos Pães, 35', 'Pães');
INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (5, 'Marcenaria Martelo', 'Rua dos Martelos, 35', 'Ferramentas');


UPDATE fornecedor SET endereco = “Rua dos Peixes, 26” WHERE id = 2

SELECT * from fornecedor;

SELECT * FROM fornecedor where = 'carnes'

delete from fornecedor where id = 1
