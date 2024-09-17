#5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
#errei, contei apenas quantas palavras eram :(
frase = 'A vida é como uma caixa de chocolates: você nunca sabe o que vai encontrar. Mas a aventura de descobrir é o que a torna tão deliciosa. E lembre-se: a felicidade não está no destino, mas na jornada.'
frase_dividida = frase.split()
print(len(frase_dividida))

#jeito certo
frase2 = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase2.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)