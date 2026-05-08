
def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    new_list = []
    for lst in matrix:
        for item in lst:
            new_list.append(item)
    return new_list



def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    new_lst= []
    for lst in matrix:
        new_lst.append(sum(lst))
    return new_lst




def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    new_lst = []
    for i in range(len(matrix[0])):
        col_sum = 0
        for lst in matrix:
            col_sum += lst[i]
        new_lst.append(col_sum)
    return new_lst

