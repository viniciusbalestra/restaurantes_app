#criar links personalizados do whatsapp e enviar mensagens para cada cliente da planilha;

import os
import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep


#abrir planilha, pegar informação e guardar informacões;
caminho_completo = os.path.abspath('cliente.xlsx')
workbook = openpyxl.load_workbook('cliente.xlsx')
pagina_clientes = workbook['Planilha1']

for linha in pagina_clientes.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    data_vencimento = linha[2].value.strftime('%d/%m/%y')

    mensagem = (f'https://web.whatsapp.com/send?phone={telefone}&text=Ol%C3%A1%20%7B{nome}%7D,%20seu%20boleto%20vence'
                f'%20no%20dia%20%7B{data_vencimento}%7D,%20pague%20pelo%20link%20http://pagamentolink.com.br')
# criar links personalizados do whatsapp e enviar mensagens para cada cliente da planilha;

    webbrowser.open(mensagem)
    sleep(15)