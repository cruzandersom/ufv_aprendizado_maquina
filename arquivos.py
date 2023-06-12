import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)
from ambiente import ambiente

DIRETORIO = ambiente['DIRETORIO']
atividade = ambiente['atividade'][1]


class Arquivos:
    def __init__(self):
        self.diretorio = DIRETORIO
        self.atividade = atividade
        self.arquivo = self.diretorio + self.atividade
        self.__colunas = self.colunas
        self.__tipos = self.tipos

    def retornar_dataset(self):
        return pd.read_csv(self.arquivo)

    @property
    def colunas(self):
        return [(i, j) for i, j in enumerate(pd.read_csv(self.arquivo).columns)]

    @property
    def tipos(self):
        return pd.read_csv(self.arquivo).dtypes

    def converter_para_data(self, coluna: str, dayfirst: bool = True):
        return pd.to_datetime(coluna, dayfirst=dayfirst)

    def converter_para_inteiro(self, coluna: str):
        return pd.to_numeric(coluna, downcast='integer')

    def converter_para_decimal(self, coluna: str):
        return pd.to_numeric(coluna, downcast='float')

    def converter_para_string(self, df: pd.DataFrame, coluna: str):
        return df[coluna].astype(str)

    def remover_nulos_gerais(self, df: pd.DataFrame):
        return df.dropna(axis=0, how='any')

    def remover_nulos_coluna(self, df: pd.DataFrame, coluna: str):
        return df.dropna(axis=0, how='any', subset=[coluna])

    def remover_colunas(self, df: pd.DataFrame, colunas: list):
        return df.drop(columns=colunas)

    def preencher_na(self, df: pd.DataFrame, coluna: str, valor: str):
        return df[coluna].fillna(valor)


