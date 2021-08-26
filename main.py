from parser_class import Parser
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
        if type(matriz) is str:
            print(matriz)
            continue

        for i in range(matriz.dimension):
            independientes.append(int(input(f"Término independiente {i+1}: ")))

        resultados = matriz.solucionar(independientes)
        print(independientes)

if __name__ == "__main__":
    main()
