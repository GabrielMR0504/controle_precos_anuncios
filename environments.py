import os
from dotenv import load_dotenv
load_dotenv()

TABELA_ML = os.environ['TABELA_ML']
SHEET_ANUNCIOS = os.environ['SHEET_ANUNCIOS']
TABELA_CONTROLE_PRECOS = os.environ['TABELA_CONTROLE_PRECOS']
SHEET_CONTROLE_PRECOS = os.environ['SHEET_CONTROLE_PRECOS']

PRECO_TAXA_FIXA = 120