import tkinter as tk

root = tk.Tk()
root.geometry('300x300')
root.title('CALCULO IMC')
# Menor que 18,5	Abaixo do peso
# 18,5 a 24,9	Peso normal
# 25 a 29,9	Sobrepeso
# 30 a 34,9	Obesidade grau I
# 35 a 39,9	Obesidade_II
# 40 a 49,9	Obesidade_III
# 50 a 59,9	Obsevidade grau IV
# Acima de 60	Obesidade grau V



def imc():
    peso = float(input_peso.get())
    altura = float(input_altura.get())
    imc = peso / (altura ** 2)
    nome = input_nome.get()
    Imc.config(text=f'NOME: {nome} \nIMC: {imc:.2f}')
    if imc < 18.5:
        abaixo = tk.Label(root, text='Abaixo do peso')
        abaixo.grid(row=5, column=2,)
    elif imc >= 18.6 and imc <= 24.9:                                                     
        normal = tk.Label(root, text='Peso Normal')
        normal.grid(row=5, column=2)
    elif imc >= 25 and imc <= 29.9:
        Sobrepeso = tk.Label(root, text='Peso Sobrepeso')
        Sobrepeso.grid(row=5, column=2)
    elif imc >= 30 and imc <= 34.9:
        Obesidade_I = tk.Label(root, text='Peso Obesidade grau I')
        Obesidade_I.grid(row=5, column=2)
    elif imc >= 35 and imc <= 39.9:
        Obesidade_II = tk.Label(root, text='Peso Obesidade Grau II')
        Obesidade_II.grid(row=5, column=2)
    elif imc >= 40 and imc <= 49.9:
        Grau_III = tk.Label(root, text='Peso Obesidade Grau III')
        Grau_III.grid(row=5, column=2)
    elif imc >= 50 and imc <= 59.9:
        Grau_IV = tk.Label(root, text='Peso Obesidade Grau IV')
        Grau_IV.grid(row=5, column=2)
    elif imc > 60:
        Grau_V = tk.Label(root, text='Obesidade Grau V')
        Grau_V.grid(row=5, column=2)
    

nome = tk.Label(root, text='Digite seu nome: ')
nome.grid(row=1, column=1,)

altura = tk.Label(root, text='Digite sua altura: ')
altura.grid(row=2, column=1)

peso = tk.Label(root, text='Digite seu peso: ')
peso.grid(row=3, column=1)

input_nome = tk.Entry(root)
input_nome.grid(row=1,column=2)

input_peso = tk.Entry(root)
input_peso.grid(row=3,column=2)

input_altura = tk.Entry(root)
input_altura.grid(row=2,column=2)

Imc = tk.Label(root, text='-')
Imc.grid(row=4, column=2, padx=5)

btn = tk.Button(root, text='IMC', command= imc)
btn.grid(row=4,column=1, padx=15)

root.mainloop()