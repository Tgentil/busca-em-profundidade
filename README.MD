# Projeto de Soma de Subconjuntos

 [![GitHub](https://img.shields.io/badge/Visit-My%20Profile-0891B2?style=flat-square&logo=github)](https://github.com/Tgentil)

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

## Melhoria de Desempenho

O script tem uma complexidade O(2^n), Entretanto, algumas otimizações foram aplicadas para melhorar a performance. Uma delas foi a reorganização da lista em ordem decrescente, para que números maiores fossem utilizados primeiro, e a outra foi a mudança de caminho ao atingir uma soma maior do que o número desejado.

Com essas mudanças, o algoritmo agora é executado de forma mais eficiente e evita iterações desnecessárias. Como resultado, a execução do script agora é muito mais rápida do que antes.

## Utilização

Para utilizar o algoritmo, importe a função `find_sum` do módulo `achar_soma` e chame-a passando a lista de números e o valor alvo como argumentos:

```python
from project.code.achar_soma import find_sum

NUMBERS = [0.50, 2, 2.50, 5, 7, 2.20] # exemplo
TARGET_SUM = 10.00  # Exemplo

    if RESULT[0]:
        print(f"\nEXISTE !! Subconjunto: {RESULT[1]} ")
    else:
        print("\nnão tem :(")

```

O código acima irá verificar se há um subconjunto de NUMBERS que soma exatamente TARGET_SUM. Se encontrar um subconjunto, imprimirá " EXISTE !! ". Caso contrário, imprimirá " não tem :( ".

Nesse exemplo o terminal vai responder com 
``` EXISTE !! Subconjunto: [5, 2.5, 2, 0.5] ```

## Minha experiência

Ao utilizar o código antes ele rodava bem com conjuntos de até 20 números, agora roda fácilmente com arrays bem maiores e ainda retorna os valores utilizados para chegar ao resultado.

## Update de testes e limitações

Ao testar o script com o último update, em um input de 45 números houve uma melhora significativa da performance:

Input de teste:

```python
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

    TARGET_SUM =  2345.07  # Exemplo de soma desejada
```

Saída do script antes:

```python
[Running] python -u "c:\busca em profundidade\project\code\achar_soma.py"

EXISTE !!

[Done] exited with code=0 in 345.134 seconds
```

Saída do script atualmente:

```python
[Running] python -u "c:\busca em profundidade\project\code\achar_soma.py"

EXISTE !! Subconjunto: [432.12, 349.43, 299.79, 278.8, 271.95, 247.62, 172.73, 88.42, 83.19, 49.23, 32.8, 19.6, 19.39] 

[Done] exited with code=0 in 3.277 seconds
```

## Hardware utlizado para teste

CPU:

	11th Gen Intel(R) Core(TM) i3-1115G4 @ 3.00GHz

Memória Ram:

    8,0 GB

    

## Autores

* Thiago da Silveira Gentil
