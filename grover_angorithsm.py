from qiskit import QuantumCircuit, transpile, assemble
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from qiskit_aer import Aer
import numpy as np

def grover_oracle(circuit, qubits, k):
    """Oracle to flip the amplitude of the state corresponding to the value k."""
    k_bin = f'{k:0{len(qubits)}b}'
    for i, bit in enumerate(k_bin):
        if bit == '0':
            circuit.x(qubits[i])
    circuit.h(qubits[-1])
    circuit.mcx(list(qubits[:-1]), qubits[-1])  # Multi-controlled X gate
    circuit.h(qubits[-1])
    for i, bit in enumerate(k_bin):
        if bit == '0':
            circuit.x(qubits[i])

def grover_diffusion(circuit, qubits):
    """Diffusion operator (amplitude amplification)."""
    circuit.h(qubits)
    circuit.x(qubits)
    circuit.h(qubits[-1])
    circuit.mcx(list(qubits[:-1]), qubits[-1])  # Multi-controlled X gate
    circuit.h(qubits[-1])
    circuit.x(qubits)
    circuit.h(qubits)

def grover_search(n, k):
    """Grover's search algorithm to find element k in a list of size 2^n."""
    num_qubits = n + 1  # Including the ancilla qubit
    qc = QuantumCircuit(num_qubits, n)

    # Apply Hadamard gates to all qubits
    qc.h(range(n))

    # Add initial ancilla qubit to |-> state
    qc.x(n)
    qc.h(n)

    # Number of iterations
    iterations = int(np.pi / 4 * np.sqrt(2**n))

    for _ in range(iterations):
        # Apply the Grover oracle
        grover_oracle(qc, range(n+1), k)
        # Apply the Grover diffusion operator
        grover_diffusion(qc, range(n))

    # Measure the first n qubits
    qc.measure(range(n), range(n))

    # Use Aer's qasm_simulator
    simulator = Aer.get_backend('qasm_simulator')

    # Execute the circuit on the qasm simulator
    compiled_circuit = transpile(qc, simulator)
    qobj = assemble(compiled_circuit)
    result = simulator.run(qobj).result()

    # Get the counts of the results
    counts = result.get_counts(qc)
    return counts

# Example usage
n = 4  # Number of qubits to represent the list
k = 5  # Element to search for (must be less than 2^n)
counts = grover_search(n, k)

# Plot the results
print("Measurement results:", counts)
plot_histogram(counts)
plt.show()
