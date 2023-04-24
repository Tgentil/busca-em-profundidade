"""Gera números para fazer teste do script"""

# Importa a biblioteca random, que será usada para gerar números aleatórios.
import random
import sys

# Define o enconding
sys.stdout.reconfigure(encoding='utf-8')

def generate_random_numbers(quantity: int) -> list:
    """
    Gera uma lista de números aleatórios com duas casas decimais.

    Args:
        quantity: A quantidade de números a serem gerados.

    Returns:
        Uma lista de números aleatórios com duas casas decimais.
    """

    # Cria uma lista vazia para armazenar os números gerados aleatoriamente.
    numbers = []

    # Loop for que irá executar a quantidade de vezes especificada no argumento "quantity".
    for _ in range(quantity):
        # Gera um número aleatório entre 0 e 100 com duas casas decimais.
        number = round(random.uniform(0, 100), 2)
        # Adiciona o número gerado à lista "numbers".
        numbers.append(number)

    # Retorna a lista de números gerados.
    return numbers

# Chama a função passando o argumento "10", que é a quantidade de números a serem gerados.
# Armazena o retorno da função na variável "NUMEROS".
NUMEROS = generate_random_numbers(10)

# Imprime a lista de números gerados pela função "generate_random_numbers".
print(f"\nSeu array de números corretos é: {NUMEROS} \n")
# Imprime a soma dos números gerados na lista "NUMEROS" com duas casas decimais.
print(f"Seu target sum é: {round(sum(NUMEROS),2)} \n")


def generate_random_numbers_v2(quantity: int) -> list:
    """
    Gera uma lista de números aleatórios com duas casas decimais.

    Args:
        quantity: A quantidade de números a serem gerados.

    Returns:
        Uma lista de números aleatórios com duas casas decimais.
    """

    # Cria uma lista vazia para armazenar os números gerados aleatoriamente.
    numbersv2 = []

    # Loop for que irá executar a quantidade de vezes especificada no argumento "quantity".
    for _ in range(quantity):
        # Gera um número aleatório entre 0 e 100 com duas casas decimais.
        numberv2 = round(random.uniform(0, 100), 2)
        # Adiciona o número gerado à lista "numbersv2".
        numbersv2.append(numberv2)

    # Retorna a lista de números gerados.
    return numbersv2

# Chama a função passando o argumento "5", que é a quantidade de números a serem gerados.
# Armazena o retorno da função na variável "NUMEROSV2".
NUMEROSV2 = generate_random_numbers_v2(5)

# Imprime a lista de números gerados pela função "generate_random_numbers_v2".
print(f"\nSeu array de números errados é: {NUMEROSV2} \n")

# Combina as listas "NUMEROS" e "NUMEROSV2" em uma nova lista chamada "NUMEROS_COMBINADOS".
NUMEROS_COMBINADOS = NUMEROS + NUMEROSV2

# Embaralha aleatoriamente os elementos da lista "NUMEROS_COMBINADOS".
random.shuffle(NUMEROS_COMBINADOS)

# Imprime a lista
print(f"Seu array de números combinados é: {NUMEROS_COMBINADOS} \n")
