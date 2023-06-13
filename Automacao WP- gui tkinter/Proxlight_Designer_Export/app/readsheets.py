import pandas as pd

class LendoPlanilha:
    def ler_planilha(self, local_planilha):
        df = pd.read_csv(local_planilha, sep=';', encoding='latin-1')
        numeros = df['numeros']
        return numeros

