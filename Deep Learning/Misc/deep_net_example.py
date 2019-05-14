# -*- coding: utf-8 -*-

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

'''

Process: (Feed forward NN)

input > weights > hidden layer 1 (activation function) > weights > hidden layer 2
(activation function) > weights > output layer

compare output to intended output > cost function (cross entropy)

optimization function (optimizer) > minimize cost (AdamOptimizer, SDG, Adagrad)


backpropagation

feed forward + backpropagation = epoch


'''


mnist = input_data.read_data_sets('/tmp/data', one_hot=True)


# 10 classes : 0 - 9

'''
One hot means: one element = 1 rest all = 0
    
0 = [1,0,0,0,0,0,0,0,0,0]
1 = [0,1,0,0,0,0,0,0,0,0]
2 = [0,0,1,0,0,0,0,0,0,0]
3 = [0,0,0,1,0,0,0,0,0,0]

''' 

# Hidden layers and nodes
n_nodes_hidden_l1 = 500
n_nodes_hidden_l2 = 500
n_nodes_hidden_l3 = 500


n_classes = 10
batch_size = 100

X = tf.placeholder('float',[None, 784])
y = tf.placeholder('float')


def neural_network_model(data):
    
    hidden_1_layer = {'weights': tf.Variable(tf.random_normal([784, n_nodes_hidden_l1])),
                      'biases': tf.Variable(tf.random_normal([n_nodes_hidden_l1]))}
    
    hidden_2_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hidden_l1, n_nodes_hidden_l2])),
                      'biases': tf.Variable(tf.random_normal([n_nodes_hidden_l2]))}
    
    hidden_3_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hidden_l2, n_nodes_hidden_l3])),
                      'biases': tf.Variable(tf.random_normal([n_nodes_hidden_l3]))}
    
    output_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hidden_l3, n_classes])),
                      'biases': tf.Variable(tf.random_normal([n_classes]))}

    
    # (input_data * weights) + biases
    l1 = tf.add( tf.matmul(data, hidden_1_layer['weights']), hidden_1_layer['biases'])
    l1 = tf.nn.relu(l1)
    
    l2 = tf.add( tf.matmul(l1, hidden_2_layer['weights']), hidden_2_layer['biases'])
    l2 = tf.nn.relu(l2)

    l3 = tf.add( tf.matmul(l2, hidden_3_layer['weights']), hidden_3_layer['biases'])
    l3 = tf.nn.relu(l3)
    
    output = tf.matmul(l3, output_layer['weights']) + output_layer['biases']
    
    return output



def train_neural_network(X):
    # Get output from neural network
    prediction = neural_network_model(X)
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



