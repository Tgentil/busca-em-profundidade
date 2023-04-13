"""script de soma de números em uma lista"""

# Importando o tipo de dados "List"
from typing import List

def sum_array(numbers: List[float]) -> float:
    """
    Soma os valores dentro de uma lista e arredonda o resultado para 2 dígitos após a vírgula.

    Args:
        numbers: Uma lista de números.

    Returns:
        A soma dos valores dentro da lista, arredondada para 2 dígitos após a vírgula.
    """
    
    # somando os valores da lista
    total = sum(numbers)
    # arredondando o resultado para 2 dígitos após a vírgula
    return round(total, 2)

# exemplo de uma lista de números
NUMBERS = [81.48, 0.29, 2.29, 34.99, 13.05, 1245.21, 24.50, 48.99]

# chamando a função e armazenando o resultado em `result`
result = sum_array(NUMBERS)

# imprimindo o resultado na tela
print(f"O resultado da soma dos valores é: {result}")
