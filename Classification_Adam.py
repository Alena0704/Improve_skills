import numpy as np
import math
import matplotlib.pyplot as plt
from IPython import display
from Classification_Momentum import Model_Momentum, Model_SGD
from Classification_with_RMS_Prop import Model_RMSPROP

class Model_Adam(Model_RMSPROP, Model_Momentum):
    def __init__(self, X, y, epoches, n_iter, eta=0.05, batch_size=4, b1 = 0.25, b2 = 0.9, eps = 1e-8):
        Model_RMSPROP.__init__(self,X,y,epoches, n_iter,eta, batch_size, b2, eps)
        Model_Momentum.__init__(self, X,y,epoches, n_iter,eta,batch_size,b1)
        self.title = "Adam"

    def fit(self):
        loss = []#np.zeros(self.epoches*len(self.X)//self.batch_size)
        plt.figure(figsize=(12, 5))
        j=0
        for _ in range(self.epoches):
            for X_batch, y_batch in self.generate_batches():          
                self.G = (self.betta * self.G + (1-self.betta)*(self.compute_grad(X_batch, y_batch, self.w)**2))/(1-math.pow(self.betta, j+1))
                self.nu = (self.alpha * self.nu + (1-self.alpha) * self.compute_grad(X_batch, y_batch, self.w))/(1-math.pow(self.alpha, j+1))
                self.w = self.w - self.eta*self.nu/((self.G+self.eps)**0.5)  
                j+=1
                loss.append(self.compute_loss())
        
        self.visualize(self.title, self.X, self.y, self.w, loss)
        