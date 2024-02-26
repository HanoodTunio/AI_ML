print("Example 01")
a = 33
b = 20
c = 23

if (a > b and a > c):
    print("a is greater")
elif (a < b or a < c):
    print("b or c is greater than a")

if (not ( not a > b)):
    print("a is not greater than b")

print("Example 02")
x = 30
if x > 20:
    print("Above ten,")
if x > 10:
    print("and also above 20!")
else:
    print("not greater number")


print("Example 03")
a = 33
b = 20
if (a>b):
    pass