class Vaso:
    def __init__(self, capacidad_oz):
        self.capacidad_oz = capacidad_oz
        self.stock = 10

    @property
    def stock(self):
        return self._stock

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



