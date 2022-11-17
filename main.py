import random
from Algoritmo_modificado import *
import time

def gerar_lista(tamanho):
    lista = [random.randrange(1,tamanho,1) for _ in range(tamanho)]
    return lista

def print_resultado(list, resultado_total):
    list.sort()
    maior = float(list[-1])
    menor = float(list[0])
    resultado_total = 0
    for i in range(len(list)):
        resultado_total += list[i]
    print(f"O tempo de execução do teste foi de: {resultado_total:.8f}\nTempo Mínimo: {menor:.9f}\nTempo Máximo: {maior:.9f}\nMédia: {(resultado_total/100):.8f}\n")

def testes_desempenhos(x):

    print("Ordenação Personalizada: \n")
    lista = []
    resultado_total = 0
    for _ in range(100):
        inicio_teste = time.time()
        ordenacao_personalizada(x)
        fim_teste = time.time()
        lista.append(fim_teste-inicio_teste)
        resultado_total += fim_teste-inicio_teste

    print_resultado(lista, resultado_total)

    print("Mergen Original: \n")
    lista = []
    resultado_total = 0
    for _ in range(100):
        inicio_teste = time.time()
        merge_original(x)
        fim_teste = time.time()
        lista.append(fim_teste-inicio_teste)
        resultado_total += (fim_teste-inicio_teste)

    print_resultado(lista, resultado_total)


    # print("SelectionSort: \n")
    # lista = []
    # resultado_total = 0
    # for _ in range(100):
    #     inicio_teste = time.time()
    #     selectionSort(x)
    #     fim_teste = time.time()
    #     lista.append(fim_teste-inicio_teste)
    #     resultado_total += (fim_teste-inicio_teste)

    # print_resultado(lista, resultado_total)

def chamando_fuc(a,b,c):
    print("----------------------------!Lista com 1000 Elementos 100x!----------------------------\n")

    testes_desempenhos(a)


    print("----------------------------!Lista com 10000 Elementos 100x!----------------------------\n")

    testes_desempenhos(b)

    print("----------------------------!Lista com 100000 Elementos 100x!----------------------------\n")

    testes_desempenhos(c)


def main():
    a = gerar_lista(1000)
    b = gerar_lista(10000)
    c = gerar_lista(100000)

    chamando_fuc(a,b,c)


if __name__ == "__main__":
    main()