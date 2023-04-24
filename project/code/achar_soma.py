"""script de soma de subconjuntos dentro de um array para obter um valor especifico"""

# Importando os tipos de dados List e deque
from typing import List, Tuple
from collections import deque
import sys

# Define o enconding
sys.stdout.reconfigure(encoding='utf-8')

def find_sum(numbers: List[float], target_sum: float, tolerance: float = 1e-6) -> Tuple[bool, List[float]]:
    """
    Verifica se existe um subconjunto de `numbers` que soma exatamente `target_sum`.

    Args:
        numbers: Uma lista de números.
        target_sum: O valor que o subconjunto deve somar.
        tolerance: O valor de tolerância para a verificação de igualdade de números de 
        ponto flutuante.

    Returns:
        Um tuple com um valor booleano indicando se existe um subconjunto que soma `target_sum`
        e uma lista com os números que formam o subconjunto.
    """

    # Criação de uma fila (deque) com um único elemento (tupla com três valores)
    queue = deque([(0, 0, [])])

    # Loop enquanto a fila tiver elementos
    while queue:
        # Remove o último elemento da fila e atribuição dos valores
        index, partial_sum, subset = queue.pop()

        # Verifica se a diferença entre partial_sum e target_sum é menor que a tolerância especifica
        if abs(partial_sum - target_sum) < tolerance:
            return True, subset  # Retorna True e o subconjunto se a soma for encontrada

        # Verifica se index é maior ou igual ao comprimento da lista numbers
        if index >= len(numbers):
            continue # Vai para o próximo elemento

        # Verifica se partial_sum atual mais o próximo número é menor ou igual ao target_sum
        if partial_sum + numbers[index] <= target_sum:
            # Adiciona duas novas tuplas à fila, uma com o próximo índice, partial_sum e subset
            # e outra com o próximo índice, partial_sum + o número atual e subset + [numbers[index]]
            queue.append((index+1, partial_sum, subset))
            queue.append((index+1, partial_sum + numbers[index], subset + [numbers[index]]))

    return False, []  # Retorna False e uma lista vazia se a soma não for encontrada



# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    NUMBERS = [0.50, 2, 2.50, 5, 7, 2.20]  # Exemplo de números

    TARGET_SUM = 10.00  # Exemplo de soma desejada

    # Remove os termos maiores que a soma desejada e ordena o array em ordem decrescente
    NUMBERS = sorted([num for num in NUMBERS if num <= TARGET_SUM], reverse=True)
    
    
# Verifica se a soma de todos os números no array é menor do que a soma desejada
if sum(NUMBERS) < TARGET_SUM:
    print("Não é possível obter a soma desejada com os números fornecidos.")
else:


# Executa a função find_sum com os números e soma desejada especificados
    RESULT = find_sum(NUMBERS, TARGET_SUM)

    # Imprime uma mensagem indicando que o valor desejado foi ou não foi encontrado
    if RESULT[0]:
        print(f"\nEXISTE !! Subconjunto: {RESULT[1]} ")
    else:
        print("\nnão tem :(")

