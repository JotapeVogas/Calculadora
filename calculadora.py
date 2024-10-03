import tkinter as tk


def adicionar_caracter(caracter):
    entrada_texto.insert(tk.END, caracter)


def limpar_entrada():
    entrada_texto.delete(0, tk.END)


def apagar_ultimo():
    entrada_texto.delete(len(entrada_texto.get()) - 1, tk.END)


def calcular():
    expressao = entrada_texto.get()
    try:
        resultado = eval(expressao)
        limpar_entrada()
        entrada_texto.insert(tk.END, resultado)
    except:
        limpar_entrada()
        entrada_texto.insert(tk.END, "Erro")


def criar_botao(valor, x, y, janela):
    botao = tk.Button(janela, text=valor, width=5, height=2, command=lambda: adicionar_caracter(valor))
    botao.place(x=x, y=y)


i = tk.Tk()
i.title("Calculadora")

i.geometry("240x340")

i.tk_setPalette(background='#40223c')

# Entrada de texto para a expressão
entrada_texto = tk.Entry(i, width=24, font=20, bg='#42988f', fg='white')
entrada_texto.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botões dos números e operações
botoes = [
    ('1', 15, 50), ('2', 70, 50), ('3', 125, 50), ('/', 180, 50),
    ('4', 15, 110), ('5', 70, 110), ('6', 125, 110), ('*', 180, 110),
    ('7', 15, 170), ('8', 70, 170), ('9', 125, 170), ('-', 180, 170),
    ('.', 15, 230), ('0', 70, 230), ('+', 125, 230), ('%', 180, 230)
]

# Adicionando botões
for valor, x, y in botoes:
    botao = tk.Button(i, text=valor, width=5, height=2, command=lambda val=valor: adicionar_caracter(val), bg='#b1c592',
                      fg='black', border=0).place(x=x, y=y)

# Botão de limpar
botao_limpar = tk.Button(i, text='C', width=5, height=2, command=limpar_entrada, bg='#fb718a', fg='black', border=0)
botao_limpar.place(x=15, y=290)

# Botão de calcular
botao_calcular = tk.Button(i, text='=', width=5, height=2, command=calcular, bg='#fb718a', fg='black', border=0)
botao_calcular.place(x=70, y=290)

botao_apagar = tk.Button(i, text='⌫', width=13, height=2, command=apagar_ultimo, bg='#fb718a', fg='black', border=0)
botao_apagar.place(x=125, y=290)

i.mainloop()
