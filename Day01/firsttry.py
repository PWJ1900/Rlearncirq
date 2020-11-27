import cirq

qubit = cirq.GridQubit(0, 0)


circuit = cirq.Circuit(cirq.X(qubit)**0.5,
                       cirq.measure(qubit, key='m')
                       )
print("Circuit:")
print(circuit)


#进行多次模拟
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)
print("Result:")
print(result)
