from tkinter import *


def btn_clicked():
    print("Button Clicked")

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

        self.img_botao = PhotoImage(file = f"img0.png")
        self.botao_enviar = Button(
            image = self.img_botao,
            borderwidth = 5,
            highlightthickness = 2,
            command = btn_clicked,
            bg= '#62D975',
            relief = "flat")
        self.botao_enviar.place(
            x = 484, y = 382,
            width = 116,
            height = 37)

        self.window.resizable(False, False)
        self.window.mainloop()

if "__main__" == __name__:

    app = EnvioDeWhatsapp()