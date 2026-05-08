
def put(value, lst):
    """
    Coloca value en el primer lugar vacio ("") que encuentre en lst
    y retorna el indice donde lo coloco.
    Si no hay ningun lugar vacio, retorna -1.
    IMPORTANTE: esta funcion modifica la lista original.

    Ejemplo:
        colors = ["Red", "", "Green"]
        put("Blue", colors) -> 1
        # colors ahora es ["Red", "Blue", "Green"]
    """
    
    i = 0
    for word in lst:
        if word == "":
            lst[i] = value
            return i
        i += 1
    return -1
            


def remove(value, lst):
    """
    Busca todas las ocurrencias de value en lst, las reemplaza por ""
    y retorna la cantidad de eliminaciones realizadas.
    IMPORTANTE: esta funcion modifica la lista original.

    Ejemplo:
        colors = ["Red", "Green", "Red", "Blue"]
        remove("Red", colors) -> 2
        # colors ahora es ["", "Green", "", "Blue"]
    """
    deleted = 0
    for i, word in enumerate(lst):
        if word == value:
            lst[i] = ""
            deleted += 1
    return deleted