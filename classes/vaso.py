# class Vaso:
#
#     def __init__(self, cant_contenido):
#         self.cant_vaso = 10
#         self.cant_contenido = cant_contenido
#
#     @property
#     def cant_vaso(self):
#         return self._cant_vaso
#
#     @cant_vaso.setter
#     def cant_vaso(self, value):
#         if value < 0:
#             raise ValueError("La cantidad de vasos no puede ser negativa.")
#         self._cant_vaso = value
#
#     def has_vaso(self, value):
#         return self._cant_vaso > value
#
#     def give_vaso(self, cant_vaso):
#         if self.has_vaso(cant_vaso):
#             self.cant_vaso -= cant_vaso
#             return f"Suplidos {cant_vaso} vasos"
#         else: return "No hay mas vasos"

class Vaso:
    def __init__(self, capacidad_oz):
        self.capacidad_oz = capacidad_oz
        self.stock = 10

    @property
    def stock(self):
        return self._stock

    # def restock(self,cant):
    #     self._stock += cant
    #     return self._stock

    @stock.setter
    def stock(self, value):
        if value <= 0:
            raise ValueError("La cantidad de vasos no puede ser negativa.")
        self._stock = value

    def has_vasos(self, cantidad):
        return self.stock >= cantidad

    def give_vaso(self, cantidad):
        if self.has_vasos(cantidad):
            self.stock -= cantidad
            return f"✅ Suplidos {cantidad} vasos de {self.capacidad_oz}oz."
        else:
            return "❌ No hay más vasos en stock."


class VasoFactory:
    @staticmethod
    def create_vaso(size):
        sizes = {8: "pequeño", 12: "mediano", 16: "grande"}
        if size in sizes:
            return Vaso(size)
        raise ValueError("❌ Tamaño de vaso no disponible.")



