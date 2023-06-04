from tkinter import *
from functionwindow import Navegador
import os

caminho = os.getcwd()

driver = Navegador()

class EnvioDeWhatsapp:
    def __init__(self):
        self.window = Tk()
        self.window.title('Envio de mensagem pelo WhatsApp')
        self.window.geometry("720x439")
        self.window.configure(bg = "#d8d8d8")
        self.canvas = Canvas(
            self.window,
            bg = "#d8d8d8",
            height = 439,
            width = 720,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file=r'background.png')
        self.background = self.canvas.create_image(
            394.5, 228.0,
            image=self.background_img)

        self.entry0_img = PhotoImage(file = r'img_textBox0.png')
        self.entry0_bg = self.canvas.create_image(
            550.5, 287.5,
            image = self.entry0_img)

        self.mensagem_para_envio = Text(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)
        self.mensagem_para_envio.place(
            x = 425, y = 231,
            width = 255,
            height = 115)

        self.entry1_img = PhotoImage(file = r"img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(
            544.5, 158.0,
            image = self.entry1_img)

        self.telefone_para_envio = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)
        self.telefone_para_envio.place(
            x = 453, y = 145,
            width = 183,
            height = 26)

        self.img0 = PhotoImage(file =r"img0.png")
        self.botao_enviar = Button(
            text='Enviar',
            bg='#ACFFB9',
            fg='black',
            borderwidth = 5,
            highlightthickness = 5,
            command = self.cliando_em_enviar,
            relief = "flat")
        self.botao_enviar.place(
            x = 501, y = 371,
            width = 116,
            height = 37)

        self.window.resizable(False, False)
        self.window.mainloop()

    def cliando_em_enviar(self):
        driver.cliquei_no_link(self.telefone_para_envio.get(), self.mensagem_para_envio.get('1.0', END))


if '__main__' == __name__:
    a = EnvioDeWhatsapp()
