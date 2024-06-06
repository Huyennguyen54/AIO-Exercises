y = float(input('y='))
y_hat = float(input('y_hat='))
n = int(input('n='))
p = int(input('p='))
loss = (y*(1/n)- y_hat*(1/n))**p
print(loss)