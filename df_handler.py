import pandas as pd


class DfHandler(pd.DataFrame):
    header_lines = None
    def __init__(self, file_name, sheet_name, header_lines) -> None:
        super().__init__(pd.read_excel(file_name, sheet_name))
        self.header_lines = header_lines 
    def remove_sub_header(self):
        self.drop(self.header_lines, inplace=True)
    
    def display_df(self):
        with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):print(self)
        
    # def filter_data(self, column, value):
        # Filtra o DataFrame com base em uma coluna e um valor
        # return self[self[column] == value]