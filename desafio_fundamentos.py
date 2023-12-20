menu = """

[d] Depositar
[s] Sacar
[e] Extarto
[x] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True: 

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor que você quer depositar:"))

        if valor > 0: 
            saldo += valor
            extrato += f"Depósito: R$ {valor :.2f}\n"
        
        else: 
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque:"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite 

        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo: 
            print("Você não possui saldo sufuciente!")

        elif excedeu_limite: 
            print("Excedeu o limite, por favor tente um valor menor. ")

        elif excedeu_saques: 
            print("Você não possui mais saques hoje!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:  R$ {valor:.2f}\n"
            numero_saques += 1

        else: 
            print("Opercação falhou! Numero informado é invalido")

        
    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não  foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================")

    elif opcao == "x":
        break

    else: 
        print("Operação invalida, por favor selecione novamente a operação desejada")