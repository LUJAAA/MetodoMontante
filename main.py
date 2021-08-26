from parser_class import Parser
from matrices import PivoteNulo
import os
import sys


def main():
    while True:
        independientes = []

        try:
            entrada = input(">> ")
        except EOFError:
            print("Adiós!")
            sys.exit()

        input_parser = Parser(entrada)
        matriz = input_parser.validar()

        # Si ocurrieron errores.
        if isinstance(matriz, str):
            print(matriz)
            continue

        i = 0
        while i < matriz.dimension:
            try:
                independientes.append(int(input(f"Término independiente {i+1}: ")))
            except ValueError:
                print("Introduzca un valor entero.\n")
                continue
            except EOFError:
                print("Adiós!")
                sys.exit()

            i += 1

        try:
            resultados = matriz.solucionar(independientes)
        except PivoteNulo as e:
            print(e.message)
            continue

        print(independientes)

if __name__ == "__main__":
    main()
