'''
class Arquivo:
    def __init__(self, arquivo, modo):
        print("INIT")
        self.arquivo = open(arquivo, modo)
    
    def __enter__(self):
        print("Abrindo arquivo")
        return self.arquivo
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Fechando arquivo")
        self.arquivo.close()
        print(exc_type)
        print(exc_val)
        print(exc_tb)

        # Tratei a exceção
        return True
    
'''
from contextlib import contextmanager

@contextmanager
def abrir(arquivo, modo):
    try:
        arquivo = open(arquivo, modo)
        print("Abrindo o arquivo")
        yield arquivo
    finally:
        print("Fechando arquivo")
        arquivo.close()

with abrir('abc.txt', 'w') as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.write("Linha 3\n")