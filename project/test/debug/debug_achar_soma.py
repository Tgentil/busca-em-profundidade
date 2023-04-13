"""debug do script principal"""

# Importando os tipos de dados List e deque
from typing import List
from collections import deque


def find_sum(numbers: List[float], target_sum: float,
            tolerance: float = 1e-6, debug: bool = False) -> bool:
    """
    Verifica se existe um subconjunto de `numbers` que soma exatamente `target_sum`.

    Args:
        numbers: Uma lista de números.
        target_sum: O valor que o subconjunto deve somar.
        tolerance: O valor de tolerância para a verificação 
        de igualdade de números de ponto flutuante.
        debug: Ativa ou desativa o modo de depuração.

    Returns:
        Um valor booleano indicando se existe ou não um subconjunto que soma `target_sum`.
    """
    # Inicializa a fila com o primeiro índice e soma parcial zero
    queue = deque([(0, 0)])
    while queue:
        # Remove o próximo índice e soma parcial da fila
        index, partial_sum = queue.pop()
        # Se o modo de depuração estiver ativado, imprime informações
        if debug:
            print(f"Index: {index}, Partial Sum: {partial_sum}, Queue: {queue}")
        # Se a soma parcial for igual ao valor alvo, retorna True
        if abs(partial_sum - target_sum) < tolerance:
            return True
        # Se o índice for maior ou igual ao comprimento da lista, pula para o próximo índice
        if index >= len(numbers):
            continue
        # Adiciona o próximo índice sem somá-lo
        queue.append((index+1, partial_sum))
        # Adiciona o próximo índice com a soma parcial atualizada
        queue.append((index+1, partial_sum + numbers[index]))
    # Retorna False se não houver subconjunto que some o valor alvo
    return False


if __name__ == '__main__':
    # Exemplo de lista de números e valor alvo
    NUMBERS = [0.29, 34.99, 13.05, 1245.21, 24.50, 48.99] 
    TARGET_SUM = 178.85  
    # Chama a função de soma de subconjuntos e ativa o modo de depuração
    RESULT = find_sum(NUMBERS, TARGET_SUM, debug=True)
    # Imprime o resultado
    if RESULT:
        print("\nEXISTE !!")
    else:
        print("\nnão tem :(")
