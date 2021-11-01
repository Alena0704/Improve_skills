import numpy as np
import matplotlib.pyplot as plt
from IPython import display
from Classification_Momentum import Model_Momentum
from Classification_with_RMS_Prop import Model_RMSPROP


class Model_Adam(Model_RMSPROP, Model_Momentum):
    def __init__(self, X, y, n_iter, eta=0.05, batch_size=4, b1 = 0.9, b2 = 0.999, eps = 1e-8):
        Model_RMSPROP.__init__(self,X,y,n_iter,eta, batch_size, b2, eps)
        Model_Momentum.__init__(self, X,y,n_iter,eta,batch_size,b1)
                

    def fit(self):
        loss = np.zeros(self.n_iter)
        plt.figure(figsize=(12, 5))

        for i in range(self.n_iter):
            ind = np.random.choice(self.X.shape[0], self.batch_size)
            loss[i] = self.compute_loss()
            if i % 10 == 0:
                self.visualize(self.X[ind, :], self.y[ind], self.w, loss)
            
            self.G = (self.betta * self.G + (1-self.betta)*(self.compute_grad(self.X[ind, :], self.y[ind], self.w)**2))/(1-self.betta**i)
            self.nu = (self.alpha * self.nu + (1-self.alpha) * self.compute_grad(self.X[ind, :], self.y[ind], self.w))/(1-self.alpha**i)

            self.w = self.w - self.eta*self.nu/(self.G+self.eps)**0.5

        self.visualize(self.X, self.y, self.w, loss)