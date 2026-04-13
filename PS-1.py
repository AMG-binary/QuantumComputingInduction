from qiskit import QuantumCircuit
from qiskit_aer import Aer
import matplotlib.pyplot as plt

qc=QuantumCircuit(2,2)
qc.h(0)
qc.cx(0,1)
qc.measure([0,1] , [0,1])

qc.draw(output='mpl')
plt.show()


backend = Aer.get_backend("qasm_simulator")
job = backend.run(qc,shots=1024)
result = job.result()

print("Measurement outcomes:",result.get_counts())