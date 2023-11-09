# Clase ColorText: Esta clase se utiliza para cambiar el color de un texto en la terminal utilizando códigos ANSI.

# Constructor (__init__): El constructor de la clase toma dos parámetros, 'text' y 'color_code'. 'text' es el texto
# que se desea colorear, y 'color_code' es el código ANSI que representa el color deseado.

# Atributos:
# - color_code: Almacena el código ANSI del color especificado.
# - text: Almacena el texto que se va a colorear.
# - color_final: Almacena el texto coloreado después de aplicar el código ANSI.

# Método cambiar_color: Este método se encarga de aplicar el código ANSI al texto y devolver el texto coloreado.
# Utiliza el formato '\033[<color_code>m<text>\033[0m' para cambiar el color del texto y restablecerlo al color
# original después del texto. El resultado se almacena en el atributo 'color_final'.

# Manejo de excepciones: El método maneja excepciones y puede generar una excepción en caso de error al cambiar el
# color del texto.

# Ejemplo de uso: Para usar esta clase, se crea una instancia de ColorText con el texto y el código de color deseados
# y luego se llama al método 'cambiar_color' para obtener el texto coloreado.

# Ejemplo:
# color_text = ColorText("Hola, mundo!", 31)  # Crear una instancia con texto y código de color rojo.
# texto_coloreado = color_text.cambiar_color()  # Obtener el texto coloreado.
# print(texto_coloreado)  # Imprimir el texto con el color aplicado.

# Nota: Asegúrate de que el entorno en el que se ejecuta el código sea compatible con los códigos ANSI para ver los
# colores correctamente en la terminal.

class ColorText:
    def __init__(self, text, color_code,):
        self.color_code = color_code
        self.text = text
        self.color_final = set()

    def cambiar_color(self):
        try:
            self.color_final = f"\033[{self.color_code}m{self.text}\033[0m"
            return self.color_final
        except Exception as e:
            raise Exception(f"Error al cambiar el color del texto: {str(e)}")
