# Projeto 3 MC346
# Desenvolvido por:
# Felipe Arruda 196862
# Renata Lellis 205320
# Gabriel Silveira 197244

import sys

def identifica_substring(string1, string2):
	for i in range(len(string1)):
		substring1 = string1[i:]
		substring2 = string2[:len(substring1)]
		if substring2.find(substring1) >= 0:
			return(len(substring1))
	return 0

def topologicalUtil(v, visited, stack, graph):
	visited[v] = True
	for neighboor in graph[v]:
		if not visited[neighboor[0]]:
			topologicalUtil(neighboor[0], visited, stack, graph)
	stack.append(v)

def topologicalSort(graph, size):
	stack = []
	visited = [0]*size
	for i in range(size):
		if not visited[i]:
			topologicalUtil(i, visited, stack, graph)

	return stack[::-1]

def monta_dna(v, visited, trecho, graph, cromos, dnas):
	visited[v] = True
	if len(graph[v]) == 0:
		return [trecho]
	for neighboor, init in graph[v]:
		novo_trecho = trecho + cromos[neighboor][init:]
		dnas = dnas + monta_dna(neighboor, visited, novo_trecho, graph, cromos, dnas)
	return dnas
	
def main():
	x = 0
	cromo = {}
	for line in sys.stdin:
		if line[-1] == '\n':
			line = line[:-2]
		cromo[x] = line # O -2 é pra tirar o \r\n da string
		x += 1

	size = len(cromo)

	graph = {}
	for i in range(size):
		edges = []
		for j in range(size):
			if i != j:
				conn = identifica_substring(cromo[i], cromo[j])
				if conn > 4:
					edges.append((j, conn))
		graph[i] = edges
	# print(graph)
	order = topologicalSort(graph, size)
	# print(order)


	dna = []
	visited = [0]*size
	for i in order:
		if not visited[i]:
			dna = dna + monta_dna(i, visited, cromo[i], graph, cromo, [])
	print(dna)
	dna.sort(key=len)
	print(dna)

if __name__ == "__main__":
    main()
