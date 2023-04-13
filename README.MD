# Projeto de Soma de Subconjuntos

Este projeto implementa um algoritmo de busca em profundidade para encontrar um subconjunto de números de uma lista que soma um valor específico.

## Motivação
Criei este script porque desejava verificar se uma lista com vários lançamentos de vendas que compõem vários lotes de lançamentos continham um lote específico.

## Estrutura do Projeto

O projeto está estruturado da seguinte maneira:

```
busca_em_profundidade
├── archive
│   ├── debug
│   │   └── debug_teste.py
│   └── teste.py
└── project
    ├── code
    │   └── achar_soma.py
    └── test
        ├── debug
        │   └── debug_achar_soma.py
        └── generator
            └── gerador_de_numeros.py
```

O diretório `archive` contém o primeiro protótipo desenvolvido durante o projeto. O código presente nesta pasta tem uma eficiência bem reduzida em comparação ao código encontrado na pasta `project`.

Ao longo do desenvolvimento, foi necessário refatorar e otimizar o código na pasta `archive` para melhorar sua eficiência e escalabilidade.

O diretório `project` contém o código-fonte (`achar_soma.py`) e uma pasta de teste que contém um script de debug (`debug_achar_soma.py`) e um gerador de números para teste do script principal (`gerador_de_numeros.py`) a pasta `Project` representa a versão mais atualizada e eficiente da solução. Ele foi aprimorado com base nos resultados obtidos a partir do protótipo inicial e é capaz de lidar com um volume de dados muito maior. Além disso, ele incorpora funcionalidades adicionais e melhorias de desempenho.

Em resumo, a pasta `archive` contém o código original do primeiro protótipo, que pode ser útil para fins de referência, mas não é recomendado para uso atual devido à sua baixa eficiência. Recomendo o uso do código encontrado na pasta `project`, que representa a versão mais atualizada e eficiente da solução.

## Utilização

Para utilizar o algoritmo, importe a função `find_sum` do módulo `achar_soma` e chame-a passando a lista de números e o valor alvo como argumentos:

```python
from project.code.achar_soma import find_sum

NUMBERS = [0.50, 2, 2.50, 5, 7, 2.20] # exemplo
TARGET_SUM = 10.00  # Exemplo

if find_sum(NUMBERS, TARGET_SUM):
    print("\nEXISTE !!")
else:
    print("\nnão tem :(")
```

O código acima irá verificar se há um subconjunto de NUMBERS que soma exatamente TARGET_SUM. Se encontrar um subconjunto, imprimirá " EXISTE !! ". Caso contrário, imprimirá " não tem :( ".

Nesse exemplo o terminal vai responder com ` EXISTE !! `, pelo fato de 0.50 + 2 + 2.50 + 5 = 10.

## Minha experiência

Ao utilizar o código, observei uma performance muito boa para listas de 20 números e um tempo aceitável para listas de 30 números. Não experimentei com listas maiores, mas acredito ser possível a implementação mesmo com um desempenho não tão bom

## Autores

* Thiago da Silveira Gentil
