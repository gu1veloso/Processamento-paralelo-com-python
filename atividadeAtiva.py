import numpy as np
import time
from multiprocessing import Pool
# Função para processar uma parte dos dados
def processar_dados(particao):
    resultado = np.sum(particao)  # Exemplo: somando os elementos da partição
    return resultado
if __name__ == "__main__":
    # Gerar dados de exemplo (uma matriz de 1000x1000)
    tamanho_matriz = (1000, 1000)
    dados = np.random.rand(*tamanho_matriz)
    print(dados.dtype)
    # Dividir a matriz em partições para processamento paralelo
    num_particoes = 4  # Número de partições
    partições = np.array_split(dados, num_particoes)
    # Iniciar o pool de processos
    pool = Pool()
    # Medir o tempo inicial
    inicio = time.time()
    # Processar as partições de forma paralela
    resultados = pool.map(processar_dados, partições)
    print(resultados)
    # Fechar o pool de processos
    pool.close()
    pool.join()
    # Calcular a soma total dos resultados
    soma_total = sum(resultados)
    # Medir o tempo final
    fim = time.time()
    # Imprimir os resultados
    print("Soma total dos resultados:", soma_total)
    print("Tempo total de processamento (segundos):", fim - inicio)

