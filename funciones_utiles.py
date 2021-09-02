def leer_archivo(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    lineas_sucias = archivo.readlines()
    archivo.close()

    lineas_limpias = []

    for linea in lineas_sucias:
        x = linea.strip("\n")
        lineas_limpias.append(x)

    return lineas_limpias