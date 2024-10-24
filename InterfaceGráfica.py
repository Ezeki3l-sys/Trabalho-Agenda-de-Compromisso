from tkinter import *

import pandas as pd

df = pd.DataFrame(
     {
         "compromisso": [
             "parque",
            "farmácia",
             "sua mãe",
         ],
         "horas": [10.30, 11.10, 1.00],
         "local": ["Campolim", "Itavuvu", "casa dela"],
     }
 )

janela = Tk()
janela.title("Agenda de compromissos")
janela.geometry("400x200")

#compromisso = Entry(janela)
#compromisso.grid(column=0,row=0)
texto = df
texto_2 = Label(janela, text = texto)
texto_2.grid(column= 0, row = 2, padx = 10 , pady = 10)


janela.mainloop()
