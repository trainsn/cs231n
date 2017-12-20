import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  dim , num_class = W.shape
  num_train = X.shape[0]
  for i in xrange(num_train):
      pro = X[i].dot(W)
      pro = np.exp(pro)
      psum = np.sum(pro)
      loss += -np.log(pro[y[i]]/psum)  
      for j in xrange(num_class):
          if j == y[i]:
              dW[:,j]+= X[i,:]*(-psum + pro[y[i]])/psum
          else :
              dW[:,j]+= X[i,:]*pro[j]/psum
               
  loss /= num_train 
  loss += 0.5 * reg * np.sum(W * W)
  
  dW /= num_train
  dW += reg * W
       
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  dim , num_class = W.shape
  num_train = X.shape[0]
  pro = np.exp(X.dot(W))
  psum = np.sum(pro,1)
  pro = pro / np.reshape(psum,(num_train,1))
  
  idx = range(0,num_train)
  loss = np.sum(-np.log(pro[idx,y]))
  loss /= num_train 
  loss += 0.5 * reg * np.sum(W * W)
  
  dW = X.T.dot(pro)
  dW_ 
  dW /= num_train
  dW += reg * W
  
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

