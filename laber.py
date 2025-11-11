import os

def leer_laberinto(filename):
    if not os.path.exists(filename):
        print(f"Error: El archivo '{filename}' no existe.")
        return None, None, None, 0, 0

    with open(filename, 'r') as f:
        try:
            rows = int(f.readline().strip())
            cols = int(f.readline().strip())
        except ValueError:
            print("Error: Formato de dimensiones incorrecto en el archivo.")
            return None, None, None, 0, 0

        maze = []
        start = None
        goal = None
        for r in range(rows):
            line = list(f.readline().strip())
            if len(line) != cols:
                print(f"Error: La fila {r} no tiene las {cols} columnas esperadas.")
                return None, None, None, 0, 0
            for c in range(cols):
                if line[c] == 'E':
                    start = (r, c)
                elif line[c] == 'S':
                    goal = (r, c)
            
            maze.append(line)
        
        if start is None or goal is None:
            print("Error: El laberinto debe contener una 'E' (Entrada) y una 'S' (Salida).")
            return None, None, None, 0, 0
            
        return maze, start, goal, rows, cols

def resolver_laberinto(maze, start, goal, rows, cols):
    pila = []
    visitado = set()

    pila.append(start)
    visitado.add(start)

    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pila:
        (fila_actual, col_actual) = pila[-1]

        if (fila_actual, col_actual) == goal:
            return pila

        encontro_camino = False
        for df, dc in movimientos:
            nueva_fila, nueva_col = fila_actual + df, col_actual + dc

            if 0 <= nueva_fila < rows and 0 <= nueva_col < cols:
                celda = maze[nueva_fila][nueva_col]
                
                if celda != '1' and (nueva_fila, nueva_col) not in visitado:
                    pila.append((nueva_fila, nueva_col))
                    visitado.add((nueva_fila, nueva_col))
                    encontro_camino = True
                    break 
        if not encontro_camino:
            pila.pop()

    return None

def imprimir_ruta(ruta):
    if ruta:
        print("¡Se encontró una ruta de solución!")
        print(" -> ".join(map(str, ruta)))
    else:
        print("No se encontró ninguna ruta de solución.")

if __name__ == "__main__":
    
    archivo_laberinto = "laberinto.txt" 
    
    maze, start, goal, rows, cols = leer_laberinto(archivo_laberinto)

    if maze:
        print("Resolviendo el laberinto...")
        ruta_solucion = resolver_laberinto(maze, start, goal, rows, cols)
    
        imprimir_ruta(ruta_solucion)