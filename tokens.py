from matrices import Matriz
from dataclasses import dataclass
from enum import Enum


class LexerException(Exception):
    def __init__(self):
        self.message = "Carácter inválido."


class Tipo(Enum):
    LEF_PARENS = 0
    RIG_PARENS = 1
    NUMERO = 2
    COMA = 3


@dataclass
class Token:
    tipo_token: Tipo
    valor: str

    def __str__(self):
        return f"Tipo: {self.tipo_token} Valor: {self.valor}"



class Tokenizador:
    def __init__(self, cadena: str):
        self.cadena = cadena.replace(' ', '')
        self.puntero = 0

    def formar_numero(self):
        numero = ""

        # Número con signo negativo.
        if self.cadena[self.puntero] == '-':
            numero += self.cadena[self.puntero]
            self.puntero += 1

        while self.puntero < len(self.cadena) and self.cadena[self.puntero].isnumeric():
            numero += self.cadena[self.puntero]
            self.puntero += 1

        return numero

    def tokenizar(self):
        while self.puntero < len(self.cadena):
            if self.cadena[self.puntero] == '[':
                self.puntero += 1
                yield Token(Tipo.LEF_PARENS, '[')
            elif self.cadena[self.puntero] == ']':
                self.puntero += 1
                yield Token(Tipo.RIG_PARENS, ']')
            elif self.cadena[self.puntero] == ',':
                self.puntero += 1
                yield Token(Tipo.COMA, ',')
            elif self.cadena[self.puntero] == '-' or self.cadena[self.puntero].isnumeric():
                yield Token(Tipo.NUMERO, self.formar_numero())
            else:
                raise LexerException
