import cirq

#本页代码就是先定义电路网格
#使用命名的量子比特
q0 = cirq.NamedQubit('source')#此处创建名字的一个比特
q1 = cirq.NamedQubit('target')#此处创建名字

#1、量子比特可以被分开的创建
q3 = cirq.LineQubit(3)

#1、这是一条直线上的0-2的位置
q0, q1, q2 = cirq.LineQubit.range(3)

#1、量子方格也可以被逐一的定范围
q4_5 = cirq.GridQubit(4, 5)


#1、或者创建一个正方形的矩阵
qubits = cirq.GridQubit.square(4)


print()

#还有一些预打包的qubit集，称为Devices，这位google早期的2X11的，cirq.Device可用于将邻接规则和其他硬件约束应用于量子电路
print(cirq.google.Foxtail)
