from Log2CSV import Log2CSV

if __name__ == "__main__":
    try:
        nombre_archivo = input("Por favor, ingrese el nombre del archivo: ")
        procesador_registros = Log2CSV(nombre_archivo)
        procesador_registros.procesar_registros()
        procesador_registros.escribir_csv()
    except Exception as e:
        print(f"Error: {str(e)}")