#exercise 1
tp=2
fp=4
fn=5
if not isinstance(tp,int):
  print('tp must be an integer')
  exit()
elif not isinstance(fp,int):
  print('fp must be an integer')
  exit()
elif not isinstance(fn,int):
  print('fn must be an integer')
  exit()
elif tp < 0:
  print('tp must be greater than zero')
  exit()
elif fp < 0:
  print('fp must be greater than zero')
  exit()
elif fn < 0:
  print('fn must be greater than zero')
  exit()
else:
  precision = tp/(tp+fp)
  recall = tp/(tp+fn)
  f1 = 2*precision*recall/(precision+recall)
  print('precision is',precision)
  print('recall is',recall)
  print('f1 is',f1)