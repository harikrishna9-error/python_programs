import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Add:", np.add(a, b))
print("All non-zero:", np.all(a))
print("Greater:", np.greater(b, a))
print("Greater equal:", np.greater_equal(b, a))
print("Less:", np.less(a, b))
print("Less equal:", np.less_equal(a, b))
print("Equal:", np.equal(a, b))
print("All close:", np.allclose(a, [1, 2, 3]))
print("Zeros:", np.zeros(3))
print("Ones:", np.ones(3))
print("Linspace:", np.linspace(0, 1, 5))
print("To list:", a.tolist())
