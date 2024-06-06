#exercise 4
x = float(input('x='))
n = int(input('n='))
def giaithua(x):
  giaithua = 1
  for i in range(x):
    giaithua = giaithua*(i+1)
  return giaithua
sinx = 0
cosx = 0
sinh = 0
cosh = 0
for i in range(n):
  sinx = sinx + ((-1)**(i))*x**(2*i+1)/giaithua(2*i+1)
  cosx = cosx + ((-1)**(i))*x**(2*i)/giaithua(2*i)
  sinh = sinh +(x**(2*i+1))/giaithua(2*i+1)
  cosh = cosh + (x**(2*i))/giaithua(2*i)
print('sinx=',sinx)
print('cosx=',cosx)
print('sinh=',sinh)
print('cosh=',cosh)