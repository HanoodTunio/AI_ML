import pandas as pd 

mydataset = {
    'cars' : ["BMW", "Volvo", "Ford"],
    'passings' : [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print("Pandas use the loc attribute to return one or more specified row(s)")
print(myvar.loc[0])

print(myvar)

a = [1, 7, 2]
myvar1 = pd.Series(a)
print(myvar1)


x = [1, 2, 3, 4, 5]
myvar2 = pd.Series(x, index = ["v", "w", "x", "y", "z"])
print(myvar2)

calories = {'day1' : 420,
            'day2' : 380,
            'day3' : 390
            }
myvar3 = pd.Series(calories, index = ['day1', 'day2'])
print(myvar3)