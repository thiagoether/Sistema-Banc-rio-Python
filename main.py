menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
->
"""
deposito = 0
saldo = 0
limite = 500
extrato = list()
numero_saques = 0
LIMITE_SAQUES = 3

while True: 
    opcao = input(menu)
    if opcao == "d":
        while True:
            deposito = float(input("Informe o valor a ser depositado: R$"))
            if deposito <= 0:
                print("Valor inválido! Tente novamente.")
            else:
                saldo += deposito
                extrato.append(f'Depósito: R${deposito:.2f}')
                break
        
    elif opcao == 's': # sacar
        while True:
            saque = float(input("Informe o valor do saque: R$"))
            if saque <= 0:
                print("Valor inválido! Tente novamente.")
            elif saque > saldo:
                print("Operação falhou. Você não tem saldo suficiente!")
                break
            elif saque > 500:
                print("Operação falhou. O valor do saque excede o limite!")
            elif numero_saques == 3:
                print('Limite de saques excedido!')
                break
            else:
                saldo -= saque
                extrato.append(f'Saque: R${saque:.2f}')
                numero_saques += 1                
                break
        
    elif opcao == 'e': # extrato
        print('========== EXTRATO ==========')
        if deposito == 0:
            print('Não foram realizadas movimentações.')
        else:
            for mostrarExtrato in extrato:
                print(mostrarExtrato)
        print(f'\nSaldo: {saldo:.2f}')
            
    elif opcao == 'q': # sair
        print('FIM')
        break
    
    else:
        print('OPCÃO INVÁLIDA.')