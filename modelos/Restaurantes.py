from modelos.avaliacao import Avaliacao

class Restaurante:
    """
    Representa um restaurante com suas informações básicas, avaliações e status de atividade.

    Attributes:
        restaurantes (list): Lista de todas as instâncias de Restaurante criadas.
        _nome (str): Nome do restaurante.
        _categoria (str): Categoria do restaurante (em letras maiúsculas).
        _ativo (bool): Indica se o restaurante está ativo ou não.
        _avaliacao (list): Lista de objetos Avaliacao associados ao restaurante.

    Methods:
        __init__(self, nome, categoria): Construtor da classe.
        __str__(self): Retorna uma representação em string do restaurante.
        listar_restaurantes(cls): Imprime uma lista formatada de todos os restaurantes.
        media_avaliacoes(self): Calcula a média das avaliações do restaurante.
        ativo(self): Retorna um emoji indicando o status de atividade do restaurante.
        alternar_status(self): Alterna o status de ativo para inativo e vice-versa.
        receber_avaliacao(self, cliente, nota): Adiciona uma nova avaliação ao restaurante.
    """
    restaurantes = []
    def __init__(self, nome, categoria):
    
        """
        Inicializa uma nova instância de Restaurante.
        Args:
        nome (str): Nome do restaurante.
        categoria (str): Categoria do restaurante.
    """
        
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        """
    Retorna uma representação em string do restaurante.

    Returns:
        str: Uma string formatada com o nome, categoria, avaliação média e status do restaurante.
    """
    
        return f'{self._nome}, {self._categoria}, {self.ativo}'

    @classmethod
    def listar_restaurantes(cls):
        """
    Imprime uma lista formatada de todos os restaurantes cadastrados.
    
    O decorador @classmethod transforma um método em um método de classe. Isso significa que ele pertence à classe e não a uma instância da classe. Ele recebe a classe como primeiro argumento (tradicionalmente chamado de cls).
    """
    
        print(f'{'Nome do restaurante'.ljust(25)}   {'Categoria'.ljust(25)}{'Avaliação'.ljust(25)}{'Status'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)}   {restaurante._categoria.ljust(25)} {str(restaurante.media_avaliacoes).ljust(25)} {restaurante.ativo}')
        print()
    
    @property
    def media_avaliacoes(self):
        """
    Calcula a média das avaliações do restaurante.

    Returns:
        float: A média das avaliações, arredondada para uma casa decimal.
        
    O decorador @property em Python transforma um método em um atributo. Isso significa que você pode acessar esse método como se fosse uma simples variável, mas por trás ele está executando um código mais complexo.
    """
    
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas/quantidade_de_notas, 1)
        return media
            
    @property
    def ativo(self):
        
        """
    Retorna um emoji indicando o status de atividade do restaurante.

    Returns:
        str: '✅' se o restaurante estiver ativo, '❌' caso contrário.
    """

        return '✅' if self._ativo else '❌'
    
    def alternar_status(self):
        """
    Alterna o status de ativo para inativo e vice-versa.
    """
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        """
    Adiciona uma nova avaliação ao restaurante.

    Args:
        cliente (str): Nome do cliente.
        nota (int): Nota da avaliação.
    """
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
        