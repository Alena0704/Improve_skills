import numpy as np
import matplotlib.pyplot as plt
from IPython import display

class Model_SGD:
    def __init__(self, X, y, n_iter, eta=0.1, batch_size=4):
        self.X = self.__expand(X)
        self.y = y
        self.w = np.array([0, 0, 0, 0, 0, 1])
        self.n_iter = n_iter
        self.eta = eta
        self.batch_size = batch_size

    def __expand(self, X):
        """
        Adds quadratic features. 
        This expansion allows your linear model to make non-linear separation.
        
        For each sample (row in matrix), compute an expanded row:
        [feature0, feature1, feature0^2, feature1^2, feature0*feature1, 1]
        
        :param X: matrix of features, shape [n_samples,2]
        :returns: expanded features of shape [n_samples,6]
        """
        X_expanded = np.zeros((X.shape[0], 5))
        X_expanded[:,0]=X[:,0]
        X_expanded[:,1]=X[:,1]
        X_expanded[:,2] = X_expanded[:,0]**2
        X_expanded[:,3] = X_expanded[:,1]**2
        X_expanded[:,4] = X_expanded[:,0]*X_expanded[:,1]
        X_expanded = np.hstack((X_expanded,np.ones([X_expanded.shape[0],1])))
        return X_expanded

    def probability(X, w):
        """
        Given input features and weights
        return predicted probabilities of y==1 given x, P(y=1|x), see description above

        :param X: feature matrix X of shape [n_samples,6] (expanded)
        :param w: weight vector w of shape [6] for each of the expanded features
        :returns: an array of predicted probabilities in [0,1] interval.
        """
        a = X@w
        return 1./(1.+np.exp(-a))
    
    def compute_loss(self):
        """
        Given feature matrix X [n_samples,6], target vector [n_samples] of 1/0,
        and weight vector w [6], compute scalar loss function L using formula above.
        Keep in mind that our loss is averaged over all samples (rows) in X.
        """
        p = self.probability(self.X, self.w)
        p = np.clip(p, 1e-10, 1 - 1e-10)
        return -np.sum(self.y*np.log(p)+(1-self.y)*np.log(1-p))/len(self.X)

    def visualize(self, X, y, w, history):
        """draws classifier prediction with matplotlib magic"""
        h = 0.01
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
        Z = self.probability(self.expand(np.c_[xx.ravel(), yy.ravel()]), w)
        Z = Z.reshape(xx.shape)
        plt.subplot(1, 2, 1)
        plt.contourf(xx, yy, Z, alpha=0.8)
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        
        plt.subplot(1, 2, 2)
        plt.plot(history)
        plt.grid()
        ymin, ymax = plt.ylim()
        plt.ylim(0, ymax)
        display.clear_output(wait=True)
        plt.show()
    
    def compute_grad(self,X, y, w):
        """
        Given feature matrix X [n_samples,6], target vector [n_samples] of 1/0,
        and weight vector w [6], compute vector [6] of derivatives of L over each weights.
        Keep in mind that our loss is averaged over all samples (rows) in X.
        """
        p = self.probability(X, w)
        return 1./y.shape[0]*((p - y)@X)

    def fit(self):
        loss = np.zeros(self.n_iter)
        plt.figure(figsize=(12, 5))

        for i in range(self.n_iter):
            ind = np.random.choice(self.X.shape[0], self.batch_size)
            loss[i] = self.compute_loss()
            if i % 10 == 0:
                self.visualize(self.X[ind, :], self.y[ind], self.w, loss)

            # Keep in mind that compute_grad already does averaging over batch for you!
            self.w = self.w - self.eta * self.compute_grad(self.X[ind, :], self.y[ind], self.w)
            # TODO:<your code here>

        self.visualize(self.X, self.y, self.w, loss)