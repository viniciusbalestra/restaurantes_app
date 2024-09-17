from modelos.Restaurantes import Restaurante


restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_takaiama = Restaurante('Takaiama', 'Japonesa')

#avaliaçoes
restaurante_praca.receber_avaliacao('João', 8)
restaurante_praca.receber_avaliacao('Patricia', 7)
restaurante_praca.receber_avaliacao('Silvo', 10)

restaurante_takaiama.alternar_status()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()