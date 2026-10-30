def double(n):
    result = n * 2
    return result

total = 0
for x in range(1, 4):
    total = total + double(x)
    print("x =", x, "total =", total)

print("Final total:", total)
