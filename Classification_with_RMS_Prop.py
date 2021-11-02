import numpy as np
import matplotlib.pyplot as plt
from IPython import display
from Classificarion_SGD import Model_SGD

class Model_RMSPROP(Model_SGD):
    def __init__(self, X, y, epoches, n_iter, eta=0.05, batch_size=4, alpha = 0.9, eps = 1e-8):
        super().__init__(X, y, epoches, n_iter, eta, batch_size)
        self.g2 = np.zeros_like(self.w) # we start with None so that you can update this value correctly on the first iteration
        self.G = np.zeros_like(self.w)
        self.eps = eps
        self.betta = alpha
        self.title = "RMS_Prop"

    def fit(self):
        loss = []#np.zeros(self.epoches*len(self.X)//self.batch_size)
        plt.figure(figsize=(12, 5))

        for _ in range(self.epoches):
            for X_batch, y_batch in self.generate_batches():
                loss.append(self.compute_loss())                
                self.G = self.betta * self.G + (1-self.betta)*(self.compute_grad(X_batch, y_batch, self.w)**2)
                self.w = self.w - self.eta*self.compute_grad(X_batch, y_batch, self.w)/(np.sqrt(self.G + self.eps))
                
        self.visualize(self.title, self.X, self.y, self.w, loss)
            