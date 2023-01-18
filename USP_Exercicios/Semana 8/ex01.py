def remove_repetidos(lista):
    lista_sem_repeticoes = list() # Utilizando o conjunto para remover elementos repetidos
    for c in lista:
        if c in lista_sem_repeticoes:
            continue
        else:
            lista_sem_repeticoes.append(c)
    lista_sem_repeticoes.sort() # Ordenando a lista
    return lista_sem_repeticoes
