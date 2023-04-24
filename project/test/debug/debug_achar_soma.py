"""debug do script principal"""

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

        # Adicionando print do debug
        print(f"index={index}, partial_sum={partial_sum}")

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
    NUMBERS = [ 116.08,  237.89, 19.60,  109.68,  111.31,
                39.20,  65.63,  135.85,  299.79,  88.42,
                278.80,  32.80,  39.20,  94.21,  156.10,
                181.07,  83.93,  19.60, 127.76,  172.73,
                100.00,  83.19,  19.60,  171.29,  39.20,
                137.51,  39.20,  83.93,  124.20,  432.12,
                349.43, 184.07,  113.20,  271.95,  19.60,
                71.29,  124.04, 24.50,  19.60,  161.43,
                49.23,  81.23,  247.62, 19.39,  88.66 ]  # Exemplo de números

    TARGET_SUM = 2345.07  # Exemplo de soma desejada

    # Remove os termos maiores que a soma desejada e ordena o array em ordem decrescente
    NUMBERS = sorted([num for num in NUMBERS if num <= TARGET_SUM], reverse=True)

# Executa a função find_sum com os números e soma desejada especificados
    RESULT = find_sum(NUMBERS, TARGET_SUM)

    # Imprime uma mensagem indicando que o valor desejado foi ou não foi encontrado
    if RESULT[0]:
        print(f"\nEXISTE !! Subconjunto: {RESULT[1]} ")
    else:
        print("\nnão tem :(")
