from mascota import Perro, Gato, Conejo
import funciones_utiles

def cargar_mascotas(archivo_mascotas):
    # COMPLETAR
    info_no_separada = funciones_utiles.leer_archivo("mascotas.csv")
    info_no_separada = info_no_separada[1:]
    info = []

    for i in info_no_separada:
        x = i.split(",")
        info.append(x)

    mascotas_obj = [] 

    for m in info:
        tipo = m[1]
        if tipo.lower() == "perro":
            mascota = Perro(m[0], m[2], m[3], int(m[4]), int(m[5]))
        elif tipo.lower() == "gato":
            mascota = Gato(m[0], m[2], m[3], int(m[4]), int(m[5]))
        elif tipo.lower() == "conejo":
            mascota = Conejo(m[0], m[2], m[3], int(m[4]), int(m[5]))  

        mascotas_obj.append(mascota)

    return mascotas_obj      


