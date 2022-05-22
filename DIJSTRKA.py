# --- IMPLEMENTAR SOLO LA FUNCION dijkstra ----
def dijkstra(N, INI, FIN, PRECIOS):
    lista = []
    for i in range(N):
        lista.append([False, 99999999, -1])
    true = True
    lista[INI][1] = 0
    while true:
        minimo = 999999999
        for i in range(len(lista)):
            if lista[i][0] == False:
                if minimo > lista[i][1]:
                    minimo = lista[i][1]
                    x = i
        v = []
        for i in len(precios[x]):
            if precios[x][i] != -1:
                v.append(i)
        for i in v:
            if lista[x][1] + precio[x][i] < lista[v][1]:
                lista[v][i] = lista[x][1] + precio[x][i]
                lista[v][2] = x
        lista[x][0] = True
        c = 0
        for i in range(len(lista)):
            if lista[i][0] == True:
                c += 1
        if c == N:
            true = False
    precio = lista[FIN][1]
    x = 999999
    ciudad = FIN
    while x != -1:
        x = lista[ciudad][2]
        if x != -1:
            ruta.append(x)
            ciudad = x
    ruta = ruta[::-1]

    return [precio, ruta]
    # 1- CREAR LA TABLA DIJKSTRA
    # * Crear tabla T con todo False, 99999999, -1
    # * Actualizar INI a 0

    # 2- ACTUALIZAR LA TABLA HASTA VISITAR TODOS
    # * Mientras falten por visitar
    # * Buscar ciudad 'x' con el menor 'precio mas barato desde INI' no visitada
    # * Buscar 'vs' (todos los vecinos no visitados de 'x')
    # * Para cada vecino 'v' de 'vs', ver si actualizamos la tabla T
    # * Marcar 'x' como visitada

    # 3- CALCULAR RUTA Y PRECIO
    # * El precio esta directamente en la tabla
    # * La ruta es ir encadenando 'ciudad previa' desde FIN a INI y darle la vuelta


# -------------------------------------------


# -------------------------
# ------NO MODIFICAR ------
N = int(input())
INI = int(input())
FIN = int(input())

PRECIOS = []
for c in range(0, N):
    ss = input().split(",")
    precio = []
    for s in ss:
        precio.append(int(s))
    PRECIOS.append(precio)

res = dijkstra(N, INI, FIN, PRECIOS)

print("Precio:", res[0])
print("Ruta:", res[1])
# -------------------------
# -------------------------