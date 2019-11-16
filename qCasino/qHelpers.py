from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, Aer
import math

def num_bits(n):
    return math.floor(math.log(n, 2)) + 1

def bitsToInt(bitlist):
    out = 0
    for bit in bitlist:
        out = (out << 1) | int(bit)
    return out  
	
def random_int(n):
    qc = QuantumCircuit(1, 1)

    qc.h(0)
    qc.measure(0, 0)
    
    backend = Aer.get_backend('qasm_simulator')
    counts = execute(qc, backend, shots = n, memory = True).result().get_memory()
    
    return bitsToInt(counts)