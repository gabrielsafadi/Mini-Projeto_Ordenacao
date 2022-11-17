

#Ordenação Solicitada na atividade

def ordenacao_personalizada(uma_lista):
    if len(uma_lista) <= 128 and len(uma_lista) > 0:
        return selectionSort(uma_lista)
    else:
        if len(uma_lista) >128:
            meio = len(uma_lista)//2
            esquerda = uma_lista[:meio]
            direita = uma_lista[meio:]
            ordenacao_personalizada(esquerda)
            ordenacao_personalizada(direita)

        i=0
        j=0
        k=0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                uma_lista[k]=esquerda[i]
                i=i+1
            else:
                uma_lista[k]=direita[j]
                j=j+1
            k=k+1
        while i < len(esquerda):
            uma_lista[k]=esquerda[i]
            i=i+1
            k=k+1
        while j < len(direita):
            uma_lista[k]=direita[j]
            j=j+1
            k=k+1

# Selection sort Maior e menor

def selectionSort(uma_lista):
    limite_esquerdo = 0
    for limite_direito in range(len(uma_lista)-1, len(uma_lista)//2-1, -1):
        posicao_maior = int(limite_esquerdo)
        posicao_menor = int(limite_direito)

        for posicao in range(limite_esquerdo, limite_direito+1):
            if uma_lista[posicao] >= uma_lista[posicao_maior]:
                posicao_maior = posicao

            if uma_lista[posicao] <= uma_lista[posicao_menor]:
                posicao_menor = posicao

        if limite_direito == posicao_menor and limite_esquerdo == posicao_maior:
            uma_lista[limite_direito], uma_lista[limite_esquerdo] = uma_lista[limite_esquerdo], uma_lista[limite_direito]

        else:
            temp_maior = uma_lista[limite_direito]
            temp_menor = uma_lista[limite_esquerdo]
            uma_lista[limite_direito] = uma_lista[posicao_maior]
            uma_lista[posicao_maior] = temp_maior

            if posicao_menor != limite_direito and posicao_maior != limite_esquerdo:
                uma_lista[limite_esquerdo] = uma_lista[posicao_menor]
                uma_lista[posicao_menor] = temp_menor

            elif posicao_menor == limite_direito:
                uma_lista[limite_esquerdo] = temp_maior
                uma_lista[posicao_maior] = temp_menor

            elif posicao_maior == limite_esquerdo:
                uma_lista[limite_esquerdo] = uma_lista[posicao_menor]
                uma_lista[posicao_menor] = temp_maior

        limite_esquerdo += 1

    return uma_lista




# Selection Sort Original

def selectionSort1(uma_lista):
    for posicao_verificada in range(len(uma_lista)-1,0,-1):
        posicao_maior = 0
        for posicao in range(1,posicao_verificada+1):
            if uma_lista[posicao]>uma_lista[posicao_maior]:
                posicao_maior = posicao
        temp = uma_lista[posicao_verificada]
        uma_lista[posicao_verificada] = uma_lista[posicao_maior]
        uma_lista[posicao_maior] = temp
    return uma_lista


# merge_original

def merge_original(uma_lista):

    if len(uma_lista) >1:
        meio = len(uma_lista)//2
        esquerda = uma_lista[:meio]
        direita = uma_lista[meio:]
        ordenacao_personalizada(esquerda)
        ordenacao_personalizada(direita)

    i=0
    j=0
    k=0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            uma_lista[k]=esquerda[i]
            i=i+1
        else:
            uma_lista[k]=direita[j]
            j=j+1
        k=k+1
    while i < len(esquerda):
        uma_lista[k]=esquerda[i]
        i=i+1
        k=k+1
    while j < len(direita):
        uma_lista[k]=direita[j]
        j=j+1
        k=k+1

# MergenSort sem Slice

def split(uma_lista, inicio, fim):
    result = []
    if not(0 <= inicio < len(uma_lista)):
        return result
    elif not(inicio <= fim < len(uma_lista)):
        return result
    else:
        for i in range(inicio, fim):
            result.append(uma_lista[i])
        return result

def mergeSort_sem_slice(uma_lista):
    if len(uma_lista)<=1:
        return uma_lista
    elif len(uma_lista)>1:
        meio = len(uma_lista)//2
        inicio = 0
        fim = len(uma_lista)-1
        met_esquerda = split(uma_lista,inicio,meio)
        met_direita = split(uma_lista,meio,fim)
        
        mergeSort_sem_slice(met_esquerda)
        mergeSort_sem_slice(met_direita)

        i=0
        j=0
        k=0
        
        while i < len(met_esquerda) and j < len(met_direita):
            if met_esquerda[i] <= met_direita[j]:
                uma_lista[k]=met_esquerda[i]
                i=i+1
            else:
                uma_lista[k]=met_direita[j]
                j=j+1
            k=k+1

        while i < len(met_esquerda):
            uma_lista[k]=met_esquerda[i]
            i=i+1
            k=k+1

        while j < len(met_direita):
            uma_lista[k]=met_direita[j]
            j=j+1
            k=k+1