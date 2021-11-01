import numpy as np
import matplotlib.pyplot as plt
from IPython import display
from Classificarion_SGD import Model_SGD

class Model_Momentum(Model_SGD):
    def __init__(self, X, y, n_iter, eta=0.05, batch_size=4, alpha=0.9):
        super().__init__(X, y, n_iter, eta, batch_size)
        self.alpha = alpha # momentum
        self.nu = np.zeros_like(self.w)

    def fit(self):
        loss = np.zeros(self.n_iter)
        plt.figure(figsize=(12, 5))

        for i in range(self.n_iter):
            ind = np.random.choice(self.X.shape[0], self.batch_size)
            loss[i] = self.compute_loss()
            if i % 10 == 0:
                self.visualize(self.X[ind, :], self.y[ind], self.w, loss)
            
            self.nu = self.alpha * self.nu + self.eta * self.compute_grad(self.X[ind, :], self.y[ind], self.w)
            self.w = self.w - self.nu
            # TODO:<your code here>

        self.visualize(self.X, self.y, self.w, loss)
