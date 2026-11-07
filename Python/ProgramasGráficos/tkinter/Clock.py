import time
def fun():
    for i in range(2_000_000):
        pass
def main():
    inicio = time.process_time()
    fun()
    fim = time.process_time()
    tempo = fim - inicio
    print(f"{tempo:.6f}")
if __name__ == "__main__":
    main()
