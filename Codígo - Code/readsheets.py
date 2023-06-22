import pandas as pd
from tkinter import messagebox
from tkinter import *
class LendoPlanilha:

    def __int__(self):
        self.planilha = None
        self.colunas = None

    def ler_planilha(self, local_planilha, coluna):
        try:
            df = pd.read_excel(local_planilha)
            self.planilha = df
            self.colunas = self.planilha.columns
            self.verificar_colunas(coluna, local_planilha, self.colunas)
            numeros = self.planilha[coluna]
            print(self.colunas)
            return numeros
        except ValueError:
            messagebox.showerror('Formato Inválido.', 'Verifique o formato do arquivo.')
            arquivo_selecionado = Label(text='Nenhum arquivo selecionado', bg='#A4FFC8', fg='black',
                                        font='-weight bold -size 7')
            arquivo_selecionado.place(x=365, y=175)

    def salvar_planilha(self, numeros, situacao, mensagem):
        novo_df = pd.DataFrame()
        novo_df['Numeros'] = numeros
        novo_df['Situação'] = situacao
        novo_df['Mensagem'] = mensagem
        novo_df.to_excel('Planilha.xlsx', index=False)
        print('Planilha gerada')

    def verificar_colunas(self, nome_da_coluna, local, colunas):
        if nome_da_coluna not in colunas:
            messagebox.showerror(title='Coluna inválida', message='Coluna não existe na base de dados.')
        else:
            messagebox.showinfo(title='CARREGANDO PLANILHA', message=f'A planilha foi carregada com sucesso.\n'
                                                                     f'Escreva a mensagem no campo '
                                                                     f'"Mensagem" e envie')
            arquivo_selecionado = Label(text=local, bg='#A4FFC8', fg='black', font='-weight bold -size 7')
            arquivo_selecionado.place(x=365, y=175)
        return nome_da_coluna
