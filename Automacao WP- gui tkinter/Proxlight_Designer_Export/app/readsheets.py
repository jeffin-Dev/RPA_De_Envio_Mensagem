import pandas as pd

class LendoPlanilha:
    def __int__(self):
        self.df = None

    def ler_planilha(self, local_planilha, coluna):
        df = pd.read_csv(local_planilha, sep=';', encoding='latin-1')
        self.df = df
        numeros = df[coluna]
        print(numeros)
        return numeros

    def salvar_planilha(self, numeros, situacao):
        novo_df = pd.DataFrame()
        novo_df['Numeros'] = numeros
        novo_df['Situação'] = situacao
        novo_df.to_excel(r'C:\Users\dakma\OneDrive\Área de Trabalho\rpa zap\Números enviados.xlsx', index=False)

