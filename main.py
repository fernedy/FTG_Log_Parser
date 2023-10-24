from Log2CSV import Log2CSV
from ColorText import ColorText

if __name__ == "__main__":
    try:
        msj = ColorText("Por favor, ingrese el nombre del archivo: ", "1;34")
        nombre_archivo = input(msj.cambiar_color())
        procesador_registros = Log2CSV(nombre_archivo)
        procesador_registros.procesar_registros()
        procesador_registros.escribir_csv()
    except Exception as e:
        print(f"Error: {str(e)}")