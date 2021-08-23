from tokens import Tokenizador, LexerException, Tipo
from matrices import Matriz

class Parser:
    def __init__(self, cadena: str):
        self.cadena = cadena
        self.elementos = []
        self.token = any

    def sig_token(self, lexer):
        try:
            self.token = next(lexer.tokenizar())
        except (StopIteration, LexerException):
            self.token = None

    def validar(self):
        y = self.cadena.find(']', 0, len(self.cadena))

        if y == -1:
            return "Entrada inválida."

        # Tenemos que saber la dimensión de la matriz a introducir.
        # Podemos saber eso analizando primero la primera fila.
        lexer1 = Tokenizador(self.cadena[:y+1])
        self.sig_token(lexer1)

        if not self.parse_a(lexer1):
            return "Entrada inválida."

        dimension = len(self.elementos)
        # Ahora sabemos la dimensión: prosigamos a analizar el
        # resto de la entrada. Al final checaremos si la matriz
        # introducida es cuadrada.
        lexer2 = Tokenizador(self.cadena[y+1:])
        self.sig_token(lexer2)

        if not self.parse_a(lexer2):
            return "Entrada inválida."

        if len(self.elementos) != (dimension ** 2):
            return "La matriz introducida no es cuadrada."

        return Matriz(dimension, self.elementos)

    def parse_a(self, lexer):
        if self.token is not None:
            if self.token.tipo_token == Tipo.LEF_PARENS:
                self.sig_token(lexer)

                if not self.parse_b(lexer):
                    return False

                if not self.parse_a(lexer):
                    return False

        return True

    def parse_b(self, lexer):
        if self.token is not None:
            if self.token.tipo_token == Tipo.NUMERO:
                self.elementos.append(int(self.token.valor))
                self.sig_token(lexer)

                if self.token.tipo_token == Tipo.COMA:
                    self.sig_token(lexer)

                    if self.parse_b(lexer):
                        return True

                if self.token.tipo_token == Tipo.RIG_PARENS:
                    self.sig_token(lexer)
                    return True

            return False

        return False
