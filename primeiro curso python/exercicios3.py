lista_de_numeros = [2, 4, 12, 3, 9, 5]
soma = 0
try:
    for numeros in lista_de_numeros:
        soma += numeros
    print(f'a soma dos números é {soma}')

except Exception as e:
    print(f"Ocorreu um erro: {e}")