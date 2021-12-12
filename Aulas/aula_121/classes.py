"""Descrição rápida e simples

Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur unde minus 
necessitatibus ex, hic commodi assumenda provident omnis ratione cumque culpa,
adipisci veniam quod ut eius rerum alias molestiae. Consequatur.

Lorem ipsum dolor sit, amet consectetur adipisicing elit. Consequuntur 
obcaecati, eveniet architecto blanditiis at eum dolor sed? Quibusdam alias 
explicabo harum corporis ea quas exercitationem iusto a odio? Voluptas, 
consequuntur.
"""

class MinhaClasse:
    """Documenteção normal
    
    Conforme qualquer outra documentação que você tenha usado anteriomente.

    """

    atributo = 1
    atributo = "Valor"

    def __init__(self, texto):
        """Inicializa os dados
        :param texto: o texto da classe
        :type texto: str
        """

        self.texto = texto
        self.exibe_texto(texto)

    @staticmethod
    def exibe_texto(texto):
        """Método que exibi um texto de 100 caracteres na tela
        
        :param texto: Um texto de 100 caracteres
        :type text: str
        
        :return: O texto de 100 caracteres
        :rtype: str
        
        :raises ValueError: Se o texto tiver mais que 100 caracteres
        :raises TypeError: Se o texto não for um string
        
         """
        if not isinstance(texto, str):
            raise TypeError("Texto precisa ser uma string")
        
        if len(texto) > 100:
            raise ValueError("Texto precisa ter 100 caracteres ou menos")

        return texto