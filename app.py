# Puxar informações via api do bling 
# Atualizar planilha de saida com dados
# Puxar informações da planilha do mercado livre
# Atualizar planilha de saida com os dados

import pandas as pd
from environments import * 
import unidecode

def main():
    insere_dados_planilha()


def insere_dados_planilha():
    df_input = pd.read_excel(PRECO_TAXA_FIXA, sheet_name=SHEET_ANUNCIOS)
    df_output = pd.read_excel(TABELA_CONTROLE_PRECOS, sheet_name=SHEET_CONTROLE_PRECOS)

    for index, row in df_input.iterrows():
        item_id = row['ITEM_ID']
        matching_rows = df_output[df_output['Código ML'] == item_id]
        if len(matching_rows) == 1:
            matching_row_index  = matching_rows.index[0]   
            update_row(matching_row_index, row, df_output)
        
        elif len(matching_rows) < 1:
            # TODO: Adiciona linha nova na tabela
            pass
        else:
            # TODO: Exclui linha repetida 
            pass


def update_row(index, row, df):
    df.at[index, 'SKU'] = row['SKU']
    df.at[index, 'Título'] = row['TITLE']
    df.at[index, 'Status'] = row['STATUS']
    df.at[index, 'Taxa de Comissão (%)'] = row['FEE_PER_SALE_MARKETPLACE']
    preco = row['MARKETPLACE_PRICE']     
    df.at[index, 'Taxa de Comissão Fixa'] = corrige_taxa_fixa(preco) 

    df.at[index, 'Frete Incluso'] = corrige_frete_incluso(row['SHIPPING_METHOD_MARKETPLACE'])
    df.at[index, 'SKU'] = row['Preço sem promoção']


def corrige_taxa_fixa(preco):
    """
    Responsável por determinar se tem taxa fixa.
    Retorno: 0.00 ou 5.00
    """
    if preco <= PRECO_TAXA_FIXA:
        return 5.00
    else:
        return 0.00


def corrige_frete_incluso(tipo_entrega):
    """
    Responsável por determinar se o frete está incluso ou não.
    Retorno: 'Sim' ou 'Não'
    """
    try:
        tipo_entrega = unidecode(tipo_entrega.strip()).upper()
    
    except Exception as e:
        print(e)
        

    if tipo_entrega in ['MERCADO ENVIOS GRATIS']:
        return 'Sim'
    elif tipo_entrega in ['MERCADO ENVIOS POR CONTA DO COMPRADOR', 'MERCADO ENVIOS POR MI CUENTA']:
        return 'Não'
    else:
        'Erro'

if __name__ == '__main__':
    main()