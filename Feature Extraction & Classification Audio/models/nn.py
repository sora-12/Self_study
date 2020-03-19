import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
from sklearn.model_selection import train_test_split
import feat_extract
import tensorflow as tf

feat_extract.main()

X_train =  np.load('feat.npy')
y_train =  np.load('label.npy').ravel()

X_test=np.load('predict_feat_good.npy')
y_test=np.load('predict_label_good.npy').ravel()

# Build the Neural Network
model = Sequential()
model.add(Dense(512, activation='relu', input_dim=193))
model.add(Dropout(0.5))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2, activation='sigmoid'))

model.compile(optimizer='rmsprop',
              loss=tf.nn.sigmoid_cross_entropy_with_logits,
            #   loss='categorical_crossentropy',
              metrics=['accuracy'])
print(X_train.shape)
model.summary()
# Convert label to onehot

y_train = keras.utils.to_categorical(y_train, num_classes=2)
y_test = keras.utils.to_categorical(y_test, num_classes=2)



# Train and test
model.fit(X_train, y_train, epochs=100, batch_size=64)
score, acc = model.evaluate(X_test, y_test, batch_size=32)
print('Test score:', score)
print('Test accuracy:', acc)