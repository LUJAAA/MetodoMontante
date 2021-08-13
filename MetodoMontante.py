cantidadVariables = 0
matriz = []
matrizIdentidad = []
matrizConIdentidad = []
guardarVariables = []
respuestas = []

def crearMatriz(cantidadVariables, matriz, matrizIdentidad, matrizConIdentidad):
    print("Ingrese la cantidad de varibles")
    cantidadVariables = int(input())
    # Guardo la cantidad de variables en una lista
    guardarVariables.append(cantidadVariables)
    # Matriz Original 
    for i in range(cantidadVariables):
        matriz.append([])
        # El +1 es para el vector de terminos independientes
        for j in range(cantidadVariables+1):
            matriz[i].append(0)

    # Matriz identidad 
    for i in range(cantidadVariables):
        matrizIdentidad.append([])
        for j in range(cantidadVariables):
            if j == i:
                matrizIdentidad[i].append(1)
            else:
                matrizIdentidad[i].append(0)

    filas = columnas = 0
    # llenamos con los datos la matriz
    for columnas in range(0,cantidadVariables):
        for filas in range(0,cantidadVariables+1):
            print(str(columnas)+str(filas), end=" ")
            matriz[columnas][filas] = float(input())

    k=0
    # Matriz original expandida con la matriz identidad
    for i in range(cantidadVariables):
        matrizConIdentidad.append([])
        for o in range(cantidadVariables*2):
            # la primera mitad de las columnas son la matriz original
            if o < cantidadVariables:
                matrizConIdentidad[i].append(float(matriz[i][k]))
            else:# la segunda mitad es la matriz identidad
                matrizConIdentidad[i].append(float(matrizIdentidad[i][k]))

            if k >= cantidadVariables-1:
                k = 0
            else:
                k += 1
def resolverMatriz(cantidadVariables, matriz, matrizIdentidad, matrizConIdentidad):
    # obtenemos la cantidad de variables 
    cantidadVariables = guardarVariables[0]
    listaResultados=[]
    pivoteActual = 0
    pivoteAnterior = 0
    i=0
    print("------------------------------------")
    for i in range(cantidadVariables):
        print("COLUMNA #"+str(i+1)+"--------------------------")
        print("------------------------------------")
        for q in range(cantidadVariables):
            for n in range(cantidadVariables*2):
                print(matrizConIdentidad[q][n],end=" ")
            print(" ")
        # Obtenemos pivotes
        if i == 0:
            pivoteActual = matrizConIdentidad[i][i]
            pivoteAnterior = 1
        else:
            pivoteActual = matrizConIdentidad[i][i]
            pivoteAnterior = matrizConIdentidad[i-1][i-1]
        
        print("Pivote actual = "+str(pivoteActual))
        print("Pivote anterior = "+str(pivoteAnterior))


        for l in range(cantidadVariables):
            if l != i:
                # Filas a modificar 
                for p in range(cantidadVariables*2-(i+1)):
                    # i es la fila actual
                    # l es la fila a modificar
                    # p es la columna actual
                    print("("+str(pivoteActual)+"("+str(matrizConIdentidad[l][p+1+i])+")"+"-"+str(matrizConIdentidad[l][i])+"("+str(matrizConIdentidad[i][p+1+i])+"))"+"/"+str(pivoteAnterior))
                    # "Formula para ir resolviendo cada fila"
                    listaResultados.append(((pivoteActual*matrizConIdentidad[l][p+1+i])-(matrizConIdentidad[l][i]*matrizConIdentidad[i][p+1+i]))/pivoteAnterior)
                # Ingresamos eso datos a las fila correspondiente
                y=0
                for w in range(cantidadVariables*2):       
                    if w > i:
                        matrizConIdentidad[l][w] = listaResultados[y]
                        y+=1
                    else:
                        matrizConIdentidad[l][w] = 0
                print(listaResultados)
                listaResultados = []
        print("------------------------------------")
    print(" ")
    print("Calculando las soluciones")
    for u in range(cantidadVariables):
        res = 0
        for a in range(cantidadVariables):
            print(str(matriz[a][cantidadVariables])+"*("+str(matrizConIdentidad[u][cantidadVariables+a])+"/"+str(pivoteActual)+") ",end=" ")
            res += matriz[a][cantidadVariables]*(matrizConIdentidad[u][cantidadVariables+a]/pivoteActual)
        respuestas.append(res)
        print(" ")
    print(" ")
    print("Soluciones="+str(respuestas))
    print(" ")
    print("------------------------------------")

# Se llaman a las funciones 
crearMatriz(cantidadVariables, matriz, matrizIdentidad, matrizConIdentidad)
resolverMatriz(cantidadVariables, matriz, matrizIdentidad, matrizConIdentidad)


