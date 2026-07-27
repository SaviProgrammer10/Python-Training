# Swap 3 numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("\nBefore Swapping:")
print("a =", a)
print("b =", b)
print("c =", c)

# Swapping
temp = a
a = b
b = c
c = temp

print("\nAfter Swapping:")
print("a =", a)
print("b =", b)
print("c =", c)