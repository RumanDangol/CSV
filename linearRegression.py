import csv
import matplotlib.pyplot as plt
import numpy as np
filename = str('house-price.csv')

exampleFile = open(filename)
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
price = []
Area = []
# print(exampleData)

for values in exampleData[1:]:
    price.append(int(values[0]))

    Area.append(int(values[1]))

price.sort()
Area.sort()
meanofArea = np.mean(Area)
meanofPrice = np.mean(price)
y1 = []
def calB1(price, Area):
    a = int(len(price))
    i = 0
    for i in range(1,a):
        B1 = np.sum((Area[i] - meanofArea) * (price[i] - meanofPrice)) / np.sum((Area[i] - meanofArea) ** 2)
        i = i + 1
    return B1

valueofB1 = calB1(price, Area)

def calB0(valueofB1):
    B0 = meanofPrice - valueofB1 * meanofArea
    return B0


valueofB0 = calB0(valueofB1)
for i in Area:
    y1.append(int(valueofB0 + valueofB1 * i))





plt.figure(1)
plt.subplot(221)
plt.plot(price, Area)
plt.plot(y1, Area,  color="red")
plt.grid(True)
plt.title('Area and their Prices')
plt.xlabel('Price')


plt.ylabel('Area')



#plt.figure(2)
plt.subplot(222)
plt.ylabel('Prices')
plt.plot(price)
plt.title('Prices')
plt.xlabel('No. of Houses')

def calB1(price, Area):
    a = int(len(price))
    i = 0

    for i in range(1,a):
        B1 = np.sum((Area[i] - meanofArea) * (price[i] - meanofPrice)) / np.sum((Area[i] - meanofArea) ** 2)
        i = i + 1
    return B1



def calB0(valueofB1):
    B0 = meanofPrice - valueofB1 * meanofArea
    return B0


# plt.figure(3)
plt.subplot(223)
plt.plot(Area)
plt.ylabel('Areas')
plt.xlabel('No. of Houses')
plt.title('Prices')

plt.show()









plt.show()