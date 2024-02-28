print("Examplpe01")
def my_function():
    print("Hello from a function")
my_function()



print("Example02")
def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")


print("Example03")

def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil", "Refsnes")


print("Example04")
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

print("Example05")
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

print("Example06")
def my_function(country = "Norway"):
    print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


print("Example07")
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)


print("Example07")
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

