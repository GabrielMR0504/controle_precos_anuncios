# Puxar informações via api do bling 
# Atualizar planilha de saida com dados
# Puxar informações da planilha do mercado livre
# Atualizar planilha de saida com os dados

from environments import * 
from openpyxl import load_workbook 
from openpyxl.utils.dataframe import dataframe_to_rows
from fontes.mercado_livre_handler import DfMlInput, DfMlOutput, MLHandler


def main():
    update_dados_planilha()


def update_dados_planilha():
    df_input = DfMlInput()
    df_output = DfMlOutput()

    print(df_input.to_string)


    df_output.remove_duplicates()

    ml_handler = MLHandler(df_input, df_output)
    ml_handler.atualiza_output()

    # df_values is the DataFrame with the data to save
    wb = load_workbook(TABELA_CONTROLE_PRECOS)
    sheet = wb.active
    df_columns = df_output.shape[1]
    # I use 2 with enumerate to save the header column of the excel sheet
    for r, row in enumerate(dataframe_to_rows(df_output, index=False, header=False), 2):
        for c in range(0, df_columns):
            sheet.cell(row=r, column=c + 1).value = row[c]
    wb.save(TABELA_CONTROLE_PRECOS)


if __name__ == '__main__':
    main()