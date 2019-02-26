# -*- coding: utf-8 -*-

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data




mnist = input_data.read_data_sets('/tmp/data', one_hot=True)


n_classes = 10
batch_size = 128

X = tf.placeholder('float',[None, 784])
y = tf.placeholder('float')



def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1,1,1,1], padding='SAME')


def maxpool2d(X):
    return tf.nn.max_pool(X, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')


def convolution_neural_network(X):
    
    weights = { # 5X5 convolution, 1 input, 32 output
                'W_conv1': tf.Variable(tf.random_normal([5, 5, 1, 32])),
                'W_conv2': tf.Variable(tf.random_normal([5, 5, 32, 64])),
                # W_fully_connected = densly connected
                'W_fully_connected': tf.Variable(tf.random_normal([7*7*64, 1024])),
                'output': tf.Variable(tf.random_normal([1024, n_classes]))}
    
    biases = {# 5X5 convolution, 1 input, 32 output
                'b_conv1': tf.Variable(tf.random_normal([32])),
                'b_conv2': tf.Variable(tf.random_normal([64])),
                # W_fully_connected = densly connected
                'b_fully_connected': tf.Variable(tf.random_normal([1024])),
                'output': tf.Variable(tf.random_normal([n_classes]))}
    
    X = tf.reshape(X, shape=[-1, 28, 28, 1])
    
    conv1 = tf.nn.relu(conv2d(X, weights['W_conv1']) + biases['b_conv1'])
    conv1 = maxpool2d(conv1)
    
    conv2 = tf.nn.relu(conv2d(conv1, weights['W_conv2']) + biases['b_conv2'])
    conv2 = maxpool2d(conv2)
    
    fully_connected = tf.reshape(conv2, [-1, 7*7*64])
    fully_connected = tf.nn.relu(tf.matmul(fully_connected, weights['W_fully_connected']) +
                                 biases['b_fully_connected'])
    
    
    output = tf.matmul(fully_connected, weights['output']) + biases['output']
    
    return output



def train_neural_network(X):
    
    # Get output from neural network
    prediction = convolution_neural_network(X)
    # Get cost
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))

    # default learning rate = 0.001
    optimizer = tf.train.AdamOptimizer().minimize(cost)
    
    # Cycles of feed forward + backpropagation
    n_epochs = 10
    
    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())

        # Training data
        for epoch in range(n_epochs):
            epoch_loss = 0
            
            for _ in range(int(int(mnist.train.num_examples/batch_size))):
                epoch_X, epoch_y = mnist.train.next_batch(batch_size)
                _, c = sess.run([optimizer,cost], feed_dict={X: epoch_X, y: epoch_y}) # c = cost
                epoch_loss += c
            print('Epoch:', epoch, 'completed out of', n_epochs, 'loss:', epoch_loss)
             
        
        
        # 
        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y,1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
        print('Accuracy:', accuracy.eval({X:mnist.test.images, y: mnist.test.labels}))



train_neural_network(X)



