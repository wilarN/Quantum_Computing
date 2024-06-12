from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

gc = QuantumCircuit(2, 2) # Quantum register with 2 qubits and 2 classical bits

gc.h(0) # Apply Hadamard gate to qubit 0. It is in superposition now
gc.cx(0, 1) # Apply CNOT gate with control qubit 0 and target qubit 1. Entanglement is created. (0 = control qbit, 1 = target qbit). If qubit 0 is 1, qubit 1 will be flipped.
gc.measure_all() # Measure all qubits and store the result in classical bits

simulator = Aer.get_backend('qasm_simulator') # Use the qasm simulator.

result = execute(gc, simulator, shots=1000).result() # Execute the circuit 1000 times
counts = result.get_counts(gc) # Get the counts
print(counts)

plot_histogram(counts) # Plot the histogram