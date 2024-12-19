import sys

# Define o encoding
sys.stdout.reconfigure(encoding='utf-8')

def format_numbers_from_string(s: str) -> list:
    """
    Recebe uma string com múltiplas linhas, cada uma no formato 'R$ 999,99',
    e retorna uma lista de floats, convertendo '999,99' em 999.99.
    """
    # Quebra a string em linhas
    lines = s.strip().split("\n")
    # Remove 'R$', troca vírgula por ponto e converte para float
    numbers = [float(line.replace("R$", "").strip().replace(",", ".")) for line in lines if line.strip()]
    return numbers

def get_input_from_console() -> str:
    """
    Lê da entrada padrão linhas até encontrar 'END'.
    Retorna uma string com todas as linhas lidas (sem a linha 'END'),
    separadas por quebras de linha.
    """
    print("Insira os valores (termine com 'END'):")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

if __name__ == "__main__":
    # Lendo os dados da entrada padrão
    INPUT_DATA = get_input_from_console()
    formatted_numbers = format_numbers_from_string(INPUT_DATA)
    print("NUMBERS = ", formatted_numbers)
