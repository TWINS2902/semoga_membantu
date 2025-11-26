# huffman dengan kode encode dan decode
import heapq, sys
sys.setrecursionlimit(1000000)

# Membangun Node untuk membuat pohon
class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None

    # Untuk priority queue (min-heap)
    def __lt__(self, other):
        return self.freq < other.freq

# Mencatat frekuensi huruf
frequency = {}

# Mencatat hasil encode huruf
code = {}

# Ini akan menjelajahi pohon dan 
def printCode(root, s):
    if not root:
        return
    
    # Jika karakternya bukan '$' yang kita setting secara default
    if root.data != '$':
        print(f"{root.data}: {s}") # Akan print

    # Traversal kiri dan kanan
    printCode(root.left, s + "0")
    printCode(root.right, s + "1")

def storeCode(root, s):
    if root is None:
        return
    
    # Jika karakternya bukan '$' yang kita setting secara default
    if root.data != '$':
        code[root.data] = s # Akan simpan hasil decodenya

    # Traversal kiri dan kanan
    storeCode(root.left, s + "0")
    storeCode(root.right, s + "1")

def Huffman():
    pq = []

    # push semua node ke priority queue dimana akan mengsortir dia dari kemunculan terbanyak
    for ch, freq in frequency.items():
        heapq.heappush(pq, Node(freq, ch))

    # bangun tree
    while len(pq) > 1:
        # Ingat seperti kodenya, dia akan ambil dua huruf terkecil yang akan digabungkan
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)

        # Disini dia akan buat node baru dengan menggabungkan dua frekuensi dari huruf kiri dan kanan.
        # Diberikan huruf '$' karena ini bukan huruf encode melainkan gabungan dua huruf encode.
        temp = Node(left.freq + right.freq, '$')

        # Anak kiri dan kanan dari node akan diassign menjadi huruf yang membentuk dia
        temp.left = left
        temp.right = right

        # Masukkan balik ke PQ untuk di sort lagi dari frekuensi terkecil
        heapq.heappush(pq, temp)

    # Setelah pohon jadi, kira-kira seperti ini pohonnya. 
    """ Contoh:
    huruf: AAMMS

    freq = {
        A : 3
        M : 2
        S : 1
    }
    
    - Freq ini akan diubah menjadi Node Object jadi
        Node1 = freq:3, data:A 
        Node2 = freq:2, data:M 
        Node3 = freq:1, data:S
        PQ = [Node3, Node2, Node1] -> Disort dari freq menggunakan pq

    - Kemudian bangun pohon dia akan pop 2 PQ
        left  = Node3       |
        right = Node2       | Kondisi PQ setelah di pop, PQ = [Node1]

    - Setelah itu dia akan membuat node sementara untuk menampung node
        temp = Node( freq = Node2.freq + node3.freq, data = '$') 
        kemudian assign kiri dan kanan temp jadi nodenya
        temp.left  = Node3
        temp.right = Node2
        Kira-kira pohonnya seperti gini dengan Node = [data, freq]
                                temp
                               [3, '$']
                                /   \
                               /     \
                        [1, "S"]    [2, "M"]
                         Node3         Node2
    
    - Kemudian setelah dia membuat node itu, masukkan kembali ke PQ
        Kondisi PQ = [Node1(freq: 3, data: "A"), temp(freq:3, data: "$")]
    - Loop terus hingga pq sisa 1 node yakni root dari tree
    - Sehingga kondisi tree akan
                        [6, '$']
                         /    \ 
                        /      \
                    [3, '$']  [3, 'A']
                     /   \      Node1
                    /     \
                [1, "S"]  [2, "M"]
                Node3       Node2

    Kondisi PQ sisa satu, PQ = [Node(data: "$", freq: 6)]
    """
    root = pq[0]

    # jalankan store code untuk membuat rumus binarynya
    storeCode(root, "")
    return root


def decode(root, bits):
    out = ""
    curr = root

    # bits seperti : 0101011101 -> hasil encode pesan
    for b in bits:
        # Kalau bits = 0 dia kekiri, jika 1 maka kekanan
        if b == '0':
            curr = curr.left
        else:
            curr = curr.right

        # Jika mentok sampai bawah dimana kiri dan kanan itu kosong. Maka ini pasti huruf
        if curr.left is None and curr.right is None:  # leaf
            out += curr.data

            # Reset posisi kembali ke pohon untuk traversal bits sisa
            curr = root 

    return out

def Huffmanmain():
    global frequency, code
    frequency = {}
    code = {}

    s = "oooooaal"

    # hitung frekuensi
    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1

    # build tree
    root = Huffman()

    print("Character with their Huffman codes:")
    for ch, c in code.items():
        print(ch, c)

    # encode
    encoded = "".join(code[ch] for ch in s)
    print("Encoded Huffman data:", encoded)

    # decode
    decoded = decode(root, encoded)
    print("Decoded Huffman data:", decoded)

Huffmanmain()
