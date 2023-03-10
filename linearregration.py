import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('sample.csv')
print(df)

x = df[['area']]
y = df[['price']]

plt.scatter(df['area'], df['price'])
plt.xlabel('Area')
plt.ylabel('Price')
plt.title('Home Rent')

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=.30, random_state=1)

reg = LinearRegression()
reg.fit(xtrain, ytrain)
reg.predict(xtest)

plt.scatter(df['area'], df['price'])
plt.xlabel('Area')
plt.ylabel('Price')
plt.title('Home Rent')
plt.plot(df.area, reg.predict(df[['area']]))
plt.show()

print(reg.predict([[39000]]))
