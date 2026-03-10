from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit_ibm_runtime import Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

# Create circuit
qc = QuantumCircuit(2)

# Create Bell pair
qc.h(0)
qc.cx(0,1)

# Measure
qc.measure_all()
print(qc.draw())
backend = AerSimulator()
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_qc = pm.run(qc)
sampler = Sampler(mode=backend)
job = sampler.run([isa_qc], shots=1000)
result = job.result()
counts = result[0].data.meas.get_counts()
print(counts)
plot_histogram(counts)

Expected Result: 00 and 11 only
