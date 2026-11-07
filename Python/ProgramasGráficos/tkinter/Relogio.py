import tkinter as tk
from time import strftime
def atualizar_relogio():
    global segundos_restantes
    hora_atual = strftime("%I:%M:%S %p")
    label_relogio.config(text=hora_atual)
    if segundos_restantes > 0:
        segundos_restantes -= 1
        janela.after(1000, atualizar_relogio)
# Configuração da janela
janela = tk.Tk()
janela.title("Relógio")
janela.geometry("400x400")
janela.resizable(False, False)
janela.configure(bg="black")
# Contador de 60 segundos
segundos_restantes = 60
# Texto do relógio
label_relogio = tk.Label(
    janela,
    text="",
    font=("Arial", 28),
    fg="red",
    bg="black"
)
label_relogio.place(relx=0.5, rely=0.5, anchor="center")
# Inicia a atualização
atualizar_relogio()
# Mantém a janela aberta
janela.mainloop()
