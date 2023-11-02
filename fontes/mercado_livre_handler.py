from df_handler import DfHandler
from environments import * 


#Data Frame de dados de entrada Mercado Livre
class DfMlInput(DfHandler):
    def __init__(self) -> None:
        super().__init__(file_name=TABELA_ML, 
                        sheet_name=SHEET_ANUNCIOS,
                        header_lines=range(0, 4))
    
    def remove_variations(self):
        self.drop(self[self['VARIATION_ID'].notna()].index, inplace=True)


#Data Frame de dados de saida Mercado Livre
class DfMlOutput(DfHandler):

    def __init__(self) -> None:
        super().__init__(file_name=TABELA_CONTROLE_PRECOS, 
                        sheet_name=SHEET_CONTROLE_PRECOS,
                        header_lines=range(0, 1))


class MLHandler():
    def __init__(self, df_input, df_output) -> None:
        self.df_ml_input = df_input
        self.df_ml_input = df_output
