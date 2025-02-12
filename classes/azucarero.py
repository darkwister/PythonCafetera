class Azucarero:

    def __init__(self,cant_azucar):
        self.cant_azucar = cant_azucar

    @property
    def cant_azucar(self):
        return self._cant_azucar

    @cant_azucar.setter
    def cant_azucar(self, value):
        if value <= 0:
            raise ValueError("La cantidad de azúcar no puede ser negativa.")
        self._cant_azucar = value

    def has_azucar(self, value):
        return self._cant_azucar > value

    def give_azucar(self, cant_pedida):
        if self.has_azucar(cant_pedida): self.cant_azucar -= cant_pedida
        else: return "No hay suficiente azúcar"