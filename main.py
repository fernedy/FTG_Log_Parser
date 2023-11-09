# Este bloque de código se encarga de ejecutar el proceso de conversión de un archivo de registros a un archivo CSV.

# Importación de módulos y clases:
# - Importa las clases 'Log2CSV' y 'ColorText' desde sus respectivos módulos para habilitar la funcionalidad necesaria.

# Bloque principal:
# - Comprueba si el script se está ejecutando como programa principal (no importado como módulo).
# - Si es así, continúa con la ejecución del proceso de conversión.

# Solicitud de entrada del nombre del archivo: - Utiliza la clase 'ColorText' para mostrar un mensaje en color que
# solicita al usuario ingresar el nombre del archivo de registros. - Captura la entrada del usuario y almacena el
# nombre del archivo en la variable 'nombre_archivo'.

# Creación de una instancia de 'Log2CSV':
# - Crea una instancia de la clase 'Log2CSV' pasando el nombre del archivo como parámetro.

# Procesamiento de registros y escritura de CSV:
# - Llama al método 'procesar_registros' en la instancia de 'Log2CSV' para procesar el archivo de registros.
# - Llama al método 'escribir_csv' para escribir los registros procesados en un archivo CSV.

# Captura de excepciones: - En caso de que ocurra una excepción durante el proceso, captura el error y muestra un
# mensaje de error en la consola.

# Nota: Los módulos 'Log2CSV' y 'ColorText' se utilizan para habilitar la funcionalidad de procesamiento de registros
# y colores en la consola.

# Ejemplo de uso: Cuando se ejecuta este script, solicitará al usuario que ingrese el nombre del archivo de registros
# y luego realizará la conversión a CSV. Si se produce un error durante el proceso, mostrará un mensaje de error en
# la consola.

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