from copy import copy

#converte os vértices de uma string para uma lista de inteiros
def seq(lista):
    lista = lista.replace('-', ' ')
    lista = lista.split(' ')
    lista1 = []
    for x in lista:
        lista1.append(int(x)-1)
    #lista = re.findall('.', lista)
    #lista = [(int(x)-1) for x in lista]
    return lista1

#retorna uma lista com os graus de um grafo
def listaGraus(grafo):
    graus = []
    for x in grafo:
        graus.append(len(grafo[x]))
    return graus

#retorna as arestas do grafo
def listaArestasGrafo(grafo):
    arestas = []
    for i in grafo:
        for j in grafo[i]:
            aresta = []
            aresta.append(i)
            aresta.append(j)
            arestas.append(aresta)
    return arestas

#retorna a lista de arestas da sequencia
def listaArestasSeq(sequencia):
    arestas = []
    for i in range(len(sequencia)-1):
        aresta = []
        aresta.append(sequencia[i])
        aresta.append(sequencia[i+1])
        arestas.append(aresta)
    return arestas

def encontrarCaminhos(graph, start, end, path=[]):
    path.append(start)
    if start == end:
        return [path]
    if not(start in graph):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = encontrarCaminhos(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def encontrarCiclo(graph):
    cycles = []
    for startnode in graph:
        for endnode in graph:
            newpaths = encontrarCaminhos(graph, startnode, endnode)
            for path in newpaths:
                if (len(path) == len(graph)):
                    if path[0] in graph[path[len(graph) - 1]]:
                        path.append(path[0])
                        cycles.append(path)
    return cycles

def verificar(teste, grafo, i):
    if teste[i] == "passeio":
        copia = grafo
        return(passeio(copia, seq(teste[2])))
    elif teste[i] == "caminho":
        return(caminho(copy(grafo), seq(teste[2])))
    elif teste[i] == "trilha":
        return(trilha(grafo.copy(), seq(teste[2])))
    elif teste[i] == "circuito":
        copia = grafo
        return(circuito(copia, seq(teste[2])))
    elif teste[i] == "ciclo":
        copia = grafo
        return(ciclo(copia, seq(teste[2])))
    elif teste[i] == "euleriano":
        copia = grafo
        return (euleriano(copia))
    elif teste[i] == "hamiltoniano":
        copia = grafo
        return(hamiltoniano())

def passeio(grafo, sequencia):
    if len(sequencia) != 1:
        for i in range(0, len(sequencia)-1):
            if (sequencia[i] in grafo) and (sequencia[i+1] in grafo[sequencia[i]]):
                y = 0
            else:
                return False
    else:
        return False
    return True

def caminho(grafoLocal, sequencia):
    if passeio(grafoLocal, sequencia):
        if sequencia[0] == sequencia[len(sequencia)-1]:
            return False
        else:
            verticesVisitados = []
            for i in range(0, len(sequencia)-1):
                if sequencia[i] in verticesVisitados:
                    return False
                else:
                    if (sequencia[i] in grafoLocal) and (sequencia[i+1] in grafoLocal[sequencia[i]]):
                        verticesVisitados.append(sequencia[i])
    else:
        return False
    return True

def trilha(grafoLocal1, sequencia):
    arestasSeq = listaArestasSeq(sequencia)
    arestasGrafo = listaArestasGrafo(grafoLocal1)
    if passeio(grafoLocal1, sequencia):
        for x in arestasSeq:
            if x in arestasGrafo:
                aux = []
                aux.append(x[1])
                aux.append(x[0])
                if aux in arestasGrafo:
                    arestasGrafo.remove(aux)
                arestasGrafo.remove(x)
            else:
                return False
    else:
        return False
    return True

def circuito(grafo, sequencia):
    arestasSeq = listaArestasSeq(sequencia)
    arestasGrafo = listaArestasGrafo(grafo)
    if passeio(grafo, sequencia):
        if sequencia[0] == sequencia[len(sequencia) - 1]:
            for x in arestasSeq:
                if x in arestasGrafo:
                    aux = []
                    aux.append(x[1])
                    aux.append(x[0])
                    if aux in arestasGrafo:
                        arestasGrafo.remove(aux)
                    arestasGrafo.remove(x)
                else:
                    return False
        else:
            return False
    else:
        return False
    return True

def ciclo(grafo, sequencia):
    if circuito(grafo, sequencia):
        if sequencia[0] == sequencia[len(sequencia)-1]:
            for x in range(1, len(sequencia)-1):
                if sequencia.count(sequencia[x]) != 1:
                    return False
        else:
            return False
    else:
        return False
    return True

def euleriano(grafo):
    for x in listaGraus(grafo):
        if (x%2 != 0):
            return False
    return True

def hamiltoniano():
    global ehHamiltoniano
    return ehHamiltoniano

def hamiltonianoChecar(grafo):
    numCiclos = encontrarCiclo(grafo)
    if len(numCiclos) == 0:
        return False
    else:
        return True

#inicio-----------------------------------------------------------------------------------------------------------------
entrada = [int(x) for x in input().split(" ")]
grafo = {}
saida = []

ehHamiltoniano = hamiltonianoChecar(grafo)

for i in range(entrada[0]):
    lista = [int(x) for x in input().split(" ")]
    adjacentes = []
    for j in range(len(lista)):
        if lista[j] != 0:
            adjacentes.append(j)
    grafo[i] = adjacentes

for i in range(entrada[1]):
    teste = [str(x) for x in input().split(" ")]
    teste[1] = teste[1].replace('!', '')
    copia1 = grafo.copy()
    copia2 = grafo.copy()
    if entrada[0] != 1:
        if verificar(teste, copia1, 0) and (not(verificar(teste, copia2, 1))):
            saida.append(True)
        else:
            saida.append(False)
    else:
        saida.append(False)

for x in saida:
    if x:
        print("yes")
    else:
        print("no")