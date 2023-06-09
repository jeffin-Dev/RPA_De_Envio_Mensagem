from tkinter import ttk
from tkinter import Tk

class Details:

    def fixar_window_centro(self, janela):
        janela.update_idletasks()

        width = janela.winfo_width()
        frm_width = janela.winfo_rootx() - janela.winfo_x()
        win_width = width + 2 * frm_width

        height = janela.winfo_height()
        titlebar_height = janela.winfo_rooty() - janela.winfo_y()
        win_height = height + titlebar_height + frm_width

        x = janela.winfo_screenwidth() // 2 - win_width // 2
        y = janela.winfo_screenheight() // 2 - win_height // 2

        janela.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        janela.deiconify()
