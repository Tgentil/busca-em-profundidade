"""script de soma de subconjuntos dentro de um array para obter um valor especifico"""

# Importando os tipos de dados List e deque
from typing import List
from collections import deque
import sys

# Define o enconding
sys.stdout.reconfigure(encoding='utf-8')

def find_sum(numbers: List[float], target_sum: float, tolerance: float = 1e-6) -> bool:
    """
    Verifica se existe um subconjunto de `numbers` que soma exatamente `target_sum`.

    Args:
        numbers: Uma lista de números.
        target_sum: O valor que o subconjunto deve somar.
        tolerance: O valor de tolerância para a verificação de igualdade de números de 
        ponto flutuante.

    Returns:
        Um valor booleano indicando se existe ou não um subconjunto que soma `target_sum`.
    """

    # Criação de uma fila (deque) com um único elemento (tupla com dois valores)
    queue = deque([(0, 0)])

    # Loop enquanto a fila tiver elementos
    while queue:
        # Remove o último elemento da fila e atribuição dos valores às variáveis index e partial_sum
        index, partial_sum = queue.pop()

        # Verifica se a diferença entre partial_sum e target_sum é menor que a tolerância especifica
        if abs(partial_sum - target_sum) < tolerance:
            return True  # Retorna True se a soma for encontrada

        # Verifica se index é maior ou igual ao comprimento da lista numbers
        if index >= len(numbers):
            continue # Vai para o proximo elemento

        # Adiciona duas novas tuplas à fila, uma com o próximo índice e partial_sum
        # e outra com o próximo índice e partial_sum + o número atual
        queue.append((index+1, partial_sum))
        queue.append((index+1, partial_sum + numbers[index]))

    return False  # Retorna False se a soma não for encontrada


# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    NUMBERS = [0.50, 2, 2.50, 5, 7, 2.20]  # Exemplo de números
    TARGET_SUM = 10.00  # Exemplo de soma desejada

# Executa a função find_sum com os números e soma desejada especificados
    RESULT = find_sum(NUMBERS, TARGET_SUM)

    # Imprime uma mensagem indicando que o valor desejado foi ou não foi encontrado
    if RESULT:
        print("\nEXISTE !!")
    else:
        print("\nnão tem :(")
