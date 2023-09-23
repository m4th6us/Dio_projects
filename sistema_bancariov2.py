class SistemaBancario:

    def __init__(self) -> None:

        self.extract = {
            "Depósitos": [],
            "Saque": []
        }

        self.account = False
    
    def __verify_account(func):
        def wrapper(self, **kwargs):
            if self.account:
                func(self, **kwargs)
                
            else:
                return "Necessário cadastrar uma conta!"
        
        return wrapper


    def register_user(self):

        idade = int(input("Qual sua idade: "))

        if idade < 18:
            return "Você é menor de idade"
        
        name = str(input("Qual seu nome: "))
        cpf  = str(input("Qual seu cpf: "))

        self.usuario = {
            "Nome": name,
            "CPF": cpf,
            "Idade": idade,
            "Conta": []
        }

        return "Usuário cadastrado !"

    
    def create_bank_account(self):
        
        if self.usuario:

            agency_number   = int(input("Número da agência: "))
            type_account    = str(input("Qual vai ser o tipo da conta: "))
            cpf             = str(input("Qual seu cpf: "))
            password        = str(input("Sua senha: "))
            confirm_password = str(input("Confirme sua senha: "))


            while cpf != self.usuario['CPF']:
                cpf = str(input("CPF incorreto, digite novamente: "))

            while password != confirm_password:
                confirm_password = str(input("Senha incorreta, tente novamente: "))
            
            self.account = {
                "Agência": agency_number,
                "Tipo": type_account,
                "CPF": cpf,
                "Movimentações": self.extract
            }

            return "Conta criada com sucesso!"
        else:
            return "É necessário cadastrar no sistema"

    @__verify_account
    def show_extratct(self):

        withdraw = sum(i for i in self.extract['Saque'])
        deposit = sum(i for i in self.extract['Depósitos'])
        balance_atual = deposit - withdraw

        print(f"Seu extrato é esse: {self.extract} e seu saldo atual é esse: {balance_atual}")

    @__verify_account
    def add_balance(self):

        balance = float(input("Qual o valor do depósito? "))

        self.extract['Depósitos'].append(balance)
    
    @__verify_account
    def withdraw(self):

        balance = float(input("Qual o valor do saque? "))

        self.extract['Saque'].append(balance)



if __name__ == '__main__':

    client = SistemaBancario()
    operation = int(input(
    '''
    Escolha a operação:
    [1] - Depositar
    [2] - Sacar
    [3] - Mostrar extrato
    [4] - Cadastrar usuário
    [5] - Cadastrar conta
    [0] - Sair

    '''))


    while operation != 0:

        if (operation == 1):
            client.add_balance()

        if (operation == 2):
            client.withdraw()

        if (operation == 3):
            client.show_extratct()

        if (operation == 4):
            result = client.register_user()
            print(result)

        if (operation == 5):
            result = client.create_bank_account()
            print(result)
        
        operation = int(input(
    '''
    Qual a próxima operação:
    [1] - Depositar
    [2] - Sacar
    [3] - Mostrar extrato
    [4] - Cadastrar usuário
    [5] - Cadastrar conta
    [0] - Sair
    
    '''))