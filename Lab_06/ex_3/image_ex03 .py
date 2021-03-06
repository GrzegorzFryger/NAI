# -*- coding: utf-8 -*-
"""image_ex03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1glIFdNT20bar8MgFISOLAzY1gvnNkHbH
"""

def printCostPlot(iteration, fit):
    plt.figure(figsize=(8,6))
    plt.plot(range(1, iteration + 1), fit.history['loss'])
    plt.plot(range(1, iteration +1 ), fit.history['acc'])
    plt.show()


    
import keras
import tensorflow as tf
import tensorflow.keras as keras
import matplotlib.pyplot as plt
import numpy as np

from keras.models import Sequential
from keras.layers import MaxPooling2D
from keras.layers import Conv2D
from keras.layers import InputLayer
from keras.datasets import cifar100
from keras.layers import Dense
from keras.layers import Flatten

       
(x_train, y_train),(x_test, y_test) = tf.keras.datasets.mnist.load_data()

#Models 
model = Sequential([
    Flatten(),
    Dense(32, activation='relu', input_shape=(28, 28, 1) ),
    Dense(32, activation='relu'),
    Dense(32, activation='relu'),
    Dense(32, activation='relu'),
    Dense(32, activation='relu'),
    Dense(32, activation='relu'),
    Dense(32, activation='relu'),
    Dense(10, activation='softmax')
])

model2 = Sequential([
    Flatten(),
    Dense(64, activation='relu', input_shape=(28, 28, 1) ),
    Dense(64, activation='relu'),
    Dense(64, activation='relu'),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

model3 = Sequential([
    Flatten(),
    Dense(128, activation='relu', input_shape=(28, 28, 1) ),
    Dense(128, activation='relu'),
    Dense(128, activation='relu'),
    Dense(128, activation='relu'),
    Dense(28, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model2.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model3.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#Training data  
data_train1 = model.fit(x_train, y_train, epochs=3)
model_loss, model_acc = model.evaluate(x_test, y_test)
print(model.summary())
print('Model 1 result loss: {:4f}'.format(model_loss))
print('Model 1 final accuracy: {:4f}'.format(model_acc))
printCostPlot(3, data_train1)

data_train2 = model2.fit(x_train, y_train, epochs=3)
model2_loss, model2_acc = model2.evaluate(x_test, y_test)
print(model2.summary())
print('Model 2 result loss: {:4f}'.format(model2_loss))
print('Model 2 final accuracy: {:4f}'.format(model2_acc))
printCostPlot(3, data_train2)

data_train3 = model3.fit(x_train, y_train, epochs=3)
model3_loss, model3_acc = model3.evaluate(x_test, y_test)
print(model3.summary())
print('Model 3 result loss: {:4f}'.format(model3_loss))
print('Model 3 final accuracy: {:4f}'.format(model3_acc))
printCostPlot(3, data_train3)


#Predict
predic1 = model.predict(x_test)
predic2 = model2.predict(x_test)
predic3 = model3.predict(x_test)

print("\n\n Predict model1 ")
plt.imshow(x_test[2],cmap=plt.cm.binary)
plt.show()
print("\n\n in the picture you can see :" + str(np.argmax(predic1[2])))

print("\n\n Predict model2 ")
plt.imshow(x_test[3],cmap=plt.cm.binary)
plt.show()
print("\n\n in the picture you can see :" + str(np.argmax(predic2[3])))

print("\n\n Predict model3 ")
plt.imshow(x_test[7],cmap=plt.cm.binary)
plt.show()
print("\n\n in the picture you can see :" + str(np.argmax(predic3[7])))

