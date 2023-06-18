from tkinter import *
from tkinter import ttk
from functiondriver import Navegador
from tkinter import messagebox
from datails import Details
from tkinter.filedialog import askopenfilename
from readsheets import LendoPlanilha
from tkinter.simpledialog import askstring

driver = Navegador()
detalhes = Details()
df = LendoPlanilha()


class EnvioDeWhatsapp:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("720x439")
        self.window.title('Robô do ZAP')
        self.window.configure(bg="#b3f0d3")
        detalhes.fixar_window_centro(self.window)
        self.numeros = []
        self.canvas = Canvas(
            self.window,
            bg="#b3f0d3",
            height=439,
            width=720,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x = 0, y = 0)
        self.background_img = PhotoImage(file = f"background.png")
        self.background = self.canvas.create_image(
            361.5, 219.5,
            image=self.background_img)
        self.opcoes = ['Contato(s)', 'Upload de planilha']
        # Criando combobox opcoes
        self.combobox_var = StringVar()
        self.combobox_opcoes = ttk.Combobox(values=self.opcoes, textvariable=self.combobox_var,
                                            state="readonly", width=20)
        self.combobox_opcoes.place(x=465, y=100)
        self.valores_combobox()
        # Caixa de text mensagem
        self.img_caixa_texto = PhotoImage(file=f"img_textBox0.png")
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
            command= self.enviar_mensagem,
            borderwidth = 5,
            highlightthickness = 2,
            bg= '#62D975',
            relief = "flat")
        self.botao_enviar.place(
            x = 484, y = 382,
            width = 116,
            height = 37)
        self.botao_fechar = Button(text='Encerrar', bg="#62D975", width=6, anchor='n',
                                   command=self.fechar_aplicacao)
        self.botao_fechar.place(x=657, y=407)
        self.papelpreto = Label(text='', bg='black', height=14, width=36)
        self.papelpreto.place(x=53, y=56)
        self.recados_importantes()
        self.window.resizable(False, False)
        self.window.mainloop()

    def recados_importantes(self):
        texto_aviso = Label(text='''
RECADOS IMPORTANTES
--------------------------------------------------------------
O Whatsaap tem api própia, esse sistema foi\nfeito para\nmeios didádicos e para estudos.\nNão envie +50 mensagens por dia. 
Use por sua conta e risco.\nSistema feito por Jefferson Roberto.\nTodos os direitos reservados.
jefferson.dev.contato@gmail.com
--------------------------------------------------------------
Para saber como usar, acesse o documento\nchamado "Como me usar"\nSe encontra na pasta deste aplicativo.
↳----------------------------------------------------------↲''', bg='#B3F0E5', fg='black',
                         font='-weight bold -size 8', )
        texto_aviso.place(x=55, y=58)

    def enviar_mensagem(self):
        driver.enviar_mensagens(self.numeros, self.mensagem_para_enviar.get('1.0', END))
        df.salvar_planilha(self.numeros, driver.pegar_situacao(), self.mensagem_para_enviar.get('1.0', END))
        messagebox.showinfo(title='Planilha Gerada', message='Planilha gerada na área de trabalho com sucesso.')
        self.numeros = self.numeros.clear()

    def valores_combobox(self, *args):
        self.combobox_var.trace('w', self.valores_combobox)
        if 'Contato(s)' in self.combobox_opcoes.get():
            self.limpar_opcoes()
            label_numeros = Label(text='Escreva o(s) número(os) abaixo.', bg='#A4FFC8', fg='black',
                                  font='-weight bold -size 9')
            label_numeros.place(x=445,
                                y=122)
            self.entrada_numero = Text(height=1, width=29)
            self.entrada_numero.place(x=420, y=148)
            butao_numeros = Button(text='Carregar Numeros(s)',
                                  bg='#62D975',fg='black', font='-weight bold -size 9', command=self.carregar_numeros)
            butao_numeros.place(x=472,
                               y=195)
            separador_labol = Label(text='Separe-os com VÍRGULA', width=30, anchor='w',
                                    bg='#A4FFC8', fg='black', font='-weight bold -size 9')
            separador_labol.place(x=465, y=170)
        if 'Upload de planilha' in self.combobox_opcoes.get():
            self.limpar_opcoes()
            arquivo = Label(text='Nenhum arquivo selecionado.',
                                    bg='#A4FFC8', fg='black', font='-weight bold -size 7')
            arquivo.place(x=365, y=175)
            butao_upload= Button(text='Carregar Planilha', bg='#62D975', fg='black', font='-weight bold -size 9',
                                 command=self.selecionar_arquivo)
            butao_upload.place(x=486,
                               y=132)

    def carregar_numeros(self):
        self.numeros_label = Label(text='', bg='#B3F0E5',
                                      font='-weight bold -size 8')
        self.numeros_label.place(x=32,
                            y=10)
        if '9' in self.entrada_numero.get('1.0', END):
            numeros_cru = self.entrada_numero.get('1.0', END).strip(' ')
            numeros_list = numeros_cru.split(',')
            mensagem_n_carregador = messagebox.showinfo(title='NÚMEROS CARREGADOS',
                                                        message='Os números foram carregados com sucesso!\nEscreva a mensagem e envie.')
            for numeros in numeros_list:
                numeros = numeros.strip()
                self.numeros.append(numeros)
        else:
            alerta = messagebox.showerror(title='NENHUM NÚMERO ENCONTRADO', message='Digite algum número')
        print(self.numeros)
    def limpar_opcoes(self):
        label_limpar = Label(height=7, width=45, bg='#A4FFC8')
        label_limpar.place(x=360, y=127)

    def selecionar_arquivo(self):
        arquivo = askopenfilename(title='Selecionar planilha')
        if arquivo:
            coluna = askstring('Coluna', 'Qual o nome da coluna que os números se encontra?')
            if coluna:
                self.numeros = df.ler_planilha(arquivo, coluna)

                # for numero in numeros:
                #     numero = str(numero).strip()
                #     self.numeros.append(numero)
                # print (self.numeros)

                arquivo_selecionado = Label(text=arquivo, bg='#A4FFC8', fg='black', font='-weight bold -size 7')
                arquivo_selecionado.place(x=365, y=175)
                messagebox.showinfo(title='CARREGANDO PLANILHA', message=f'Coluna: {coluna}.\nA planilha foi carregada '
                                                                         f'com sucesso!! Escreva a mensagem no campo '
                                                                         f'"Mensagem" e envie')
            else:
                messagebox.showerror(title='ERRO DE COLUNA', message='Nenhuma coluna selecionada.')
        else:
            label_arquivo_n_selecionado = Label(text='Nenhum arquivo selecionado', width=50, anchor='w',
                                                      bg='#A4FFC8', fg='black', font='-weight bold -size 7')
            label_arquivo_n_selecionado.place(x=365, y=175)
            label_inf = Label(text='', bg='#A4FFC8',
                                fg='black', font='-weight bold -size 7', anchor='w', width=55)
            label_inf.place(x=365, y=200)

    def fechar_aplicacao(self):
        mensagem = messagebox.askquestion(title='Encerrando sistema', message='Deseja realmente sair?')
        if 'no' in mensagem:
            pass
        else:
            self.window.destroy()


if "__main__" == __name__:

    app = EnvioDeWhatsapp()