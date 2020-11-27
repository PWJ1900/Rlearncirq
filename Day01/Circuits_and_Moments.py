import cirq

circuit = cirq.Circuit()#首先创建一个电路来，可以通过添加电路来创建它
circuit.append(cirq.H(q) for q in cirq.LineQubit.range(3))
# 由于没有重叠，所有闸门都置于相同的时刻
print(circuit)


# 我们页可以直接创建一个电路
print(cirq.Circuit((cirq.SWAP(q, q+1) for q in cirq.LineQubit.range(3))))

#不希望cirq自动将操作一直移到最左边。要在不执行此操作的情况下构建电路，可以按瞬间创建电路，也可以使用其他方法
# 在单独的时刻创建每个门。
print(cirq.Circuit(cirq.Moment([cirq.H(q)]) for q in cirq.LineQubit.range(3)))
