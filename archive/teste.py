"""script para encontrar se a soma de números dentro de uma lista consegue
resultar em um número especifico"""

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
    # Cria uma pilha "stack" e adiciona uma tupla com o índice 0 e a soma parcial 0
    stack = [(0, 0)]
    # Define uma variável "found" como False
    found = False
    # Executa um loop enquanto não encontrar o valor alvo
    while stack and not found:
        # Remove o último elemento adicionado e define as variáveis
        index, partial_sum = stack.pop()
        # Verifica se a soma é igual ao valor alvo e arredonda os valores para 2 casas decimais
        if round(partial_sum, 2) == round(target_sum, 2):
            # Se a condição acima for verdadeira, interrompe o loop
            found = True
            break
        # Verifica se o índice é maior ou igual ao tamanho da lista "numbers"
        if index >= len(numbers):
            # Se a condição acima for verdadeira, pula para a próxima iteração do loop
            continue
        # Adiciona à pilha "stack" duas tuplas
        stack.append((index+1, partial_sum))
        stack.append((index+1, round(partial_sum + numbers[index], 2)))
    # Retorna o valor da variável "found"
    return found


# Cria uma lista de números
NUMBERS = [
    19.60, 109.68, 111.31, 39.20, 65.63, 135.85,
    88.42, 32.80, 39.20, 94.21, 156.10,
    19.60, 91.41, 83.93, 78.39, 19.60, 19.60, 116.82,
    101.48, 23.05, 39.20, 19.60, 78.46,
]

# Define o valor alvo
TARGET_SUM = 178.49


# Imprime uma mensagem indicando que o valor desejado foi ou não foi encontrado
if find_sum(NUMBERS, TARGET_SUM):
    print("Existe um subconjunto que forma o valor desejado!!")
else:
    print("Não foi possivel encontrar o valor desejado :( ")
