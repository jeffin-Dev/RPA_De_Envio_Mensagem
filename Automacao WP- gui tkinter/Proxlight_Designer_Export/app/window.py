from tkinter import *
from tkinter import ttk
from functiondriver import Navegador
from tkinter import messagebox
from datails import Details
from tkinter.filedialog import askopenfilename
from readsheets import LendoPlanilha

driver = Navegador()
detalhes = Details()
df = LendoPlanilha()


class EnvioDeWhatsapp():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("720x439")
        self.window.configure(bg = "#b3f0d3")
        detalhes.fixar_window_centro(self.window)
        self.numeros = []


        self.canvas = Canvas(
            self.window,
            bg = "#b3f0d3",
            height = 439,
            width = 720,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"background.png")
        self.background = self.canvas.create_image(
            361.5, 219.5,
            image=self.background_img)


        self.opcoes= ['Contato(s)','Upload de planilha']
        # Criando combobox opcoes
        self.combobox_var = StringVar()
        self.combobox_opcoes = ttk.Combobox(values=self.opcoes, textvariable=self.combobox_var,
                                            state="readonly", width=20)
        self.combobox_opcoes.place(x=465, y=100)
        self.valores_combobox()



        # Caixa de text mensagem
        self.img_caixa_texto = PhotoImage(file = f"img_textBox0.png")
        self.img_caixa_texto = self.canvas.create_image(
            541.5, 310.5,
            image = self.img_caixa_texto)
        self.mensagem_para_enviar = Text(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)
        self.mensagem_para_enviar.place(
            x = 416, y = 254,
            width = 251,
            height = 111)

        # Botao "Enviar'
        self.img_botao = PhotoImage(file = f"img0.png")
        self.botao_enviar = Button(
            image = self.img_botao,
            borderwidth = 5,
            highlightthickness = 2,
            bg= '#62D975',
            relief = "flat")
        self.botao_enviar.place(
            x = 484, y = 382,
            width = 116,
            height = 37)


        self.botao_fechar = Button(text='valor', bg= "#62D975", width=6, anchor='n',
                                   command=self.fechar_aplicacao)
        self.botao_fechar.place(x=657, y=407)

        self.window.resizable(False, False)
        self.window.mainloop()

    def valores_combobox(self, *args):
        self.combobox_var.trace('w', self.valores_combobox)
        if 'Contato(s)' in self.combobox_opcoes.get():
            self.limpar_opcoes()
            label_numeros = Label(text='Escreva o(s) número(os) abaixo.', bg='#A4FFC8', fg='black',
                                 font='-weight bold -size 9')
            label_numeros.place(x=445,
                                y=127)

            self.entrada_numero = Text(height=1, width=20)
            self.entrada_numero.place(x=445, y=148)

            butao_numeros = Button(text='Carregar Numeros(s)',
                                  bg='#62D975',fg='black', font='-weight bold -size 9', command=self.numeros_carregados)
            butao_numeros.place(x=460,
                               y=200)

            separador_labol = Label(text='Separe-os com VÍRGULA', width=35, anchor='w',
                                    bg='#A4FFC8', fg='black', font='-weight bold -size 9')
            separador_labol.place(x=460, y=175)


        elif 'Upload de planilha' in self.combobox_opcoes.get():
            self.limpar_opcoes()
            arquivo = Label(text='Nenhum arquivo selecionado.',
                                    bg='#A4FFC8', fg='black', font='-weight bold -size 7')
            arquivo.place(x=365, y=175)
            butao_upload= Button(text='Carregar Planilha',
                                    bg='#62D975', fg='black', font='-weight bold -size 9', command= self.selecionar_arquivo)
            butao_upload.place(x=480,
                               y=132)


    def numeros_carregados(self):
        numeros_cru = self.entrada_numero.get('1.0', END).strip(' ')
        numeros_list = numeros_cru.split(',')
        for numeros in numeros_list:
            numeros = numeros.strip()
            self.numeros.append(numeros)
        print (self.numeros)
        mensagem_n_carregador = messagebox.showinfo(title='CARREGANDO NÚMEROS', message='Os números foram carregados com sucesso!')
        numeros_label = Label(text='Os numeros carregados são: {}'.format(self.numeros))
        numeros_label.place(x=10,
                            y=10)
    def limpar_opcoes(self):
        label_limpar = Label(height=7, width=40, bg='#A4FFC8')
        label_limpar.place(x=360,
                            y=127)


    def selecionar_arquivo(self):
        arquivo = askopenfilename(title='Selecionar planilha')
        if arquivo:
            arquivo_selecionado = Label(text=arquivo,
                                 bg='#A4FFC8', fg='black', font='-weight bold -size 8')
            arquivo_selecionado.place(x=365, y=175)

            mostrar_numeros = Label(text=f'{df.ler_planilha(arquivo)}', bg='#A4FFC8', fg = 'black',
                                    font='-weight bold -size 9')
            mostrar_numeros.place(x=90,
                                  y=170)

        else:
            label_arquivo_n_selecionado = Label(text='Nenhum arquivo selecionado', width=50, anchor='w',
                                 bg='#A4FFC8', fg='black', font='-weight bold -size 7')
            label_arquivo_n_selecionado.place(x=365, y=175)



    def fechar_aplicacao(self):
        mensagem = messagebox.askquestion(title='Encerrando sistema', message='Deseja realmente sair?')
        if 'no' in mensagem:
            pass
        else:
            self.window.destroy()




if "__main__" == __name__:

    app = EnvioDeWhatsapp()