import numpy as np
import matplotlib.pyplot as plt
from IPython import display
from Classificarion_SGD import Model_SGD

class Model_RMSPROP(Model_SGD):
    def __init__(self, X, y, n_iter, eta=0.05, batch_size=4, alpha = 0.9, eps = 1e-8):
        super().__init__(X, y, n_iter, eta, batch_size)
        self.g2 = np.zeros_like(self.w) # we start with None so that you can update this value correctly on the first iteration
        self.G = np.zeros_like(self.w)
        self.eps = eps
        self.betta = alpha

    def fit(self):
        loss = np.zeros(self.n_iter)
        plt.figure(figsize=(12, 5))

        for i in range(self.n_iter):
            ind = np.random.choice(self.X.shape[0], self.batch_size)
            loss[i] = self.compute_loss()
            if i % 10 == 0:
                self.visualize(self.X[ind, :], self.y[ind], self.w, loss)
            
            self.G = self.betta * self.G + (1-self.betta)*(self.compute_grad(self.X[ind, :], self.y[ind], self.w)**2)
            self.w = self.w - self.eta*self.compute_grad(self.X[ind, :], self.y[ind], self.w)/(np.sqrt(self.G + self.eps))

        self.visualize(self.X, self.y, self.w, loss)