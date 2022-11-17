import random
from Algoritmo_modificado import *
import time

def gerar_lista(tamanho):
    lista = [random.randrange(1,tamanho,1) for _ in range(tamanho)]
    return lista

def hibrido(a,b,c):

    print("----------------------------!Ordenação Híbrida!----------------------------\n")
    inicio_primeiro_teste = time.time()
    for _ in range(100):
        ordenacao_personalizada(a)
    fim_primeiro_teste = time.time()
    print(f"O tempo de execução da Ordenação Híbrida com 1000 elementos levou: {fim_primeiro_teste-inicio_primeiro_teste:.4f}")

    inicio_segundo_teste = time.time()
    for _ in range(100):
       ordenacao_personalizada(b)
    fim_segundo_teste = time.time()
    print(f"O tempo de execução da Ordenação Híbrida com 10000 elementos levou: {fim_segundo_teste-inicio_segundo_teste:.4f}")

    inicio_terceiro_teste = time.time()
    for _ in range(100):
        ordenacao_personalizada(c)
    fim_terceiro_teste = time.time()
    print(f"O tempo de execução da Ordenação Híbrida com 100000 elementos levou: {fim_terceiro_teste-inicio_terceiro_teste:.4f}\n")

    print("---------------------------------------------------------------------------\n")

def merge_originall(a,b,c):

    print("----------------------------!MergeSort Original!----------------------------\n")
    inicio_primeiro_teste = time.time()
    merge_original(a)
    fim_primeiro_teste = time.time()
    print(f"O tempo de execução da Ordenação MergeSort Original com 1000 elementos levou: {fim_primeiro_teste-inicio_primeiro_teste:.4f}")

    inicio_segundo_teste = time.time()
    mergeSort_sem_slice(b)
    fim_segundo_teste = time.time()
    print(f"O tempo de execução da Ordenação MergeSort Original com 10000 elementos levou: {fim_segundo_teste-inicio_segundo_teste:.4f}")

    inicio_terceiro_teste = time.time()
    merge_original(c)
    fim_terceiro_teste = time.time()
    print(f"O tempo de execução da Ordenação MergeSort Original com 100000 elementos levou: {fim_terceiro_teste-inicio_terceiro_teste:.4f}\n")

    print("---------------------------------------------------------------------------\n")



def main():
    a = gerar_lista(1000)
    b = gerar_lista(10000)
    c = gerar_lista(100000)

    merge_originall(a,b,c)
    hibrido(a,b,c)

# Não foi realizado o teste com selectionSort1, por que demora muito tempo

if __name__ == "__main__":
    main()