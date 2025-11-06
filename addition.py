def calc(a, b):
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return sum, sub, mul, div

t = calc(100, 50)
print("The Results are")
for i in t:
    print(i)
