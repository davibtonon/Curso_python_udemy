from abc import ABC, abstractmethod


class Pessoa():
    def __init__(self, nome, idade) -> None:
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade


class Cliente(Pessoa):
    def __init__(self, nome, idade) -> None:
        super().__init__(nome, idade)
        self._conta = None

    def adicionar_conta(self, conta):
        self._conta = conta
    
    @property
    def conta(self):
        return self._conta


class Conta():
    def __init__(self, numero_conta, agencia) -> None:
        self.numero_conta = numero_conta
        self._agencia = agencia
        self.__saldo = 0

    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        print(f"R${valor} depositado na conta")
        self.saldo += valor
        self.extrato()

    def extrato(self, limite=None):
        print(f"Conta - {self.numero_conta}")
        print(f"Ag: {self.agencia}")
        print(f"Saldo: R${self.__saldo}")
        if limite:
            print(f"Limite: R${limite}")

    @property
    def agencia(self):
        return self._agencia
        
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            valor = float(valor)

        self.__saldo += valor


class ContaPoupanca(Conta):
    def __init__(self, numero_conta, agencia) -> None:
        super().__init__(numero_conta, agencia)

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"O valor de R${valor} foi sacado")
        else:
            print("Saldo insuficiente")


class ContaCorrente(Conta):
    def __init__(self, numero_conta, agencia, limite=50) -> None:
        super().__init__(numero_conta, agencia)
        self.__limite = limite
  
    def sacar(self, valor):
        if self.saldo + self.__limite >= valor:
            self.saldo -= valor
            print(f"O valor de R${valor} foi sacado da conta")
            self.extrato()
        else:
            print("Saldo insuficiente")
    
    def extrato(self):
        return super().extrato(self.__limite)


class Banco:
    def __init__(self) -> None:
        self.clientes = []
        self.conta = ["xxxx", "aaaa"]
        self.agencias = [9999, 4444, 1111, 2222]
        
    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def verificar_cliente(self, cliente):
        if cliente.conta.agencia not in self.agencias:
            print(f"Agencia não é desse banco")
            return False
        if cliente.conta.numero_conta not in self.conta:
            print(f"Numero da conta não é desse banco")
            return False
        if cliente not in self.clientes:
            print(f"Cliente {cliente.nome} não é desse banco")
            return False
        
        return True

    def cliente_sacar(self, cliente, valor):
        resp = self.verificar_cliente(cliente)
        if resp:
            print("Saque Autorizado")
            cliente.conta.sacar(valor)
        else:
            print("Saque não Autorizado")
    
    def lista_cliente(self):
        print(f"O banco tem {len(self.clientes)} clientes: ")
        for cliente in self.clientes:
            print("- " + cliente.nome)


