import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
class model: 
    def __init__ (self,file_csv):
        self.dataset = pd.read_csv(file_csv)
        self.model = None
        self.history =None
        self.X = None 
        self.y = None  
    def preprocess(self):
        self.dataset = self.dataset.replace(',', '', regex=True)
        self.z = self.dataset.shape[0]
        self.data = self.dataset[['Open', 'High', 'Low', 'Close', 'Adj Close']].values
        x = np.array([self.data[0:self.z-6,:].T, self.data[1:self.z-5,:].T, self.data[2:self.z-4,:].T
                      ,self.data[3:self.z-3,:].T, self.data[4:self.z-2,:].T])
        self.X = x.reshape((self.z-6), -1)
        self.y = self.data[5:(self.z-1),:]
        self.X = self.X.astype(float)
        self.y = self.y.astype(float)
        
    def build_model(self):
        self.model = Sequential()
        self.model.add(Dense(1000,input_shape=(self.X.shape[1],),activation = 'relu'))
        self.model.add(Dense(500,activation='relu'))
        self.model.add(Dense(5, activation='linear'))
    
    def train_model(self, epochs, batch_size):
        self.model.compile(loss='mae', optimizer='adam', metrics=['accuracy'])
        self.history = self.model.fit(self.X, self.y, epochs=epochs, batch_size=batch_size)
    def predict_and_format(self):
        x1 = self.data[self.z-5:self.z,:].reshape(1, 25)
        y1 = [[float(item) for item in sublist] for sublist in x1]
        Y1 = self.model.predict(y1)
        formatted_Y1 = [['{:,.2f}'.format(value) for value in sublist] for sublist in Y1]
        return formatted_Y1
        
    def plot_loss(self):
        loss = self.history.history['loss']
        plt.plot(range(len(loss)), loss)
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.title('Loss per Epoch')
        plt.show()
