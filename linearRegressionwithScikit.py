import matplotlib.pyplot as plt
import csv
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

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

regr = linear_model.LinearRegression()
#create linear regression object

regr.fit(price, Area)
#train the model

print('coefficients: \n', regr.coef_)
#The coefficient

print("Mean squared error: %.2f" % mean_squared_error(price, Area))
#Mean squared error

#print('Variance score: %.2f' % r2_score())
#Explained variance score: 1 is perfect prediction

plt.scatter(price, Area, color='black')
plt.plot()
plt.show()