import numpy as np

class LinearRegression:
    def __init__(self, X,Y):
        self.X = np.hstack((np.ones((X.shape[0],1)),X))
        self.W = np.zeros((self.X.shape[1]))
        self.Y = Y
        self.lr = 1e-2
    
    def MSE(self):
        return (np.sum(self.X @ self.W-self.Y)**2)/self.X.shape[0]
    
    def fit(self, iters = 10000):
        losses = []
        for _ in range(iters):
            self.W = self.W - self.lr * 2*self.X.T @ (self.X @ self.W-self.Y)/self.X.shape[0]
            if _%10==0:
                losses.append(self.MSE())
    def predict(self):
        return self.X@self.W

objects_num = 50
X1 = np.linspace(-5, 5, objects_num)
X2 = np.linspace(1, 10, objects_num)
y = 6 + 5 * X1 - 4 * X2 + np.random.randn(objects_num) * 5
X = np.hstack((X1.reshape((50, 1)), X2.reshape(50, 1)))

from sklearn import preprocessing
maker = preprocessing.StandardScaler()
X = maker.fit_transform(X)

regressor = LinearRegression(X,y)
regressor.fit()
print(regressor.MSE())

        