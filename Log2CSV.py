import csv  # Importa la biblioteca CSV para trabajar con archivos CSV.
import re  # Importa la biblioteca de expresiones regulares para buscar patrones en el texto.
import codecs  # Importa la biblioteca codecs para manejar diferentes codificaciones de caracteres.
import os  # Importa el módulo 'os' para acceder a funcionalidades relacionadas con el sistema operativo,


# como la manipulación de rutas de archivos y directorios, gestión de variables de entorno y más.


class Log2CSV:
    def __init__(self, fileName):
        self.fileName = fileName
        self.events = []
        self.headers = []
        self.current_directory = set()

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
            raise Exception(f"Error al leer o procesar el archivo de registros: {str(e)}")

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
            print(f"[+] Finalizado - {str(len(self.events))} filas escritas en {newFile}")
            print(f"[+] Ubicación del Archivo: {self.current_directory}")

        except Exception as e:
            raise Exception(f"Error al escribir en el archivo CSV: {str(e)}")
