"""Descrição rápida e simples

Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur unde minus 
necessitatibus ex, hic commodi assumenda provident omnis ratione cumque culpa,
adipisci veniam quod ut eius rerum alias molestiae. Consequatur.

Lorem ipsum dolor sit, amet consectetur adipisicing elit. Consequuntur 
obcaecati, eveniet architecto blanditiis at eum dolor sed? Quibusdam alias 
explicabo harum corporis ea quas exercitationem iusto a odio? Voluptas, 
consequuntur.
"""

variavel_1 = "valor 1"

def soma(x, y):
    """
    Soma x e y
    
    :param x: Número1
    :type x: int or float
    :param y: Número 2
    :type y: int or float

    :return: A soma entre x e y
    :return: int or float
    """
    return x + y

def multiplica(x, y, z=None):
    """Mutiplica x, y, z
    
    Multiplica x, y e z. O programador pode omitir a variável z caso não tenha
    necessidade de usá-la
    
    :param x: Número 1
    :type x: int or float
    :param y: Número 2
    :type y: int or float
    :param z: Número 3 (optional)
    :type z: int, float or None

    return: A soma entre x, y e z
    :rtype: int or float
    """


    if z:
        return x *y
    else:
        return x * y * z
