from tkinter import *
from tkinter import ttk
from functionwindow import Navegador
from options import Opcoes


driver = Navegador()
opcao = Opcoes()


class EnvioDeWhatsapp():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("720x439")
        self.window.configure(bg = "#b3f0d3")
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
        self.combobox_opcoes = StringVar()
        self.combobox_opcoes = ttk.Combobox(values=self.opcoes, textvariable = self.combobox_opcoes, state="readonly", width=20)
        opcao.opcao_escolhida(self.combobox_opcoes.get())
        self.combobox_opcoes.place(x= 465, y = 100)


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
            command = self.cliquei,
            bg= '#62D975',
            relief = "flat")
        self.botao_enviar.place(
            x = 484, y = 382,
            width = 116,
            height = 37)

        self.window.resizable(False, False)
        self.window.mainloop()


    def cliquei(self):
        print (self.combobox_opcoes.get())

if "__main__" == __name__:

    app = EnvioDeWhatsapp()