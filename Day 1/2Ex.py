#WAP for swapping without using third variable

a = 100
b = 200

print("Before Swapping:")
print("a =", a,"b =", b)

a = a + b
b = a - b
a = a - b

print("After Swapping:")
print("a =", a,"b =", b)
