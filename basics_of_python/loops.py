print("Example01")
i = 1
while i < 6:
    print(i)
    i += 1

print("Example02")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print("Example03")
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


print("Example04")
i = 1
while i < 6:
    print(i)
    if i == 3:
        i += 1
        continue    
    i += 1