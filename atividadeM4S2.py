def decorator_imprimir(funcao):
   
    def mensagem(*args, **kwargs):
       
        capital, taxa, tempo = args
        
        
        result = funcao(*args, **kwargs)
        
       
        return print(f"CAPITAL: {capital}, TAXA: {taxa}, TEMPO: {tempo}, RESULTADO: {result}")
    return mensagem

@decorator_imprimir
def juros_simples(capital, taxa, tempo):
   
    return capital * (taxa / 100) * tempo
