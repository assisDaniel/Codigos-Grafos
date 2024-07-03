import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def ler_matrizes_de_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        matrizes = []
        matriz_atual = []
        for linha in arquivo:
            linha = linha.strip()
            if linha == "":
                if matriz_atual:
                    matrizes.append(np.array(matriz_atual, dtype=int))
                    matriz_atual = []
            else:
                matriz_atual.append(list(map(int, linha.split())))
        if matriz_atual:
            matrizes.append(np.array(matriz_atual, dtype=int))
    return matrizes

def bfs(grafo, start):
    visitados = set()
    fila = deque([start])
    arvore_bfs = nx.Graph()
    caminho_bfs = []
    pai = {start: None}  # Dicionário para rastrear pais dos nós
    while fila:
        vertice = fila.popleft()
        if vertice not in visitados:
            visitados.add(vertice)
            arvore_bfs.add_node(vertice)
            caminho_bfs.append(vertice + 1)
            for vizinho in grafo.neighbors(vertice):
                if vizinho not in visitados:
                    fila.append(vizinho)
                    arvore_bfs.add_edge(vertice, vizinho)
                    pai[vizinho] = vertice  # Atribui o pai do vizinho
    return arvore_bfs, caminho_bfs, pai

def plotar_grafo(grafo, titulo, pos=None):
    if pos is None:
        pos = nx.spring_layout(grafo)
    nx.draw(grafo, pos, with_labels=True, labels={n: n + 1 for n in grafo.nodes()}, node_color='lightblue',
            edge_color='gray', node_size=500, font_size=12)
    plt.title(titulo)
    plt.show()

def plotar_arvore(arvore, titulo, raiz, pos=None):
    pos = nx.spring_layout(arvore) if pos is None else pos
    labels = {n: n + 1 for n in arvore.nodes()}
    nx.draw(arvore, pos, with_labels=True, labels=labels, node_color='lightgreen', edge_color='gray', node_size=500, font_size=12)
    plt.title(titulo)
    plt.show()

def main():
    nome_arquivo = "grafo.txt"
    matrizes = ler_matrizes_de_arquivo(nome_arquivo)

    print("Selecione a matriz de adjacência (1 a 5):")
    for i, matriz in enumerate(matrizes, 1):
        print(f"Matriz {i}:\n{matriz}")

    escolha_matriz = int(input("Escolha a matriz: ")) - 1
    matriz_adjacencia = matrizes[escolha_matriz]

    grafo = nx.from_numpy_array(matriz_adjacencia)

    while True:
        print("Digite a Opção Desejada:")
        print("1. Verificar se o grafo é conexo")
        print("2. Aplicar Busca em Largura")
        print("3. Encontrar Bipartição")
        print("4. Sair")

        opcao = int(input("Opção: "))

        if opcao == 2:
            print(f"Nós do grafo: {[n + 1 for n in grafo.nodes()]}")
            vertice_inicial = int(input("Escolha o vértice inicial (1 a n): ")) - 1

            arvore_bfs, caminho_bfs, pai = bfs(grafo, vertice_inicial)

            print(f"Busca em Largura (BFS) começando do nó '{vertice_inicial + 1}':")
            print(" ".join(map(str, caminho_bfs)))

            plotar_grafo(grafo, "Grafo Original")
            plotar_arvore(arvore_bfs, "Árvore BFS", vertice_inicial)

        elif opcao == 4:
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
