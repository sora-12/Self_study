from __future__ import absolute_import, division, print_function, unicode_literals, unicode_literals
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

from tensorflow import keras
from sklearn.model_selection import train_test_split

import numpy as np


X=  np.load('feat_big.npy')
y = np.load('label_big.npy')
y=y.reshape(-1,1)
print(X.shape)
print(y.shape)
# model train & evaluation set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
y_train = keras.utils.to_categorical(y_train, num_classes=2)
y_test = keras.utils.to_categorical(y_test, num_classes=2)

learning_rate=0.1
training_epochs=300
batch_size=100


X=tf.placeholder(tf.float32,[None,193])
y=tf.placeholder(tf.float32,[None,2])


with tf.name_scope('layer1') as scope:
  W1=tf.Variable(tf.random_normal([193,256]),name="W1")
  b1=tf.Variable(tf.random_normal([256]))
  L1=tf.nn.relu(tf.matmul(X,W1)+b1)
  L1=tf.nn.dropout(L1,keep_prob=0.5)

with tf.name_scope('layer2') as scope:
  W2=tf.Variable(tf.random_normal([256,256]),name="W2")
  b2=tf.Variable(tf.random_normal([256]))
  L2=tf.nn.relu(tf.matmul(L1,W2)+b2)
  L2=tf.nn.dropout(L2,keep_prob=0.5)

with tf.name_scope('layer3') as scope:
  W3=tf.Variable(tf.random_normal([256,128]),name="W3")
  b3=tf.Variable(tf.random_normal([128]))
  L3=tf.nn.relu(tf.matmul(L2,W3)+b3)
  L3=tf.nn.dropout(L3,keep_prob=0.5)

with tf.name_scope('layer4') as scope:
  W4=tf.Variable(tf.random_normal([128,2]),name="W4")
  b4=tf.Variable(tf.random_normal([2]))
  L4=tf.nn.sigmoid(tf.matmul(L3,W4)+b4)
  hypothesis=tf.matmul(L3,W4)+b4

cost=tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=hypothesis,labels=y))
optimizer=tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

correct_prediction = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# loss와 accuracy scalar 저장
tf.summary.scalar("loss",cost)
tf.summary.scalar("accuracy",accuracy)


with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  writer=tf.summary.FileWriter("./log/",sess.graph)
  merged_summary=tf.summary.merge_all()
  for epoch in range(training_epochs):
    avg_cost=0
    total_batch=int(X_train.shape[0]/batch_size)
    

    for i in range(total_batch):
      idx=i*batch_size
      batch_xs,batch_ys=X_train[idx:idx+batch_size],y_train[idx:idx+batch_size]
      c,_=sess.run([cost,optimizer],feed_dict={X:batch_xs,y:batch_ys})
      avg_cost+=c/total_batch
      summary=sess.run(merged_summary,feed_dict={X:batch_xs,y:batch_ys})
      writer.add_summary(summary,global_step)


    print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.9f}'.format(avg_cost))

  print("---------------------------------------------------------------------")

  print('Learning Finished!')




  print('Accuracy:', sess.run(accuracy, feed_dict={X: X_test, y: y_test}))