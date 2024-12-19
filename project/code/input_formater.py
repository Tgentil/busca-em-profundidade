"""_summary_ = Formata os números de uma string para uma lista de floats.
"""
import sys

# Define o enconding
sys.stdout.reconfigure(encoding='utf-8')

def format_numbers_from_string(s: str) -> list:
    """
    Formata uma string contendo números separados por linhas novas em uma lista de floats.
    Argumentos:
    - s (str): Uma string contendo números separados por linhas novas.
    
    Retorna:
    - Uma lista de floats, onde cada float é um número da string de entrada.
    """

    # Separa as linhas e formata cada número
    numbers = [float(line.replace("R$", "").replace(",", ".")) for line in s.strip().split("\n")]
    return numbers

def get_input_from_console() -> str:
    """
    Solicita ao usuário a entrada de uma lista de números, terminada pela string 'END'.
    Retorna uma string contendo os números inseridos, separados por linhas novas.
    """
    print("Insira os números (termine com 'END'):")
    lines = []
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    return "\n".join(lines)

if __name__ == "__main__":
    # Pegando os números do console
    INPUT_DATA = get_input_from_console()
    formatted_numbers = format_numbers_from_string(INPUT_DATA)
    print("    NUMBERS = ", formatted_numbers)
