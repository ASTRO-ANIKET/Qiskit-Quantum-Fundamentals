from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit_ibm_runtime import Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

# Create 1-qubit circuit
qc = QuantumCircuit(1)

# Apply Hadamard -> creates superposition
qc.h(0)

# Measure
qc.measure_all()
print(qc.draw())

# Simulator backend
backend = AerSimulator()

# Transpile circuit
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_qc = pm.run(qc)

# Execute
sampler = Sampler(mode=backend)
job = sampler.run([isa_qc], shots=1000)
result = job.result()
counts = result[0].data.meas.get_counts()
print(counts)
plot_histogram(counts)

Expected Output: {'0': ~500, '1': ~500}
