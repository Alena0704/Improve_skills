import numpy as np
import matplotlib.pyplot as plt
from Classificarion_SGD import Model_SGD
from Classification_Adam import Model_Momentum, Model_Adam, Model_RMSPROP

def show_picture(X, y):
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired, s=20)
    plt.show()

with open('train.npy', 'rb') as fin:
    X = np.load(fin)
    
with open('target.npy', 'rb') as fin:
    y = np.load(fin)

model_SGD = Model_SGD(X,y,100)
model_SGD.fit()

model_momentum = Model_Momentum(X,y,100)
model_momentum.fit()

model_Rms = Model_RMSPROP(X,y,100)
model_Rms.fit()

model_adam = Model_Adam(X,y,100)
model_adam.fit()