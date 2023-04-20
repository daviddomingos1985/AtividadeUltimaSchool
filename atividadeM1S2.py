'''
Crie uma aplicação que calcule o valor total que o Sr. João possui 
em moedas de real (R$) no caixa. 
A aplicação deve imprimir o valor total em reais (R$) 
e pode-se utilizar ponto flutuante para representar o valor 
com duas casas decimais no momento que for imprimir o valor na tela.

'''

moeda5 = 0.05
moeda10 = 0.10
moeda25 = 0.25
moeda50 = 0.50
moeda1 = 1.00

quantidade5 = float(input('digite a quantidade de moedas de 5 centavos: '))
quantidade10 = float(input('digite a quantidade de moedas de 10 centavos: '))
quantidade25 = float(input('digite a quantidade de moedas de 25 centavos: '))
quanatidade50 = float(input('digite a quantidade de moedas de 50 centavos: '))
quantidade1 = float(input('digite a quantidade de moedas de 1 real: '))

resultado1 = (moeda5 * quantidade5)
resultado2 = (moeda10 * quantidade10)
resultado3 = (moeda25 * quantidade25)
resultado4 = (moeda50 * quanatidade50)
resultado5 = (moeda1 * quantidade1)


print('valor em moedas e 5: ', resultado1)
print('valor em moedas e 5: ', resultado2)
print('valor em moedas e 5: ', resultado3)
print('valor em moedas e 5: ', resultado4)
print('valor em moedas e 5: ', resultado5)

resultado_final = (resultado1 + resultado2 + resultado3 + resultado4 + resultado5)

print ('o valor total em moedas é de',resultado_final,'reais.')
