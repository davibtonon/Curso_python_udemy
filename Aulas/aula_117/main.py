class A:
   
    def __init__(self) -> None:
        print("Eu sou o INIT")

    def __call__(self, *args, **kwargs):
        resultado = 1

        for i in args:
            resultado *= i
        
        return resultado
    
    def __str__(self) -> str:
        return "Essa é a class A criada para tal coisa"
a = A()

print(a)