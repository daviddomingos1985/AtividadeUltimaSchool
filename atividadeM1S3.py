'''
Crie uma função que, ao receber um número inteiro,
retorna se um número é par ou ímpar (utilizando **kwargs).

'''

def par_ou_impar (**kwargs):
    return()


numero = int(input('Me diga um numero: '))
resultado = numero % 2
if resultado == 0:
    print (f'o numero {numero} é par')
else:
    print(f'o numero {numero} é impar')
    
par_ou_impar()