print("Example 01")
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

print("Example 02")
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

print("Example 03")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

print("Example 04")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

print("Example 05")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
thislist[1] = "blackcurrant"
print(thislist)
thislist.append("orange")
print(thislist)
thislist.insert(1, "orange")
print(thislist)
thislist.remove("orange")
print(thislist)
thislist.pop(1)
print(thislist)

# print("Example 06")
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)


print("Example 07")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)





