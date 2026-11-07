import ctypes
import time
user32 = ctypes.WinDLL("user32", use_last_error=True)
TECLAS = {
    0x01: "Botão esquerdo do mouse",
    0x02: "Botão direito do mouse",
    0x41: "Tecla A",
    0x42: "Tecla B",
    0x20: "Barra de espaço",   
    0x1B: "Tecla ESC",
}
ESTADO_PRESSIONADO = 0x8000
INTERVALO = 0.01
def esta_pressionado(tecla):
    return bool(user32.GetAsyncKeyState(tecla) & ESTADO_PRESSIONADO)
def main():
    estados_anteriores = {tecla: False for tecla in TECLAS}
    print("Monitoramento iniciado. Pressione Ctrl+C para sair.\n")
    try:
        while True:
            for tecla, nome in TECLAS.items():
                estado_atual = esta_pressionado(tecla)
                # Detecta apenas a transição de solto para pressionado
                if estado_atual and not estados_anteriores[tecla]:
                    print(f"{nome} pressionado")
                estados_anteriores[tecla] = estado_atual
            time.sleep(INTERVALO)
    except KeyboardInterrupt:
        print("\nMonitoramento encerrado.")
if __name__ == "__main__":
    main()
