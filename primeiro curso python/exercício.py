dados = {'nome': 'bob', 'idade': 23, 'cidade': 'cascavel'}
dados.update({'idade': 28}) 
#ou dados['idade'] = 28
dados.update({'profissao': 'jornaleiro'})
dados.pop('idade')
print('nome' in dados)