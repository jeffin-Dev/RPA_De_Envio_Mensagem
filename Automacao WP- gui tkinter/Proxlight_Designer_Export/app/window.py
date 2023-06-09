from tkinter import *
from tkinter import ttk
from functionwindow import Navegador
from tkinter import messagebox
from datails import Details

driver = Navegador()
detalhes = Details()

class EnvioDeWhatsapp():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("720x439")
        self.window.configure(bg = "#b3f0d3")
        detalhes.fixar_window_centro(self.window)
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


        self.opcoes= ['Contato(s)', 'Upload de planilha']


        # Criando combobox opcoes

        self.combobox_var = StringVar()
        self.combobox_opcoes = ttk.Combobox(values=self.opcoes, textvariable=self.combobox_var,
                                            state="readonly", width=20)
        self.combobox_opcoes.place(x=465, y=100)
        self.valor_combobox(self.combobox_var)


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
            # command= driver.cliquei_no_link()
            image = self.img_botao,
            borderwidth = 5,
            highlightthickness = 2,
            bg= '#62D975',
            relief = "flat")
        self.botao_enviar.place(
            x = 484, y = 382,
            width = 116,
            height = 37)


        self.botao_fechar = Button(text='Fechar', bg= "#62D975", width=6, anchor='n',
                                   command=self.fechar_aplicacao)
        self.botao_fechar.place(x=657, y=407)

        self.window.resizable(False, False)
        self.window.mainloop()


    def valor_combobox(self, *args):
        self.combobox_var.trace('w', self.valor_combobox)
        if 'Contato(s)' in self.combobox_opcoes.get():
            inf_contatos = Label(text='Escreva o(s) número(os) abaixo.', bg='#B3F0D3', fg='black',
                                 font='-weight bold -size 9')
            inf_contatos.place(x=445,
                               y=127)
            numero_s = Text(height=1,
                            width=20)
            numero_s.place(x=455,
                            y=150)
            separador_labol = Label(text='Separe-os com VÍRGULA',
                                    bg='#A4FFC8', fg='black', font='-weight bold -size 9')
            separador_labol.place(x=460, y=175)

        elif 'Upload de planilha' in self.combobox_opcoes.get():
            separador_labol = Label(text='fazer',
                                    bg='#A4FFC8', fg='black', font='-weight bold -size 9')
            separador_labol.place(x=460, y=175)

    def fechar_aplicacao(self):
        mensagem = messagebox.askquestion(title='Encerrando sistema', message='Deseja realmente sair?')
        if 'no' in mensagem:
            pass
        else:
            self.window.destroy()




if "__main__" == __name__:

    app = EnvioDeWhatsapp()