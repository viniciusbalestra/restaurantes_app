import os
import openpyxl

def verificar_arquivo(caminho_arquivo):
    if os.path.exists(caminho_arquivo):
        return True
    else:
        return False
