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
