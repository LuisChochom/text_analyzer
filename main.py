import os
import tkinter as tk
from tkinter import filedialog

class TextAnalyzer:
    """
    Clase encargada del análisis del texto.
    Encapsula:
        - texto original
        - texto normalizado
        - tokens
        - conteos
    """

    def __init__(self, text: str):
        if not isinstance(text, str):
            raise TypeError("El texto debe ser un string.")
        if text.strip() == "":
            raise ValueError("El texto está vacío.")

        self.original_text = text
        self.normalized_text = ""
        self.tokens = []
        self.counts = {}
        self.unique_tokens = set()

    # ----------------------------------------------
    # Método principal de análisis
    # ----------------------------------------------
    def analyze(self):
        self.normalized_text = self._normalize_text(self.original_text)
        self.tokens = self._tokenize(self.normalized_text)
        self.counts = self._count_tokens(self.tokens)
        self.unique_tokens = set(self.tokens)

    # ----------------------------------------------
    # Métodos internos
    # ----------------------------------------------
    def _normalize_text(self, text: str) -> str:
        cleaned = ""
        for char in text.lower():
            if char.isalnum() or char.isspace():
                cleaned += char
            else:
                cleaned += " "
        return cleaned

    def _tokenize(self, text: str) -> list[str]:
        return text.split()

    def _count_tokens(self, tokens: list[str]) -> dict:
        counts = {}
        for token in tokens:
            counts[token] = counts.get(token, 0) + 1
        return counts

    # ----------------------------------------------
    # Reporte en consola
    # ----------------------------------------------
    def report(self):
        if not self.tokens:
            raise RuntimeError("Debe ejecutar analyze() antes de generar el reporte.")

        total_tokens = len(self.tokens)
        total_unique = len(self.unique_tokens)

        sorted_tokens = sorted(
            self.counts.items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]

        avg_length = sum(len(t) for t in self.tokens) / total_tokens

        max_len = max(len(t) for t in self.tokens)
        min_len = min(len(t) for t in self.tokens)

        longest = [w for w in self.unique_tokens if len(w) == max_len]
        shortest = [w for w in self.unique_tokens if len(w) == min_len]

        print("\n===== REPORTE =====")
        print(f"Total tokens: {total_tokens}")
        print(f"Tokens únicos: {total_unique}")
        print(f"Longitud promedio: {avg_length:.2f}")
        print(f"Palabras más largas: {longest}")
        print(f"Palabras más cortas: {shortest}")

        print("\nTop 10 tokens más frecuentes:")
        for token, count in sorted_tokens:
            print(f"{token} -> {count}")

    # ----------------------------------------------
    # Consulta interactiva
    # ----------------------------------------------
    def query(self, word: str):
        if not self.tokens:
            raise RuntimeError("Debe ejecutar analyze() antes de consultar.")

        word = word.lower()

        if word not in self.counts:
            print(f"La palabra '{word}' no aparece en el texto.")
            return

        frequency = self.counts[word]
        total = len(self.tokens)
        percentage = (frequency / total) * 100

        if frequency == 1:
            classification = "rara"
        elif frequency >= 5:
            classification = "común"
        else:
            classification = "moderada"

        print(f"\nPalabra: {word}")
        print(f"Frecuencia: {frequency}")
        print(f"Porcentaje: {percentage:.2f}%")
        print(f"Clasificación: {classification}")


# ==================================================
# FUNCIONES DE ENTRADA
# ==================================================

def read_text_from_console() -> str:
    text = input("Ingrese el texto:\n")
    if text.strip() == "":
        raise ValueError("El texto ingresado está vacío.")
    return text


def select_file_gui() -> str:
    """
    Abre un explorador gráfico para seleccionar archivo .txt
    """
    root = tk.Tk()
    root.withdraw()  # Oculta ventana

    file_path = filedialog.askopenfilename(
        title="Seleccionar archivo de texto",
        filetypes=[("Archivos de texto", "*.txt")]
    )

    if not file_path:
        raise ValueError("No se seleccionó ningún archivo.")

    return file_path


def read_text_from_file(path: str) -> str:
    if not os.path.exists(path):
        raise FileNotFoundError("Archivo no encontrado.")

    if not os.path.isfile(path):
        raise ValueError("Ruta inválida.")

    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()

        if content.strip() == "":
            raise ValueError("El archivo está vacío.")

        return content

    except OSError:
        raise OSError("Error de lectura del archivo.")


# ==================================================
# PROGRAMA PRINCIPAL
# ==================================================

def main():
    try:
        print("1. Ingresar texto por consola")
        print("2. Leer texto desde archivo (.txt)")

        option = input("Seleccione opción (1/2): ")

        if option == "1":
            text = read_text_from_console()

        elif option == "2":
            path = select_file_gui()
            text = read_text_from_file(path)

        else:
            raise ValueError("Opción inválida.")

        analyzer = TextAnalyzer(text)
        analyzer.analyze()
        analyzer.report()

        # ===============================
        # CONSULTAS INTERACTIVAS
        # ===============================
        while True:
            word = input("\nIngrese palabra para consultar (o 'exit' para salir): ")
            if word.lower() == "exit":
                print("Saliendo del sistema...")
                break
            analyzer.query(word)

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except OSError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()