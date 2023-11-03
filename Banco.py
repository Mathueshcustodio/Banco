class ContaBancaria:
    def __init__(self, numero, saldo, nome, tipo, limite, status = False):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.status = status
        self.limite = limite

    def ativarconta(self):
        if self.status == False:
            self.status = True
            print('A conta foi ativada')
        else:
            print('Conta já está ativada')

    def depositar(self, valor_deposito):
        if valor_deposito > 0:
            self.saldo += valor_deposito
            self.verificarsaldo()
        else:
            print('Impossivel depositar um valor negativo!')
    def sacar(self, valor_saque):
        if valor_saque <= self.limite:
            self.saldo -= valor_saque
            self.verificarsaldo()
        else:
            print('Seu saque de {} supera o seu limite de {}'.format(valor_saque,self.limite))
    def verificarsaldo(self):
        print('O seu saldo é: R${}'.format_map(self.saldo))


conta = ContaBancaria(665,1000,"V","Corrente",5000)

deposito = int(input('Digite o valor do deposito: '))
conta.depositar(deposito)

saque = int(input('Digite o valor do saque: '))
conta.sacar(saque)