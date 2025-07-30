import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto4 = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_2["text"] = texto4


janela = Tk()
janela.title("te amo <3")
janela.geometry("100x200")

texto = Label(janela, text="Clique aqui!")
texto.grid(column=0,row=0, padx = 10 , pady = 10)

botao = Button(janela, text="buscar amor",command=pegar_cotacoes)
botao.grid(column=0,row=1, padx = 20 , pady = 10)

texto_2 = Label(janela, text = "")
texto_2.grid(column= 0, row = 2, padx = 10 , pady = 10)

janela.mainloop()