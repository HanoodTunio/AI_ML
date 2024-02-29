print("Example 01")
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

print("Example02")
thistuple = ("apple", "banana", "cherry")
y = list(thistuple) 
y.append("orange")
thistuple = tuple(y)
print(thistuple)
