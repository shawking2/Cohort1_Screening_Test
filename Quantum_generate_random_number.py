from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Global variable to count the number of times a random number is generated
total_generated = 0

# Dictionary to store the number of times each random number is generated
number_counts = {}

def generate_random_number(min_value, max_value):
    global total_generated

    # Check if the min_value is greater than the max_value
    if min_value > max_value:
        raise ValueError(
            "Invalid range: Minimum value should be less than or equal to the maximum value")

    # Determine the number of bits required to represent max_value
    num_bits = len(bin(max_value)) - 2

    # Create a quantum circuit with num_bits qubits and num_bits cbits
    circuit = QuantumCircuit(num_bits, num_bits)
    
    # Apply Hadamard gates to all qubits to put them in superposition
    circuit.h(range(num_bits))
    
    # Measure the qubits and store the results in the corresponding cbits
    circuit.measure(range(num_bits), range(num_bits))

    # Draw the quantum circuit
    #circuit.draw(output='mpl')
    #plt.show()

    # Use the Aer simulator to run the quantum circuit
    backend = Aer.get_backend('qasm_simulator')
    transpiled_circuit = transpile(circuit, backend=backend)
    result = backend.run(transpiled_circuit).result()
    
    # Get the measurement results from the simulator
    counts = result.get_counts(circuit)

    # Plot the histogram of results
    #plot_histogram(counts)
    #plt.show()

    # Select the first bit string from the measurement results (in this case, only running 1 shot)
    random_bitstring = list(counts.keys())[0]
    random_number = int(random_bitstring, 2)

    # Ensure the random number is within the specified range
    random_number = min(max(random_number, min_value), max_value)

    # Update the number of times the random number has been generated in the dictionary
    number_counts[random_number] = number_counts.get(random_number, 0) + 1
    total_generated += 1

    return random_number

def main():
    n = abs(int(input("Enter the number of bits (n must be a positive value): ")))
    # Example usage of the function to generate random numbers in the range from 10 to 20
    min_value = 0
    max_value = 2**n - 1
    list_n = []
    while len(list_n) < 2*n:
        random_number = generate_random_number(min_value, max_value)
        if random_number not in list_n:
            list_n.append(random_number)
    print(list_n)

if __name__ == "__main__":
    main()
