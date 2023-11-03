# Puxar informações via api do bling 
# Atualizar planilha de saida com dados
# Puxar informações da planilha do mercado livre
# Atualizar planilha de saida com os dados

from src.mercado_livre_handler import DFMLInput, DFMLOutput, MLHandler

def main():
    update_dados_planilha()


def update_dados_planilha():
    df_input = DFMLInput()
    df_output = DFMLOutput()

    print(df_input.to_string)

    ml_handler = MLHandler(df_input, df_output)
    ml_handler.update_output()
    ml_handler.load_output_to_workbook()

if __name__ == '__main__':
    main()