import cirq

#举个例子(许多算术运算也可以应用于门。这里有些例子)
#一个门是可以应用于一组量子位的效果
#一个operation是应用于一组量子位的门。

#比如一个Gate对象为cirq.xxx
#而一个Operation对象为cirq.xxx(cirq.LineQubit(1))意思是这是应用于特定量子位的xxx门

not_gate = cirq.CNOT
pauli_z = cirq.Z


#使用求幂来获得一个门的平方根
sqrt_x_gate = cirq.X**0.5
sqrt_iswap = cirq.ISWAP**0.5


#一些门也可以获取参数
sqrt_sqrt_y = cirq.YPowGate(exponent=0.25)


#举行为的例子
q0, q1 = cirq.LineQubit.range(2)
z_op = cirq.Z(q0)
not_op = cirq.CNOT(q0, q1)
sqrt_iswap_op = sqrt_iswap(q0, q1)
print(sqrt_iswap_op)
