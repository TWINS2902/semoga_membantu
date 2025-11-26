# Algoritma Kruskal Optimize dengan predessecor list dan rank union
import sys
sys.setrecursionlimit(1000000)

class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

# Disjoint set union
class DSU:
    # Menginisiasi dengan mengisi list parent dan rank : Gambaran
    """
         Node   =  0  1  2  3  4, ...
    List parent = [0, 1, 2, 3, 4, ...]
    :-> Memiliki arti bahwa node 0 memiliki parent 0, dimana dia menggunakan index untuk menandakan node
    Contoh:
                0
               / \
              1   3
             /     \
            2       4
       node = i =  0  1  2  3  4  
    List parent = [0, 0, 1, 0, 3]
    Disitu node 1 memiliki parent 0 dan Node 2 memiliki parent 1 yang memiliki parent 0. 
    Ini konsep predessecor list
    """
    def __init__(self, N):
        self.parent = [i for i in range(N)] 
        self.rank = [1] * N # Untuk menandakan kisaran tinggi pohon

    # Fungsi mencari parent dari sebuah node. Menggunakan predessecor list
    def find(self, i):
        if (i == self.parent[i]): 
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    # Menggabungkan dua buah pohon terpisah
    def unite(self, x, y):
        # Dilakukan hanya jika parent dari x dan y berbeda jadi bisa digabung
        parentx, parenty = self.find(x), self.find(y)
        if (parentx != parenty):
            # Jika rank/tinggi pohon x < pohon y. Maka pohon y digabungkan ke x
            if (self.rank[parentx] < self.rank[parenty]): self.parent[parentx] = parenty
            elif (self.rank[parentx] > self.rank[parenty]): self.parent[parenty] = parentx
            else: 
                # Jika seri maka dipilih sembarang saja
                self.parent[parentx] = parenty 
                self.rank[parentx] += 1

# (Source, Destination, Weight)
N = 6
graph = [
    (0, 1, 1), (0, 2, 1),
    (1, 2, 4), (1, 4, 2),
    (4, 3, 13), (1, 3, 15),
    (2, 3, 5)
]

dsu = DSU(N)

edge_list = [Edge(s, d, w) for (s, d, w) in graph]
edge_list.sort(key= lambda var: var.weight)

ans = []
cost = 0
for edge in edge_list:
    if dsu.find(edge.source) != dsu.find(edge.destination):
        ans.append(edge)
        cost += edge.weight
        dsu.unite(edge.source, edge.destination)

print(cost)
for e in ans:
    print(f"source {e.source} to {e.destination}: {e.weight}")
