

extrato = []
dict_extrato = {
    'Depositos': 0,
    'Saques': 0
}
saldo = 0
total_saques = []

operacao = 0

while operacao < 4:
    operacao = int(input(
    '''
    Escolha a operação:
    [1] - Depositar
    [2] - Sacar
    [3] - Mostrar extrato
    [4] - Sair
    '''))

    if operacao == 1:
        continuar = 'sim'

        while continuar == 'sim' :
            deposito = float(input('Valor depósito: \n'))

            if deposito < 0.0:
                print('Não é possível depositar valores menores do que 0 \n')
            
            else:
                print('depósito realizado com sucesso! \n')
                saldo += deposito
                extrato.append(deposito)
                dict_extrato = {
                    'Depositos': extrato
                }
                continuar = input('deseja continuar: ').strip().lower()

                if continuar != 'sim':
                    continuar == 'nao'
                else:
                    continue

    elif operacao == 2:
        sacar = 1
        while sacar <= 3:
            saque = float(input(f'Seu saldo é de: R${saldo}, deseja sacar quanto? \n'))
            if saque > saldo:
                print('não é possível sacar mais do que seu saldo!')
            saldo -= saque
            total_saques.append(saque)
            dict_extrato['Saques'] = total_saques
            sacar +=1
    
    elif operacao == 3:
        print(f'Seu extrato: {dict_extrato}, valor atual: {saldo}')

    else:
        print('Operação não existe')


        






