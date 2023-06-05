from qiskit import *
%matplotlib inline
from qiskit.tools.visualization import plot_histogram

number_in_question = "10100101001"


circuit = QuantumCircuit(len(number_in_question)+1, len(number_in_question))

circuit.h(range(len(number_in_question)))
circuit.x(len(number_in_question))
circuit.h(len(number_in_question))


circuit.barrier()

for ii, yesno in enumerate(reversed(number_in_question)):
    if yesno == '1':
        circuit.cx(ii, len(number_in_question))


circuit.barrier()

circuit.h(range(len(number_in_question)))
circuit.barrier()
circuit.measure(range(len(number_in_question)), range(len(number_in_question)))


circuit.draw(output='mpl')


simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend=simulator, shots=1).result()
counts = result.get_counts()
print(counts)


plot_histogram(counts)