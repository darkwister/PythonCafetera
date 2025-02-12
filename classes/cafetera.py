class Cafetera:

    def __init__(self,cant_cafe):
        self.cant_cafe = cant_cafe

    @property
    def cant_cafe(self):
        return self._cant_cafe

    @cant_cafe.setter
    def cant_cafe(self, value):
        if value <= 0:
            raise ValueError("La cantidad de café no puede ser negativa.")
        self._cant_cafe = value

    def has_cafe(self, value):
        return self._cant_cafe > value

    def give_cafe(self, cant_pedida):
        if self.has_cafe(cant_pedida): self.cant_cafe -= cant_pedida
        else: return "Bueno manito, se acabo el cafe"