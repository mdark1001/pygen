"""
@author miguelCabrera1001 | 
@date 11/12/19
@project 
@name aptitud
"""


class Aptitud(object):
    """
      Calcular la aptitud de las
    """

    def __init__(self, suma, producto, duplicados):
        self.suma = suma
        self.producto = producto
        self.duplicados = duplicados
        diferenciaProducto = abs(360 - producto)
        diferenciaSuma = abs(36 - suma)
        self.diferenci_total = diferenciaSuma - diferenciaProducto

    def __gt__(self, other):
        if self.duplicados != other.duplicados:
            return self.duplicados < other.duplicados
        return self.diferenci_total < other.diferenci_total

    def __str__(self):
        return "SUM: {}  Prod: {} dups {}".format(self.suma, self.producto, self.duplicados)
