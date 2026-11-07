import tkinter as tk
TEMPO_VERMELHO = 5
TEMPO_AMARELO = 2
TEMPO_VERDE = 5
janela = tk.Tk()
janela.title("Semáforo")
janela.geometry("600x200")
janela.resizable(False, False)
janela.configure(bg="black")
canvas = tk.Canvas(
    janela,
    width=600,
    height=180,
    bg="black",
    highlightthickness=0
)
canvas.pack(pady=10)
raio = 80
centros = [100, 300, 500]
cores = ["red", "yellow", "green"]
luzes = []
for x in centros:
    luz = canvas.create_oval(
        x - raio, 10,
        x + raio, 170,
        fill="#333333",
        outline="white",
        width=3
    )
    luzes.append(luz)
estados = [
    (0, TEMPO_VERMELHO),
    (2, TEMPO_VERDE),
    (1, TEMPO_AMARELO)
]
indice = 0
def atualizar_semaforo():
    global indice
    luz_ativa, duracao = estados[indice]
    for luz in luzes:
        canvas.itemconfig(luz, fill="#333333")
    canvas.itemconfig(
        luzes[luz_ativa],
        fill=cores[luz_ativa]
    )
    indice = (indice + 1) % len(estados)
    janela.after(duracao * 1000, atualizar_semaforo)
atualizar_semaforo()
janela.mainloop()
