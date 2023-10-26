"""_summary_ = Formata os números de uma string para uma lista de floats.
"""
import sys

# Define o enconding
sys.stdout.reconfigure(encoding='utf-8')

def format_numbers_from_string(s: str) -> list:
    """
    Formats a string containing numbers separated by newlines into a list of floats.
    Args:
    - s (str): A string containing numbers separated by newlines.
    
    Returns:
    - A list of floats, where each float is a number from the input string.
    """

    # Separa as linhas e formata cada número
    numbers = [float(line.replace("R$", "").replace(",", ".")) for line in s.strip().split("\n")]
    return numbers

def get_input_from_console() -> str:
    """
    Prompts the user to input a list of numbers, terminated by the string 'END'.
    Returns a string containing the input numbers, separated by newlines.
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
