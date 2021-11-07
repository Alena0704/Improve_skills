import numpy as np
import matplotlib.pyplot as plt
from IPython import display
from Classificarion_SGD import Model_SGD

class Model_Momentum(Model_SGD):
    def __init__(self, X, y, epoches, n_iter, eta=0.05, batch_size=4, alpha=0.9):
        super().__init__(X, y, epoches, n_iter, eta, batch_size)
        self.alpha = alpha # momentum
        self.nu = np.zeros_like(self.w)
        self.title = "Momentum"

    def fit(self):
        loss = []#np.zeros(self.epoches*len(self.X)//self.batch_size)
        plt.figure(figsize=(12, 5))

        for _ in range(self.epoches):
            for X_batch, y_batch in self.generate_batches():
                               
                self.nu = self.alpha * self.nu + self.eta * self.compute_grad(X_batch, y_batch, self.w)
                self.w = self.w - self.nu
                #self.visualize(self.title,X_batch, y_batch, self.w, loss)
                loss.append(self.compute_loss())
        self.visualize(self.title, self.X, self.y, self.w, loss)
            

class Nesterov(Model_Momentum):
    def __init__(self, X, y, epoches, n_iter, eta=0.05, batch_size=4, alpha=0.9):
        super().__init__(X, y, epoches, n_iter, eta=eta, batch_size=batch_size, alpha=alpha)
        self.title = "Nesterov"
    
    def fit(self):
        loss = []#np.zeros(self.epoches)
        plt.figure(figsize=(12, 5))

        for _ in range(self.epoches):
            for X_batch, y_batch in self.generate_batches():
                
                self.nu = self.alpha * self.nu + self.eta * self.compute_grad(X_batch, y_batch, self.w-self.alpha * self.nu)
                self.w = self.w - self.nu
            #self.visualize(self.title,X_batch, y_batch, self.w, loss)
                loss.append(self.compute_loss())
        self.visualize(self.title, self.X, self.y, self.w, loss)
            