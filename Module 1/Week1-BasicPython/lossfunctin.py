#exercise 3
import random
def calculateloss(pred,target,loss_name):
  if loss_name == 'mse' or 'rmse':
    return (pred-target)**2
  elif loss_name == 'mae':
    return abs(pred-target)
num_samples = input('number of samples= ')
if not num_samples.isnumeric():
  print('number of samples must be an integer number')
  exit()
else:
  loss_name = input('loss name=')
  n = int(num_samples)
  for i in range(n):
    print('sample=',i)
    sumloss = 0
    pred = random.uniform(0.0,10.0)
    target = random.uniform(0.0,10.0)
    loss = calculateloss(pred,target,loss_name)
    print('pred =',pred)
    print('target =',target)
    print('loss =',loss)
    sumloss = sumloss + loss
  if loss_name == 'mae':
    print(' final mae=',sumloss/n)
  elif loss_name == 'mse':
    print(' final mse=',sumloss/n)
  elif loss_name == 'rmse':
    print(' final rmse=',np.sqrt(sumloss/n))