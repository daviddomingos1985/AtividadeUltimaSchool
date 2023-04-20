'''
Crie uma tabela chamada “cliente”. 
É necessário que ela tenha as seguintes colunas:

- ID
- NOME
- CPF
- DATA_CADASTRO
- ENDERECO


'''

CREATE TABLE cliente(
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOME TEXT(100),
	CPF TEXT(11),
	DATA_CADASTRO TEXT(20),
	ENDERECO TEXT(150)
    
);

insert into cliente values(1, "Danilo", "11111111111", "05/10/2022", "RIO TINTO");

select * from cliente;