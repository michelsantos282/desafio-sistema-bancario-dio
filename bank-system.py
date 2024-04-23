LIMITE_SAQUES = 3
numero_saques = 0
extrato = ""
saldo = 0
limite = 500

menu = f"""
    {" Menu ".center(34, "=")}
    |                                | 
    | 1 - Depósito                   | 
    | 2 - Saque                      | 
    | 3 - Extrato                    |                  
    | 0 - Sair                       |
    |                                |
    {"".center(34, "=")}
"""    

while True:
    opcao = int(input(menu))
    if opcao == 1:
        valor_deposito = float(input("Digite o valor que deseja depositar: R$"))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito realizado no valor de R${valor_deposito:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou, valor de depósito inválido")

    elif opcao == 2:
        valor_saque = float(input("Digite o valor que deseja sacar: R$"))
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        excedeu_limite = valor_saque > limite
        excedeu_saldo = valor_saque > saldo
    
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque realizado no valor de R${valor_saque:.2f}\n"
            print("Saque realizado com sucesso!")

    elif opcao == 3:
        print(" EXTRATO ".center(50, "="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo disponível: R$ {saldo:.2f}")
        print("".center(50, "="))
    
    elif opcao == 0:
        break
    else:
        print("Opção inválida, por favor selecione novamente.")

print("Obrigado por utilizar nosso sistema, volte sempre!")

