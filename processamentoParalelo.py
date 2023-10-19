import numpy as np
import time
from multiprocessing import Pool

#função que identifica os números primos
def f(n):
    list = n.tolist()
    result = []
    for i in list:
        x = 0
        if i > 1:
            for num in range(2, i):
                if(i % num) == 0:
                    x += 1
            if x == 0:
                result.append(i)
    return result

if __name__ == "__main__":
    #Cria um array com a sequência de números a serem analisados
    data = np.arange(100)
    
    #Divide o array em 1 partições
    partData = np.array_split(data,1)
    #Inicia o Pool de processos
    p = Pool()
    #Registra o tempo inicial
    t = time.time()
    #Processa as partições de forma paralela
    result = p.map(f,partData)
    #Fecha o Pool de processos
    p.close()
    p.join()
    #Mostra o tempo de execução
    print(f"Tempo de execução em 1 partições: {time.time() - t} segundos")
    #Concatena as partições processadas em um único array
    result = np.concatenate(result)
    #Mostra os resultados
    #print(f"Lista com os números primos:\n {result}\n")
    
    #Divide o array em 4 partições
    partData = np.array_split(data,4)
    #Inicia o Pool de processos
    p = Pool()
    #Registra o tempo inicial
    t = time.time()
    #Processa as partições de forma paralela
    result = p.map(f,partData)
    #Fecha o Pool de processos
    p.close()
    p.join()
    #Mostra o tempo de execução
    print(f"Tempo de execução em 4 partições: {time.time() - t} segundos")
    #Concatena as partições processadas em um único array
    result = np.concatenate(result)
    #Mostra os resultados
    #print(f"Lista com os números primos:\n {result}\n")

    # Divide o array em 6 partições
    partData = np.array_split(data, 6)
    # Inicia o Pool de processos
    p = Pool()
    # Registra o tempo inicial
    t = time.time()
    # Processa as partições de forma paralela
    result = p.map(f, partData)
    # Fecha o Pool de processos
    p.close()
    p.join()
    # Mostra o tempo de execução
    print(f"Tempo de execução em 6 partições: {time.time() - t} segundos")
    # Concatena as partições processadas em um único array
    result = np.concatenate(result)
    # Mostra os resultados
    #print(f"Lista com os números primos:\n {result} \n")

    # Divide o array em 8 partições
    partData = np.array_split(data, 8)
    # Inicia o Pool de processos
    p = Pool()
    # Registra o tempo inicial
    t = time.time()
    # Processa as partições de forma paralela
    result = p.map(f, partData)
    # Fecha o Pool de processos
    p.close()
    p.join()
    # Mostra o tempo de execução
    print(f"Tempo de execução em 8 partições: {time.time() - t} segundos")
    # Concatena as partições processadas em um único array
    result = np.concatenate(result)
    # Mostra os resultados
    print(f"Lista com os números primos:\n {result}\n")