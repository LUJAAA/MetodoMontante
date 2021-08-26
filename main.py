from parser_class import Parser

my_parser = Parser("[2, 1, -2] [3, 2, 1] [-2, 1, 3]")
independientes = [-3, 3, 3]
matriz = my_parser.validar()
print(matriz.solucionar(independientes))
