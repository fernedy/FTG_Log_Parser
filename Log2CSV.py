# Clase Log2CSV: Esta clase se utiliza para procesar archivos de registros y convertirlos en archivos CSV.

# Importación de bibliotecas: - csv: Utilizada para trabajar con archivos CSV. - re: Utilizada para buscar patrones
# en el texto a través de expresiones regulares. - codecs: Utilizada para manejar diferentes codificaciones de
# caracteres en el archivo. - os: Utilizada para operaciones relacionadas con el sistema operativo,
# como la manipulación de rutas de archivos y directorios.

# Importación de la clase 'ColorText' desde el módulo 'ColorText' para habilitar el cambio de colores de texto en la
# consola.

# Constructor (__init__): - Recibe el parámetro 'fileName', que es el nombre del archivo de registros que se
# procesará. - Inicializa varios atributos para almacenar información procesada y controlar la ubicación del archivo
# CSV resultante.

# Método procesar_registros: - Este método se encarga de procesar el archivo de registros. Abre el archivo,
# busca patrones en el texto y crea un diccionario para cada evento registrado. - Los eventos se almacenan en una
# lista llamada 'events'. - Cualquier error durante el procesamiento se captura y se lanza una excepción.

# Método escribir_csv: - Este método se encarga de escribir los registros procesados en un archivo CSV. - Itera a
# través de los diccionarios de eventos para compilar una lista única de encabezados. - Luego, crea un nuevo archivo
# CSV y escribe los encabezados y datos en él. - Muestra un mensaje de finalización con información sobre el número
# de filas escritas y la ubicación del archivo CSV resultante. - Captura y maneja cualquier error que pueda ocurrir
# durante la escritura.

# Nota: La clase utiliza la biblioteca 'ColorText' para resaltar mensajes en colores en la consola.

# Ejemplo de uso: Para utilizar esta clase, se debe crear una instancia de 'Log2CSV' con el nombre del archivo de
# registros y luego llamar a los métodos 'procesar_registros' y 'escribir_csv' para realizar la conversión a CSV.

import csv  # Importa la biblioteca CSV para trabajar con archivos CSV.
import re  # Importa la biblioteca de expresiones regulares para buscar patrones en el texto.
import codecs  # Importa la biblioteca codecs para manejar diferentes codificaciones de caracteres.
import os  # Importa el módulo 'os' para acceder a funcionalidades relacionadas con el sistema operativo,
# como la manipulación de rutas de archivos y directorios, gestión de variables de entorno y más.
from ColorText import ColorText # Importa la clase 'ColorText' desde el módulo 'ColorText' para habilitar el cambio
# de colores de texto en la consola.


class Log2CSV:
    def __init__(self, fileName):
        self.fileName = fileName
        self.events = []
        self.headers = []
        self.current_directory = set()
        self.color_msj = set()

    def procesar_registros(self):
        try:
            self.current_directory = os.getcwd() + "\Log" + "\\"
            print(f"[+] Leyendo registros de {self.fileName}")
            with codecs.open(self.current_directory + self.fileName, "r", encoding="UTF-8") as log_data:
                search_pattern = re.compile('(\w+)(?:=)(?:"{1,3}([\w\-\.:\ =]+)"{1,3})|(\w+)=(?:([\w\-\.:\=]+))')
                for line in log_data:
                    event = {}  # Crea un diccionario vacío para cada evento.
                    match = search_pattern.findall(line)  # Encuentra todas las coincidencias en la línea actual.
                    for group in match:
                        if group[0] != "":
                            event[group[0]] = group[1]  # Agrega un par clave-valor al diccionario 'event'.
                        else:
                            event[group[2]] = group[3]
                    self.events.append(event)  # Agrega el diccionario 'event' a la lista 'events'.

        except Exception as e:
            self.color_msj = ColorText(f"Error al leer o procesar el archivo de registros: {str(e)}", "31")
            raise Exception(self.color_msj.cambiar_color())

    def escribir_csv(self):
        try:
            # Itera a través de los diccionarios de eventos para compilar una lista única de encabezados.
            self.current_directory = os.getcwd() + "\Log" + "\\"
            print(f"[+] Procesando campos de registro")
            for row in self.events:
                for key in row.keys():
                    if key not in self.headers:
                        self.headers.append(key)
            print(f"[+] Escribiendo CSV")
            newFile = self.fileName.split('.')[0] + '.csv'
            with codecs.open(self.current_directory + newFile, "w", encoding="UTF-8") as archivo_csv:
                csvfile = csv.DictWriter(archivo_csv, self.headers)
                csvfile.writeheader()  # Escribe los encabezados en el archivo CSV.
                for row in self.events:
                    csvfile.writerow(row)  # Escribe los datos en el archivo CSV.
            self.color_msj = ColorText(f"[+] Finalizado - {str(len(self.events))} filas escritas en {newFile}", "32")
            print(f"{self.color_msj.cambiar_color()}")
            print(f"[+] Ubicación del Archivo: {self.current_directory}")

        except Exception as e:
            self.color_msj = ColorText(f"Error al escribir en el archivo CSV: {str(e)}", "31")
            raise Exception(self.color_msj.cambiar_color())



