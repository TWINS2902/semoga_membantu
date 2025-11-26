# Prim Algorithm Optimize dengan PQ
import heapq, sys
sys.setrecursionlimit(1000000)

class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

def primAlgorithm(V, edges):
    # Build adjacency list

    adj = [[] for _ in range(V)]
    # Isinya akan seperti
    # Node:          0                 1
    #       [[(2, 3), (3, 1)], [(1, 1), (2, 1)], ...]
    # Menandakan bahwa node 0 bisa ke 2 dan 3 dengan weight 3 dan 1


    for e in edges:
        adj[e.source].append((e.destination, e.weight))
        adj[e.destination].append((e.source, e.weight))
    # karena undirected maka kalau ditambahkan dari source ke destination maka dia juga harus ada dari destination ke source

    pq = []  # (weight, node)

    # Menggunakan Heap (priority, queue) supaya weight yang kepilih selalu yang terkecil
    heapq.heappush(pq, (0, 0)) 

    # Ini untuk mencatat jika node itu telah dikunjungi
    visited = [False] * V 
    ans = []
    res = 0

    # Ini melakukan BFS [ Pelajarin BFS kalau bingung ]
    while pq:
        weight, node = heapq.heappop(pq)

        if visited[node]:
            continue

        ans.append((weight, node))
        res += weight
        visited[node] = True

        # Setiap tetangga dari node nya akan di cek
        for nextNode, edgeWeight in adj[node]:
            if not visited[nextNode]:
                # Kalau belum pernah dikunjungi masukkan ke priority queue
                heapq.heappush(pq, (edgeWeight, nextNode))

    # Output
    print(res)
    print("Visited Node:")
    for i, (w, n) in enumerate(ans, start=1):
        print(f"{i}. {n} : {w}")


def primMain():
    graph = [
        (0, 1, 10), 
        (1, 3, 15), 
        (2, 3, 4), 
        (2, 0, 6), 
        (0, 3, 5)
    ]

    edges = [Edge(u, v, w) for u, v, w in graph]

    # Disini ada PR baru, 3 kan disitu banyaknya node. Gimana cara mencari total node jika inputnya seperti
    """ S D W
        0 1 10
        1 3 15
        2 3 4
        2 0 6
        0 3 5

    S = Source, D = destination, W = weight
    """
    primAlgorithm(4, edges)

primMain()
