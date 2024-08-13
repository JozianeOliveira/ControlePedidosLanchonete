# Autora: Joziane Oliveira
# Descrição: Controle de pedidos de uma lanchonete

def menu():
    print("===MENU PRINCIPAL===")
    print("====================")
    print("1 - LANCHES")
    print("2 - ACOMPANHAMENTOS")
    print("3 - BEBIDAS")
    print("0 - SAIR DO SISTEMA")

def opcao():
    tpopc = 0

    menu()
    tpopc = int(input("Digite a opção desejada: "))

    while tpopc < 0 or tpopc > 3:
        print("Opção inválida, digite uma das opções válidas.")
        tpopc = int(input("Digite a opção desejada: "))

    return tpopc

def lanches():
    opcaoLanche = int(input("Digite a opção desejada: "))

    while opcaoLanche < 0 or opcaoLanche > 7:
        print("Opção inválida, digite uma das opções válidas.")
        opcaoLanche = int(input("Digite a opção desejada: "))

    return opcaoLanche

def acompanhamentos():
    opcaoAcompanhamento = int(input("Digite a opção desejada: "))

    while opcaoAcompanhamento < 0 or opcaoAcompanhamento > 7:
        print("Opção inválida, digite uma das opções válidas.")
        opcaoAcompanhamento = int(input("Digite a opção desejada: "))

    return opcaoAcompanhamento

def bebidas():
    opcaoBebida = int(input("Digite a opção desejada: "))

    while opcaoBebida < 0 or opcaoBebida > 7:
        print("Opção inválida, digite uma das opções válidas.")
        opcaoBebida = int(input("Digite a opção desejada: "))

    return opcaoBebida

def main():
    tpopcao = 0
    opcaoLanche = 0
    opcaoAcompanhamento = 0
    opcaoBebida = 0
    quantidade = 0
    totalLanches = 0.0
    totalAcompanhamentos = 0.0
    totalBebidas = 0.0
    totalGeral = 0.0

    tpopcao = opcao()

    if tpopcao == 0:
        print("Valor total de vendas no dia é zero.")
    else:
        while True:
            if tpopcao == 1:
                while True:
                    print("=================LANCHES================")
                    print("========================================")
                    print("1 - MODA DA CASA --------------- R$27,00")
                    print("2 - BURGUER SALADA ------------- R$21,00")
                    print("3 - FRAMBURGUER SALADA --------- R$25,00")
                    print("4 - X-EGG BACON ---------------- R$25,00")
                    print("5 - AMERICANO ------------------ R$23,00")
                    print("6 - X-BACON -------------------- R$26,00")
                    print("7 - LOMBINHO ESPECIAL ---------- R$27,00")
                    print("0 - RETORNAR AO MENU ANTERIOR")
                    opcaoLanche = int(input("Digite a opção desejada: "))

                    if opcaoLanche == 0:
                        print(f"O valor total dos lanches escolhidos nesse momento foi: R$ {totalLanches}")
                        print("Retornando ao Menu principal para que continue com seu pedido.")
                        break

                    quantidade = int(input("Informe a quantidade: "))

                    if opcaoLanche == 1:
                        totalLanches += 27.00 * quantidade
                    elif opcaoLanche == 2:
                        totalLanches += 21.00 * quantidade
                    elif opcaoLanche == 3:
                        totalLanches += 25.00 * quantidade
                    elif opcaoLanche == 4:
                        totalLanches += 25.00 * quantidade
                    elif opcaoLanche == 5:
                        totalLanches += 23.00 * quantidade
                    elif opcaoLanche == 6:
                        totalLanches += 26.00 * quantidade
                    elif opcaoLanche == 7:
                        totalLanches += 27.00 * quantidade

            elif tpopcao == 2:
                while True:
                    print("=============ACOMPANHAMENTOS=============")
                    print("=========================================")
                    print("1 - Batata Frita ----------------- R$8,00")
                    print("2 - Salada ----------------------- R$12,50")
                    print("3 - Anéis de Cebola -------------- R$14,00")
                    print("4 - Batata Doce Frita ------------ R$9,00")
                    print("5 - Nuggets ---------------------- R$10,00")
                    print("6 - Coxinha ---------------------- R$5,00")
                    print("7 - Polenta Frita ---------------- R$13,00")
                    print("0 - RETORNAR AO MENU ANTERIOR")
                    opcaoAcompanhamento = int(input("Digite a opção desejada: "))

                    if opcaoAcompanhamento == 0:
                        print(f"O valor total dos acompanhamentos escolhidos nesse momento foi: R$ {totalAcompanhamentos}")
                        print("Retornando ao Menu principal para que continue com seu pedido.")
                        break

                    quantidade = int(input("Informe a quantidade: "))

                    if opcaoAcompanhamento == 1:
                        totalAcompanhamentos += 8.00 * quantidade
                    elif opcaoAcompanhamento == 2:
                        totalAcompanhamentos += 12.50 * quantidade
                    elif opcaoAcompanhamento == 3:
                        totalAcompanhamentos += 14.00 * quantidade
                    elif opcaoAcompanhamento == 4:
                        totalAcompanhamentos += 9.00 * quantidade
                    elif opcaoAcompanhamento == 5:
                        totalAcompanhamentos += 10.00 * quantidade
                    elif opcaoAcompanhamento == 6:
                        totalAcompanhamentos += 5.00 * quantidade
                    elif opcaoAcompanhamento == 7:
                        totalAcompanhamentos += 13.00 * quantidade

            elif tpopcao == 3:
                while True:
                    print("=================BEBIDAS==================")
                    print("==========================================")
                    print("1 - Coca-cola 2l ------------------ R$10,00")
                    print("2 - Coca-cola 1l ------------------ R$8,00")
                    print("3 - Fanta 2l ---------------------- R$9,00")
                    print("4 - Fanta 1l ---------------------- R$8,00")
                    print("5 - Guaraná 1l -------------------- R$6,00")
                    print("6 - Suco Natural ------------------ R$7,00")
                    print("7 - Água -------------------------- R$2,00")
                    print("0 - RETORNAR AO MENU ANTERIOR")
                    opcaoBebida = int(input("Digite a opção desejada: "))

                    if opcaoBebida == 0:
                        print(f"O valor total das bebidas escolhidos nesse momento foi: R$ {totalBebidas}")
                        print("Retornando ao Menu principal para que continue com seu pedido.")
                        break

                    quantidade = int(input("Informe a quantidade: "))

                    if opcaoBebida == 1:
                        totalBebidas += 10.00 * quantidade
                    elif opcaoBebida == 2:
                        totalBebidas += 8.00 * quantidade
                    elif opcaoBebida == 3:
                        totalBebidas += 9.00 * quantidade
                    elif opcaoBebida == 4:
                        totalBebidas += 8.00 * quantidade
                    elif opcaoBebida == 5:
                        totalBebidas += 6.00 * quantidade
                    elif opcaoBebida == 6:
                        totalBebidas += 7.00 * quantidade
                    elif opcaoBebida == 7:
                        totalBebidas += 2.00 * quantidade

            tpopcao = opcao()
            if tpopcao == 0:
                break

        totalGeral = totalLanches + totalAcompanhamentos + totalBebidas

        print(f"\nTotal de vendas de Lanches: R$ {totalLanches:.2f}")
        print(f"Total de vendas de Acompanhamentos: R$ {totalAcompanhamentos:.2f}")
        print(f"Total de vendas de Bebidas: R$ {totalBebidas:.2f}")
        print(f"Total geral de vendas do dia: R$ {totalGeral:.2f}")
        print("\nSaindo do sistema.")

if __name__ == "__main__":
    main()
