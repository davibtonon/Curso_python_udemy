"""
Resolução do desafio da aula 122.
    Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
    Criar um sistema bancário (extremamente simples) que tem cliente,
    contas e um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente)
    e que possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
    Banco de clientes e contas.
"""
from classes import Cliente
from classes import ContaCorrente, ContaPoupanca
from classes import Banco

davi = Cliente("Davi", 25)
joao = Cliente("Joao", 35)

joao.adicionar_conta(ContaPoupanca('iiiii', 4444))
davi.adicionar_conta(ContaCorrente("xxxx", 9999))

banco = Banco()

banco.adicionar_cliente(davi)
banco.adicionar_cliente(joao)

banco.lista_cliente()
