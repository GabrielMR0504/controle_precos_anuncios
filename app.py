# Puxar informações via api do bling 
# Atualizar planilha de saida com dados
# Puxar informações da planilha do mercado livre
# Atualizar planilha de saida com os dados
import os
from dotenv import load_dotenv
load_dotenv()
import pandas as pd

def main():
    insere_dados_planilha()

def insere_dados_planilha():
    df_input = pd.read_excel(os.environ['TABELA_ML'], sheet_name=os.environ['SHEET_ANUNCIOS'])
    df_output = pd.read_excel(os.environ['TABELA_CONTROLE_PRECOS'], sheet_name=os.environ['SHEET_CONTROLE_PRECOS'])

    for index, row in df_input.iterrows():
        item_id = row['ITEM_ID']
        matching_rows = df_output[df_output['Código ML'] == item_id]
        if len(matching_rows) == 1:
            matching_row_index  = matching_rows.index[0]   
            update_row(matching_row_index, row, df_output)
            
def update_row(index, row, df):
    df.at[index, 'SKU'] = row['SKU']
    df.at[index, 'TITLE'] = row['Título']
    df.at[index, 'MARKETPLACE_PRICE'] = row['Status']
    df.at[index, 'SHIPPING_METHOD_MARKETPLACE'] = row['Taxa de Comissão (%)']
    df.at[index, 'SKU'] = row['Taxa de Comissão Fixa']
    df.at[index, 'SKU'] = row['Frete Incluso']
    df.at[index, 'SKU'] = row['Preço sem promoção']


if __name__ == '__main__':
    main()


