import csv
print("Enter File name: ")
filename = str(input()+'.csv')

exampleFile = open(filename)
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)

for values in exampleData[3:6]:
    print(values[0:2])
