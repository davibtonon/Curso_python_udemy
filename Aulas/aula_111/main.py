from classes import *

'''
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É

'''

c1 = Cliente("Luiz", 45)
c1.comprar()

print()

c2 = ClienteVip("Rose", 25, "Miranda")
c2.falar()