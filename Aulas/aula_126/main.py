from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict, astuple
'''
    param eq: Controla se é possivel fazer igualdade ou não
    param repr:
    param order: False > Não permiti classifica os itens
    param init: Escolhe se faz o initi ou não
    '''


@dataclass(eq=True, repr=False, order=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome: str  # =field(repr=False) oculta o camo

    def __post_init__(self):
        # self.nome_completo = f"{self.nome} {self.sobrenome}"
        if not isinstance(self.nome, str):
            raise TypeError(
                f"Tipo inválido {type(self.nome).__name__} != str em{self}")

    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"


p1 = Pessoa("A", "5")
p2 = Pessoa("C", "4")
p3 = Pessoa("D", "6")
p4 = Pessoa("B", "3")


pessoas = [p1, p2, p3, p4]

print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome, reverse=True))

# print(p1)
# print(p1 == p2)


# print(p1.nome)
# print(p1.sobrenome)
# print(p1.nome_completo)

print(asdict(p1))
print(astuple(p1))