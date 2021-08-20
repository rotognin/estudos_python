# Lidando com diferentes temas de sistema

import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # root window
        self.title('Demonstração de temas para as janelas')
        self.geometry('400x300')
        self.style = ttk.Style(self)

        # label
        label = ttk.Label(self, text = 'Nome: ')
        label.grid(column = 0, row = 0, padx = 10, pady = 10,  sticky = 'w')
        # entry
        textbox = ttk.Entry(self)
        textbox.grid(column = 1, row = 0, padx = 10, pady = 10,  sticky = 'w')
        # button
        btn = ttk.Button(self, text = 'Mostrar')
        btn.grid(column = 2, row = 0, padx = 10, pady = 10,  sticky = 'w')

        # radio button
        self.selected_theme = tk.StringVar()
        theme_frame = ttk.LabelFrame(self, text = 'Temas')
        theme_frame.grid(padx = 10, pady = 10, ipadx = 20, ipady = 20, sticky = 'w')

        for theme_name in self.style.theme_names():
            rb = ttk.Radiobutton(
                theme_frame,
                text = theme_name,
                value = theme_name,
                variable = self.selected_theme,
                command = self.change_theme)
            rb.pack(expand = True, fill = 'both')

    def change_theme(self):
        self.style.theme_use(self.selected_theme.get())


if __name__ == "__main__":
    app = App()
    app.mainloop()