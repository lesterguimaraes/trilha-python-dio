menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
numero_depositos = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    #DEPÓSITO
    if opcao == "d":
        valor=float(input("Informe o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            numero_depositos += 1
            extrato += f"Depósito: R${valor:.2f}\n"
            print(f"Foi realizado um Depósito no valor de R${valor:.2f}")
        else:
            print(f"Não foi possivel depositar. \n Valor R${valor:.2f} incorreto \n")
    
    #SAQUE
    elif opcao == "s":
        valor_saque=float(input("Informe o valor do Saque: "))

        sem_saldo = valor_saque > saldo
        sem_limite_saldo = valor_saque > limite
        sem_limite_saques = numero_saques >= LIMITE_SAQUES
        

        if sem_saldo:
            print(f"Sua conta está com saldo insuficiente para valor de saque. Seu saldo é de R${saldo:.2f}")
           
        elif sem_limite_saques:
            print(f"Caro cleinte! Você Excedeu a quantidade limite de {LIMITE_SAQUES} saques diário.")
        
        elif valor_saque > 0:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque: R${valor_saque:.2f}\n"
            print(f"Foi realizado o saque no valor de R$:{valor_saque}")
    
    #EXTRATO    
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Quantidade de depósitos realizados: {numero_depositos}")
        print(f"Quantidade de saques realizados: {numero_saques}")
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("==========================================")
    
    #SAIR
    elif opcao == "q":
        break
    else:
        print("Operação inválida, selecione a opção desejada")
