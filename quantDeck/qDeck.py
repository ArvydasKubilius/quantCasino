from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, Aer
import math

def num_bits(n):
    return math.floor(math.log(n, 2)) + 1
	
SUITS = ["Diamonds", "Clubs", "Hearts", "Spades"]
VALUES = ["2", "3", "4", "5", "6", "7", "8", "9","10",
         "Jack", "Queen", "King", "Ace"]
		 
POWER = 6
DrawnCards = set()

def bitsToInt(bitlist):
    out = 0
    for bit in bitlist:
        out = (out << 1) | int(bit)
    return out  
	
def random_int():
    qc = QuantumCircuit(1, 1)

    qc.h(0)
    qc.measure(0, 0)
    
    backend = Aer.get_backend('qasm_simulator')
    counts = execute(qc, backend, shots = POWER, memory = True).result().get_memory()
    
    return bitsToInt(counts)
	
def shuffle():
    global DrawnCards 
    DrawnCards = set()
	
def draw():
    global DrawnCards
    n = random_int()
    while n > 51 or n in DrawnCards:
        n = random_int()
    DrawnCards.add(n)
    card = f"{VALUES[(n+1)%13]} of {SUITS[(n+1)//13]}"
    return card