from classes.maquina_cafe import MaquinaCafe

def main():
    print(" ¡Bienvenido a la Máquina de Café! ")
    #Testing Pipelines
    maquina = MaquinaCafe()

    while True:
        print("\n\t MENÚ PRINCIPAL")
        print("1. Servir café")
        print("2. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mensaje = maquina.dar_vaso_con_cafe()
            print(mensaje)
        elif opcion == "2":
            print(" ¡Gracias por usar la Máquina de Café! Hasta luego.")
            break
        else:
            print(" Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
