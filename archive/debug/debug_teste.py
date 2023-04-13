"""script para encontrar se a soma de numeros dentro de uma lista dá um número especifico"""

# Importa o módulo "List" da biblioteca "typing"
from typing import List

# Define a função "find_sum" que recebe uma lista de números e um número alvo como argumentos
def find_sum(numbers: List[float], target_sum: float) -> bool:
    """
    Verifica se existe um subconjunto de numbers que soma exatamente target_sum.

    Args:
        numbers: Uma lista de números.
        target_sum: O valor que o subconjunto deve somar.

    Returns:
        Um valor booleano indicando se existe ou não um subconjunto que soma target_sum.
    """
    # Imprime mensagem de início da função
    print("Starting find_sum function...")

    # Inicializa a pilha de subconjuntos parciais
    stack = [(0, 0)]
    # Define a variável "found" como "False"
    found = False

    # Executa um loop enquanto o valor desejado não for encontrado
    while stack and not found:
        # Remove o último elemento adicionado à pilha
        index, partial_sum = stack.pop()
        # Imprime mensagem de verificação de índice e soma parcial
        print(f"Checking index {index} with partial sum {partial_sum}")

        # Se a soma parcial for igual ao numero desejado, interrompe o loop
        if round(partial_sum, 2) == round(target_sum, 2):
            found = True
            break

        # Se já tiver verificado todos os elementos da lista, passa para a próxima iteração do loop
        if index >= len(numbers):
            continue

        # Adiciona o próximo elemento da lista à pilha sem incluí-lo no subconjunto parcial
        stack.append((index+1, partial_sum))
        # Adiciona o próximo elemento da lista à pilha incluindo-o no subconjunto parcial
        stack.append((index+1, round(partial_sum + numbers[index], 2)))

    # Retorna o valor da variável "found"
    return found


# Define a lista de números que será verificada
NUMBERS = [
    19.60, 109.68, 111.31, 39.20, 65.63, 135.85,
    88.42, 32.80, 39.20, 94.21, 156.10,
    19.60, 91.41, 83.93, 78.39, 19.60, 19.60, 116.82,
    101.48, 23.05, 39.20, 19.60, 78.46,
    ]

# Define o valor que o subconjunto deve somar
TARGET_SUM = 178.49

# Verifica se existe um subconjunto de "NUMBERS" com o valor desejado
if find_sum(NUMBERS, TARGET_SUM):
    print("There is a subset that adds up to the target sum.")
else:
    print("There is no subset that adds up to the target sum.")
