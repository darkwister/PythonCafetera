from classes.cafetera import Cafetera
from classes.vaso import VasoFactory
from classes.azucarero import Azucarero

class MaquinaCafe:
    def __init__(self):
        self.cafe = Cafetera(1000)
        self.azucar = Azucarero(500)
        self.vasos = {
            8: VasoFactory.create_vaso(8),
            12: VasoFactory.create_vaso(12),
            16: VasoFactory.create_vaso(16),
        }

    def dar_vaso(self):
        print("\tELIGE EL TAMAÑO DEL VASO")
        print("1. Vaso pequeño 8oz")
        print("2. Vaso mediano 12oz")
        print("3. Vaso grande 16oz")

        opciones = {1: 8, 2: 12, 3: 16}
        try:
            opc = int(input("Opción: "))
            size = opciones.get(opc)
            if size:
                return self.vasos[size].give_vaso(1)
            else:
                print("❌ Opcion invalida")
                return None
        except ValueError:
            print("❌ Entrada invalida, ingrese un numero valido.")
            return None

    def dar_vaso_con_cafe(self):
        resultado_vaso = self.dar_vaso()
        if not resultado_vaso or "❌" in resultado_vaso:
            return "No tienes un vaso disponible."

        print(resultado_vaso)

        size = next((s for s, v in self.vasos.items() if v.stock >= 0), None)
        if size is None:
            return "No se pudo determinar el tamaño del vaso."

        # cant_cafe = int(input(f"☕ ¿Cuántos ml de café desea en su vaso de {size}oz?: "))
        # if self.cafe.has_cafe(cant_cafe) and cant_cafe > 0 and cant_cafe > self.cafe.cant_cafe * 30:
        #     self.cafe.give_cafe(cant_cafe)
        # else:
        #     return "❌ No hay suficiente café."

        while True:
            try:
                cant_cafe = int(input(f"Cuantos ml de cafe desea en su vaso de {size}oz?: "))
                if cant_cafe <= 0 or cant_cafe > size * 30:  # Aproximadamente 30 ml por onza
                    print("Cantidad invalida. Ingrese un valor entre 1ml y el tamaño maximo del vaso.")
                elif not self.cafe.has_cafe(cant_cafe):
                    print("No hay suficiente cafe disponible.")
                else:
                    break
            except ValueError:
                print("Entrada invalida. Ingrese un numero valido.")

        self.cafe.give_cafe(cant_cafe)

        opc_azucar = input("Desea agregar azúcar? (s/n): ").strip().lower()
        cant_azucar = 0
        if opc_azucar == "s":
            cant_azucar = int(input("Cuantos gramos de azúcar desea?: "))
            if self.azucar.has_azucar(cant_azucar) and cant_azucar > 0:
                self.azucar.give_azucar(cant_azucar)
            else:
                return "No hay suficiente azúcar."

        return f"Vaso {size}oz con {cant_cafe}ml de café y {cant_azucar}g de azúcar servido. \n\tDisfrute su café!"
