
# Lista que armazenará todos os chamados
chamados = []


# Função para validar a prioridade
def solicitar_prioridade():

    prioridade = input(
        "Digite a prioridade (BAIXA, MEDIA ou ALTA): "
    ).strip().upper()

    while prioridade not in ["BAIXA", "MEDIA", "ALTA"]:

        print("Prioridade inválida! Tente novamente.")

        prioridade = input(
            "Digite a prioridade (BAIXA, MEDIA ou ALTA): "
        ).strip().upper()

    return prioridade


# i. Função para adicionar um chamado
def adicionar_chamado(lista, id, usuario, descricao, prioridade):

    chamado = {
        "id": id,
        "usuario": usuario,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": "ABERTO"
    }

    lista.append(chamado)

    print("\nChamado cadastrado com sucesso!")

    return chamado


# ii. Função para listar os chamados
def listar_chamados(lista, filtro_prioridade=None):

    encontrou = False

    print("\n========== LISTA DE CHAMADOS ==========")

    for chamado in lista:

        if filtro_prioridade is None or chamado["prioridade"] == filtro_prioridade:

            print(f"ID: {chamado['id']}")
            print(f"Usuário: {chamado['usuario']}")
            print(f"Descrição: {chamado['descricao']}")
            print(f"Prioridade: {chamado['prioridade']}")
            print(f"Status: {chamado['status']}")
            print("-" * 35)

            encontrou = True

    if not encontrou:

        print("Nenhum chamado encontrado.")


# iii. Função para encerrar um chamado
def encerrar_chamado(lista, id):

    for chamado in lista:

        if chamado["id"] == id:

            chamado["status"] = "CONCLUÍDO"

            print("\nChamado encerrado com sucesso!")

            return True

    print("\nChamado não encontrado!")

    return False


# iv. Função para contar chamados abertos
def obter_total_abertos(lista):

    total = 0

    for chamado in lista:

        if chamado["status"] == "ABERTO":

            total += 1

    return total


# Menu principal
def main():

    proximo_id = 1

    while True:

        print("\n========== SERVICE DESK ==========")
        print("1 - Novo Chamado")
        print("2 - Listar Todos")
        print("3 - Listar por Prioridade")
        print("4 - Encerrar Chamado")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        # Opção 1 - Novo chamado
        if opcao == "1":

            usuario = input("Nome do usuário: ")

            descricao = input("Descrição do problema: ")

            prioridade = solicitar_prioridade()

            adicionar_chamado(
                chamados,
                proximo_id,
                usuario,
                descricao,
                prioridade
            )

            proximo_id += 1

        # Opção 2 - Listar todos
        elif opcao == "2":

            listar_chamados(chamados)

            print(
                f"Total de chamados abertos: "
                f"{obter_total_abertos(chamados)}"
            )

        # Opção 3 - Listar por prioridade
        elif opcao == "3":

            prioridade = solicitar_prioridade()

            listar_chamados(chamados, prioridade)

        # Opção 4 - Encerrar chamado
        elif opcao == "4":

            try:

                id_chamado = int(
                    input("Digite o ID do chamado: ")
                )

                encerrar_chamado(chamados, id_chamado)

                print(
                    f"Total de chamados abertos: "
                    f"{obter_total_abertos(chamados)}"
                )

            except ValueError:

                print("Erro: informe um ID numérico!")

        # Opção 0 - Sair
        elif opcao == "0":

            print("Encerrando o sistema...")

            break

        else:

            print("Opção inválida! Tente novamente.")


# Executa o programa
if __name__ == "__main__":
    main()
