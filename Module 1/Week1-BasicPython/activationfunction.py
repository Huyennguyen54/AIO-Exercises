#exercise 2
import numpy as np

def is_number (n) :
  try :
    float (n)
  except ValueError :
    return False
  return True

def is_activation(x):
  if x in ['sigmoid','relu','elu']:
    return True
  else:
    return False

def relu_(x):
  if x > 0:
    return x
  else:
    return 0

def sigmoid_(x):
  return 1/(1+np.exp(-x))

def elu_(x):
  if x > 0:
    return x
  else:
    return 0.01*(np.exp(x)-1)

x = input('x=')
if not is_number(x):
  print('x must be a number')
  exit()
else:
  activation = input('activation function = ')
  if not is_activation(activation):
    print(activation,'is not supported')
    exit()
  else:
    if activation == 'sigmoid':
      print(sigmoid_(float(x)))
    elif activation == 'relu':
      print(relu_(float(x)))
    elif activation == 'elu':
      print(elu_(float(x)))
