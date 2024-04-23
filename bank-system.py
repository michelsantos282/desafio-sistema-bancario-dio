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

        if valor_deposito < 0:
            print("Valor inválido, tente novamente!")

            while valor_deposito < 0:
                valor_deposito = float(input("Digite o valor que deseja depositar: R$"))
        
        saldo += valor_deposito
        extrato = extrato + f"Depósito realizado no valor de R${valor_deposito:.2f}\n"
        print("Depósito realizado com sucesso!")
    
    elif opcao == 2:
        if numero_saques >= LIMITE_SAQUES:
            print("Você atingiu o limite de saques diários, tente novamente amanhã!")
            continue

        valor_saque = float(input("Digite o valor que deseja sacar: R$"))
        if valor_saque > limite:
             print("Valor de saque excedido, tente novamente!")
             while valor_saque > limite:
                valor_saque = float(input("Digite o valor que deseja sacar: R$"))
        elif valor_saque > saldo:
            print("Saldo insuficiente, tente novamente!")
            while valor_saque > saldo:
                valor_saque = float(input("Digite o valor que deseja sacar: R$"))
        
        saldo -= valor_saque
        numero_saques += 1
        extrato = extrato + f"Saque realizado no valor de R${valor_saque:.2f}\n"
        print("Saque realizado com sucesso!")

    elif opcao == 3:
        print(extrato)
        print(f"Saldo disponível: R$ {saldo:.2f}")
    
    elif opcao == 0:
        break
    else:
        print("Opção inválida, por favor selecione novamente.")

print("Obrigado por utilizar nosso sistema, volte sempre!")

