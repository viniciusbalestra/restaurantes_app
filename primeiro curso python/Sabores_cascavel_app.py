import os

restaurantes = [{'nome':'Lasanha', 'categoria': 'Italiana', 'status': True}, 
                {'nome': 'Pastel', 'categoria': 'lanche', 'status': False}, 
                {'nome': 'Bolinho', 'categoria': 'doces', 'status': True}]


def exibir_nome_programa():
    '''Exibe o nome estilizado do programa'''
    
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░███████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝█████╗░░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗██╔══╝░░░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║███████╗██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░

░█████╗░░█████╗░░██████╗░█████╗░░█████╗░██╗░░░██╗███████╗██╗░░░░░
██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██║░░░██║██╔════╝██║░░░░░
██║░░╚═╝███████║╚█████╗░██║░░╚═╝███████║╚██╗░██╔╝█████╗░░██║░░░░░
██║░░██╗██╔══██║░╚═══██╗██║░░██╗██╔══██║░╚████╔╝░██╔══╝░░██║░░░░░
╚█████╔╝██║░░██║██████╔╝╚█████╔╝██║░░██║░░╚██╔╝░░███████╗███████╗
░╚════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚══════╝''')

def exibir_opcoes():
    '''Exibe opções que o usuário pode escolher
    Inputs:
    - Escolha entre opções de 1 a 4 para definir a ação.
    '''
    print('-' * 65)
    print('1. Cadastrar restaurante.')
    print('2. Listar restaurante.')
    print('3. Alterar status do restaurante.')
    print('4. Sair do app.\n')

def exibir_subtitulo(texto):
    '''Limpa a tela, define as configurações do subtítulo, e o define baseado na escolha do usuário no menu
    Inputs:
    - texto: str - o texto do subtitulo
    '''
    os.system('cls')
    print('=' * 52)
    print('|{:^50}|'.format(texto))
    print('=' * 52)
    print()

def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal 
    Outputs:
    - Retorna ao menu principal
    '''
    print()
    input('Digite uma tecla para voltar ao menu principal. ')
    main()

def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''  
    print('Opção inválida.\n')
    voltar_ao_menu_principal()

def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    
    print()
    exibir_subtitulo('PROGRAMA FINALIZADO')

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante, loop permite que cadastre quantos restaurantes desejar sem precisar voltar ao menu
    
    Inputs:
    - Nome do restaurante
    - Categoria
    - opção de continuar ou encerrar o cadastro de novos restaurantes

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    
    while True:
        
        exibir_subtitulo('CADASTRO DE NOVOS RESTAURANTES')
        
        nome_do_restaurante = str(input('Digite o nome do restaurante que deseja cadastrar: '))
        categoria = str(input(f'\nDigite o nome da categoria do restaurante: '))
        dados_restaurante = {'nome':nome_do_restaurante, 'categoria': categoria, 'status': False}
        restaurantes.append(dados_restaurante)
        
        frase_confirmacao_cadastro = f'Restaurante {nome_do_restaurante} cadastrado com sucesso!\n'
        print('-' * len(frase_confirmacao_cadastro),'\n')
        print(frase_confirmacao_cadastro)
        print('-' * len(frase_confirmacao_cadastro),'\n')
        resposta = str(input('Deseja cadastrar um novo restaurante?[S/N] '))[0].lower().strip()
        if resposta == 'n':
            break
    voltar_ao_menu_principal()
  
def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    
    exibir_subtitulo('LISTA DE RESTAURANTES CADASTRADOS')
    for restaurante in restaurantes:
        nome_restaurantes = restaurante['nome']
        categoria = restaurante['categoria']
        status = restaurante['status']
        if status == True:
            ativo = 'ativo'
        else:
            ativo = 'desativado'
        print('---' * 10,'\n')
        print(f'Nome: {nome_restaurantes}\nCategoria: {categoria}\nStatus: {ativo}\n')
    print('===' * 16,'\n')
    voltar_ao_menu_principal()

def alterar_status_restaurantes():
    ''' Altera o estado ativo/desativado de um restaurante,
    e mostra mensagem caso restaurante digitado não conste na lista
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    - Exibe mensagem de erro caso restaurante não conste na lista
    '''
    
    exibir_subtitulo('ALTERAR STATUS DO RESTAURANTE')
    nome_do_restaurante = str(input('Digite o nome do restaurante: '))
    
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['status'] = not restaurante['status']
            if restaurante['status'] == True:
                ativo = 'ativado'
            else:
                ativo = 'desativado'
            print('---' * 23,'\n')
            print(f'O restaurante {nome_do_restaurante.capitalize()} foi {ativo} com sucesso.\n')
            print('---' * 23,'\n')
            
    if not restaurante_encontrado:
        print('---' * 23,'\n')
        print('O restaurante não foi encontrado.\n')
        print('---' * 23,'\n')   
        
    voltar_ao_menu_principal()

def escolher_opcoes():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    
    try:
        opcao_escolhida = int(input('Qual é a sua opção: '))
        print('-' * 65)
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_status_restaurantes()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        
def main():
    ''' Função principal que inicia o programa '''
    
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()

