class Matriz:
    def __init__(self, dimension: int, elementos: list):
        self.dimension = dimension
        self.elementos = elementos
        self.determinante = None

    def posicion(self, i: int, j: int):
        return self.elementos[self.dimension * i + j]

    def solucionar(self, independientes: list):
        pivote_anterior = 1

        # k: posición del pivote.
        # i: fila
        # j: columna.
        for k in range(self.dimension):
            pivote_actual = self.posicion(k, k)

            for i in range(k + 1, self.dimension):
                for j in range(k + 1, self.dimension):
                    self.elementos[i * self.dimension + j] = (self.posicion(i, j) * pivote_actual - self.posicion(i, k) * self.posicion(k, j)) / pivote_anterior

                independientes[i] = (independientes[i] * pivote_actual - self.posicion(i, k) * independientes[k]) / pivote_anterior
            # Ahora a calcular las posiciones que están encima del pivote.
            for i in range(0, k):
                for j in range(k + 1, self.dimension):
                    self.elementos[i * self.dimension + j] = (self.posicion(i, j) * pivote_actual - self.posicion(i, k) * self.posicion(k, j)) / pivote_anterior

                independientes[i] = (independientes[i] * pivote_actual - self.posicion(i, k) * independientes[k]) / pivote_anterior

            pivote_anterior = pivote_actual

        self.determinante = self.posicion(self.dimension - 1, self.dimension - 1)

        for i in range(len(independientes)):
            independientes[i] /= self.determinante

        return independientes
    
    def __str__(self):
        pass
