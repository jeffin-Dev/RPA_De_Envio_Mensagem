import pandas as pd
from tkinter import messagebox
from tkinter.simpledialog import askstring

class LendoPlanilha:

    def __int__(self):
        self.planilha = None
        self.colunas = None

    def ler_planilha(self, local_planilha, coluna):
        df = pd.read_excel(local_planilha, sep=';', encoding='latin-1')
        self.planilha = df
        self.colunas = self.planilha.columns
        self.verificar_colunas(coluna)
        numeros = df[coluna]
        print(numeros)
        print (self.colunas)
        return numeros

    def salvar_planilha(self, numeros, situacao, mensagem):
        novo_df = pd.DataFrame()
        novo_df['Numeros'] = numeros
        novo_df['Situação'] = situacao
        novo_df['Mensagem'] = mensagem
        novo_df.to_excel(r'C:\Users\jeffe\Desktop\Planilha.xlsx', index=False)
        print('Planilha gerada')

    def verificar_colunas(self, nome_da_coluna):
        if nome_da_coluna not in self.colunas:
            messagebox.showerror(title='Coluna inválida', message='Coluna não existe na base de dados.')
        return nome_da_coluna



