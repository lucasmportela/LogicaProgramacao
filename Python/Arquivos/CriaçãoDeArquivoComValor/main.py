def main():
    try:
        with open("program.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()
            if not conteudo:
                print("Erro: o arquivo está vazio.")
                return
            num = float(conteudo.split()[0])
            print(f"Valor lido do arquivo é = {num:.1f}")
    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")
    except ValueError:
        print("Erro: o arquivo não contém um número válido.")
    except OSError as erro:
        print(f"Erro ao acessar o arquivo: {erro}")
if __name__ == "__main__":
    main()
