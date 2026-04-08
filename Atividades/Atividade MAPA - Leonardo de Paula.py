from datetime import datetime
import math

# --- Configurações Iniciais ---
# --- Desenvolvido por: Leonardo de Paula da Silva | Data: 02/04/2026 ---
# --- Login: admin | Senha: admin ---
veiculos = []

tipos = {
    1: "Carro",
    2: "Motocicleta",
    3: "Camionete"
}


def calcular_valor(minutos):
    if minutos <= 15:
        return 0.0
    elif minutos <= 60:
        return 1.50
    else:
        # R$ 1,50 da primeira hora + R$ 1,00 por hora adicional (ou fração)
        # Ex: 70 min -> (70-60)/60 = 0.16 -> ceil vira 1 -> Total 2.50
        horas_adicionais = math.ceil((minutos - 60) / 60)
        return 1.50 + float(horas_adicionais)


def converter_hora(hora_str):
    agora = datetime.now()
    if ":" in hora_str:
        h, m = hora_str.split(":")
        return agora.replace(hour=int(h), minute=int(m), second=0, microsecond=0)
    else:
        return agora.replace(hour=int(hora_str), minute=0, second=0, microsecond=0)


# --- Loop Principal de Login ---
while True:
    print("\n" + "=" * 21 + " LOGIN " + "=" * 24)
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario != "admin" or senha != "admin":
        print("Login inválido!")
        continue

    # --- Menu do Sistema ---
    while True:
        print("\n" + "=" * 21 + " MENU " + "=" * 22)
        print("1 - Inserir veículo")
        print("2 - Consultar todos veículos")
        print("3 - Veículos estacionados (pendentes por tipo)")
        print("4 - Retirar veículo (Baixa)")
        print("5 - Totais Financeiros")
        print("6 - Editar hora de entrada")
        print("7 - Relatório Detalhado por Tipo")
        print("0 - Logout")

        opcao = input("Escolha: ")

        # 1 - INSERIR VEÍCULO
        if opcao == "1":
            placa = input("Placa: ").upper()

            # Verificar duplicidade
            ja_estacionado = False
            for v in veiculos:
                if v["placa"] == placa and v["status"] == "PENDENTE":
                    print("Erro: Este veículo já está no pátio!")
                    ja_estacionado = True
                    break

            if not ja_estacionado:
                print("Tipos disponíveis:")
                for k, v in tipos.items():
                    print(f"{k} - {v}")

                try:
                    tipo_escolhido = int(input("Escolha o tipo: "))
                    if tipo_escolhido in tipos:
                        hora_atual = datetime.now()
                        veiculos.append({
                            "placa": placa,
                            "tipo": tipos[tipo_escolhido],
                            "entrada": hora_atual,
                            "saida": None,
                            "status": "PENDENTE"
                        })
                        print(f"Registrado com sucesso às {hora_atual.strftime('%H:%M')}")
                    else:
                        print("Tipo inválido!")
                except ValueError:
                    print("Entrada inválida! Digite o número do tipo.")

        # 2 - CONSULTAR TODOS
        elif opcao == "2":
            if not veiculos:
                print("Nenhum registro encontrado.")
                continue

            print("\n" + "-" * 15 + " Relatório Geral " + "-" * 15)
            print(f"{'PLACA':8} | {'TIPO':12} | {'STATUS':10} | {'TEMPO'}")
            for v in veiculos:
                ref_final = v["saida"] if v["status"] == "CONCLUIDO" else datetime.now()
                minutos = int((ref_final - v["entrada"]).total_seconds() / 60)
                print(f"{v['placa']:8} | {v['tipo']:12} | {v['status']:10} | {minutos} min")

        # 3 - VEÍCULOS PENDENTES POR TIPO
        elif opcao == "3":
            print("\nFiltrar por tipo:")
            for k, v in tipos.items(): print(f"{k} - {v}")

            try:
                t_busca = int(input("Escolha: "))
                if t_busca in tipos:
                    print(f"\n--- {tipos[t_busca].upper()} NO PÁTIO ---")
                    encontrou = False
                    for v in veiculos:
                        if v["status"] == "PENDENTE" and v["tipo"] == tipos[t_busca]:
                            minutos = int((datetime.now() - v["entrada"]).total_seconds() / 60)
                            print(f"Placa: {v['placa']} | Entrada: {v['entrada'].strftime('%H:%M')} | {minutos} min")
                            encontrou = True
                    if not encontrou: print("Nenhum veículo deste tipo estacionado.")
            except ValueError:
                print("Opção inválida.")

        # 4 - RETIRAR VEÍCULO
        elif opcao == "4":
            placa = input("Placa para saída: ").upper()
            encontrou = False
            for v in veiculos:
                if v["placa"] == placa and v["status"] == "PENDENTE":
                    v["saida"] = datetime.now()
                    v["status"] = "CONCLUIDO"
                    minutos = int((v["saida"] - v["entrada"]).total_seconds() / 60)
                    valor = calcular_valor(minutos)
                    print(f"\nSaída confirmada! Tempo: {minutos} min | Valor: R$ {valor:.2f}")
                    encontrou = True
                    break
            if not encontrou: print("Veículo não encontrado ou já processado.")

        # 5 - TOTAIS FINANCEIROS
        elif opcao == "5":
            t_concluido = 0.0
            t_pendente = 0.0
            for v in veiculos:
                if v["status"] == "CONCLUIDO":
                    minutos = int((v["saida"] - v["entrada"]).total_seconds() / 60)
                    t_concluido += calcular_valor(minutos)
                else:
                    minutos = int((datetime.now() - v["entrada"]).total_seconds() / 60)
                    t_pendente += calcular_valor(minutos)

            print(f"\n--- RESUMO FINANCEIRO ---")
            print(f"Já Arrecadado: R$ {t_concluido:.2f}")
            print(f"Previsão Pendente: R$ {t_pendente:.2f}")
            print(f"Total Geral: R$ {t_concluido + t_pendente:.2f}")

        # 6 - EDITAR HORA
        elif opcao == "6":
            placa = input("Placa do veículo: ").upper()
            encontrou = False
            for v in veiculos:
                if v["placa"] == placa and v["status"] == "PENDENTE":
                    nova_hora = input("Nova hora (ex 08:30 ou 14): ")
                    try:
                        v["entrada"] = converter_hora(nova_hora)
                        print(f"Sucesso! Nova entrada: {v['entrada'].strftime('%H:%M')}")
                        encontrou = True
                    except:
                        print("Erro no formato da hora.")
                    break
            if not encontrou: print("Veículo não localizado.")

        # 7 - RELATÓRIO DETALHADO (NOVA OPÇÃO)
        elif opcao == "7":
            print("\n" + "=" * 15 + " RELATÓRIO POR TIPO " + "=" * 15)
            # Dicionário: {Nome: [No Pátio, Saíram, Valor Total]}
            stats = {nome: [0, 0, 0.0] for nome in tipos.values()}
            total_arrecadado = 0.0

            for v in veiculos:
                t = v["tipo"]
                if v["status"] == "PENDENTE":
                    stats[t][0] += 1
                else:
                    stats[t][1] += 1
                    minutos = int((v["saida"] - v["entrada"]).total_seconds() / 60)
                    v_pago = calcular_valor(minutos)
                    stats[t][2] += v_pago
                    total_arrecadado += v_pago

            print(f"{'TIPO':15} | {'PÁTIO':7} | {'SAÍDAS':7} | {'ARRECADADO'}")
            print("-" * 50)
            for tipo, dados in stats.items():
                print(f"{tipo:15} | {dados[0]:^7} | {dados[1]:^7} | R$ {dados[2]:>8.2f}")
            print("-" * 50)
            print(f"TOTAL FINAL ARRECADADO: R$ {total_arrecadado:.2f}")
            print("=" * 50)

        # 0 - LOGOUT
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")