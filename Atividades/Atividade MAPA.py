from datetime import datetime
import math

veiculos = []

tipos = {
    1: "Carro",
    2: "Motocicleta",
    3: "Camionete"
}

def calcular_valor(minutos):

    if minutos <= 15:
        return 0
    elif minutos <= 60:
        return 1.50
    else:
        horas = math.ceil((minutos - 60) / 60)
        return 1.50 + horas


def converter_hora(hora_str):

    agora = datetime.now()

    if ":" in hora_str:
        h, m = hora_str.split(":")
        return agora.replace(hour=int(h), minute=int(m), second=0, microsecond=0)
    else:
        return agora.replace(hour=int(hora_str), minute=0, second=0, microsecond=0)


while True:

    print("\n===================== LOGIN ========================")

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario != "admin" or senha != "admin":
        print("Login inválido")
        continue

    while True:

        print("\n===================== MENU =====================")
        print("1 - Inserir veículo")
        print("2 - Consultar todos veículos")
        print("3 - Veículos estacionados (pendentes)")
        print("4 - Retirar veículo")
        print("5 - Totais")
        print("6 - Editar hora de entrada")
        print("0 - Logout")

        opcao = input("Escolha: ")

        # ----------------------------
        # 1 INSERIR VEÍCULO
        # ----------------------------

        if opcao == "1":

            placa = input("Placa: ").upper()

            # verificar se já existe veículo pendente com a mesma placa
            for v in veiculos:
                if v["placa"] == placa and v["status"] == "PENDENTE":
                    print("Este veículo já está estacionado!")
                    break
            else:

                print("Tipo:")
                for k, v in tipos.items():
                    print(k, "-", v)

                try:
                    tipo = int(input("Escolha o tipo: "))
                except:
                    print("Tipo inválido")
                    continue

                if tipo not in tipos:
                    print("Tipo inválido")
                    continue

                hora = datetime.now()

                veiculos.append({
                    "placa": placa,
                    "tipo": tipos[tipo],
                    "entrada": hora,
                    "saida": None,
                    "status": "PENDENTE"
                })

                print("Veículo registrado às", hora.strftime("%H:%M"))

        # ----------------------------
        # 2 CONSULTAR TODOS
        # ----------------------------

        elif opcao == "2":

            if not veiculos:
                print("Nenhum veículo registrado")
                continue

            print("\n=============== Relatório ===============\n")

            print("PLACA   | TIPO         | STATUS     | TEMPO")
            print("---------------------------------------------")

            for v in veiculos:

                if v["status"] == "PENDENTE":
                    minutos = int((datetime.now() - v["entrada"]).total_seconds() / 60)
                else:
                    minutos = int((v["saida"] - v["entrada"]).total_seconds() / 60)

                print(f'{v["placa"]:7} | {v["tipo"]:12} | {v["status"]:10} | {minutos} min')

            print("\n===========================================")

        # ----------------------------
        # 3 VEÍCULOS PENDENTES
        # ----------------------------

        elif opcao == "3":

            print("\nFiltrar tipo")

            for k, v in tipos.items():
                print(k, "-", v)

            try:
                tipo = int(input("Escolha: "))
            except:
                print("Tipo inválido")
                continue

            if tipo not in tipos:
                print("Tipo inválido")
                continue

            encontrou = False

            print("\n====== VEÍCULOS ESTACIONADOS ======\n")

            for v in veiculos:

                if v["status"] == "PENDENTE" and v["tipo"] == tipos[tipo]:

                    minutos = int((datetime.now() - v["entrada"]).total_seconds() / 60)

                    print(f'{v["placa"]} | {v["tipo"]} | {minutos} minutos')

                    encontrou = True

            if not encontrou:
                print("Nenhum veículo encontrado")

        # ----------------------------
        # 4 RETIRAR VEÍCULO
        # ----------------------------

        elif opcao == "4":

            placa = input("Placa do veículo: ").upper()

            encontrou = False

            for v in veiculos:

                if v["placa"] == placa and v["status"] == "PENDENTE":

                    saida = datetime.now()

                    minutos = int((saida - v["entrada"]).total_seconds() / 60)

                    valor = calcular_valor(minutos)

                    v["saida"] = saida
                    v["status"] = "CONCLUIDO"

                    print("\nTempo:", minutos, "minutos")
                    print(f"Valor a pagar: R$ {valor:.2f}")

                    encontrou = True
                    break

            if not encontrou:
                print("Veículo não encontrado ou já retirado")

        # ----------------------------
        # 5 TOTAIS
        # ----------------------------

        elif opcao == "5":

            total_concluido = 0
            total_pendente = 0

            for v in veiculos:

                if v["status"] == "CONCLUIDO":

                    minutos = int((v["saida"] - v["entrada"]).total_seconds() / 60)
                    valor = calcular_valor(minutos)

                    total_concluido += valor

                elif v["status"] == "PENDENTE":

                    minutos = int((datetime.now() - v["entrada"]).total_seconds() / 60)
                    valor = calcular_valor(minutos)

                    total_pendente += valor

            total_geral = total_concluido + total_pendente

            print("\n============= TOTAIS =============\n")

            print(f"Total concluído: R$ {total_concluido:.2f}")
            print(f"Total pendente : R$ {total_pendente:.2f}")
            print(f"Total geral    : R$ {total_geral:.2f}")

            print("\n==================================")

        # ----------------------------
        # 6 EDITAR HORA ENTRADA
        # ----------------------------

        elif opcao == "6":

            placa = input("Placa do veículo: ").upper()

            encontrou = False

            for v in veiculos:

                if v["placa"] == placa and v["status"] == "PENDENTE":

                    nova_hora = input("Nova hora de entrada (8 ou 8:10): ")

                    try:

                        v["entrada"] = converter_hora(nova_hora)

                        print("Hora de entrada atualizada para", v["entrada"].strftime("%H:%M"))

                        encontrou = True

                    except:
                        print("Formato de hora inválido")

                    break

            if not encontrou:
                print("Veículo não encontrado ou já concluído")


        elif opcao == "0":
            break