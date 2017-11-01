import numpy as np

fmeta = "/root/pro/py/ml/data/cifar-10-batches-py/batches.meta"
f1 = "/root/pro/py/ml/data/cifar-10-batches-py/data_batch_1"

def unpickle(file):
  import cPickle
  with open(file, 'rb') as fo:
    dict = cPickle.load(fo)
  return dict

def sigmoid(z):
   s = 1 / (1 + exp(-z)) 
   return s

def initialize_with_zeros(dim):
  w = np.zeros(dim, 1)
  b = 0
  return w, b

def propagate(w, b, X, Y):
  m = X.shape[1] # 样本个数
  Y_hat = sigmoid(np.dot(w.T, X) + b)
  cost = -(np.sum(np.dot(Y, np.log(Y_hat).T) +
        np.dot((1-Y), np.log(1 - Y_hat).T))) / m

  dw = (np.dot(X, (Y_hat - Y).T)) / m
  db = (np.sum(Y_hat - Y)) / m
  cost = np.squeeze(cost) # 压缩维度
  grads = {"dw": dw, "db": db}

  return grads, cost

def optimize(w, b, X, Y, num_iter, lrate, print_cost = False):
  # num_iter 梯度下降次数
  costs = []
  for i in range(num_iter):
    grads, cost = propagate(w, b, X, Y)
    dw = grads["dw"]
    db = grads["db"]

    w = w - lrate * dw
    b = b - lrate * dd

    if i % 100 == 0:
      costs.append(cost)

    if print_cost and i % 100 == 0:
      print ("循环%i次后的成本值：%f" %(i, cost))

  params = {"w": w, "b": b}
  grads = {"dw": dw, "db": db}

  return params, grads, costs

def predict(w, b, X):
  m = X.shape[1] # 样本个数
  Y_prediction = np.zeros(1, m) # 初始化预测输出
  w = w.reshape(X.shape[0], 1) # 转置参数向量w

  Y_hat = sigmoid(np.dot(w.T, X) + b)

  for i in range(Y_hat.shape[1]):
    if Y_hat[:, i] > 0.5:
      Y_prediction[:, i] = 1
    else:
      Y_prediction[:, i] = 0

  return Y_prediction
      

def model(X_train, Y_train, X_test, Y_test,
    num_iter = 2000, lrate = 0.5, print_cost = False):
  w, b = initialize_with_zeros(X_train.shape[0])

  params, grads, costs = optimize(w, b, X_train,
      Y_train, num_iter, lrate, print_cost)

  w = params["w"]
  b = params["b"]

  Y_pre_train = predict(w, b, X_train)
  Y_pre_test = predict(w, b, X_test)

  train_accuracy = 100 -
    np.mean(np.abs(Y_pre_train - Y_train)) * 100
    
  test_accuracy = 100 - 
    np.mean(np.abs(Y_pre_test - Y_test)) *100


  print("训练集识别精度: {}%".format(train_accuracy)) 
  print("测试集识别精度: {}%".format(test_accuracy))

  d = {
    "costs": costs,
    "Y_pre_test": Y_pre_test,
    "Y_pre_train": Y_pre_train,
    "w": w,
    "b": b,
    "learning_rate": lrate,
    "num_iter": num_iter}

  return d



dmeta = unpickle(fmeta)
d1 = unpickle(f1)

print(type(dmeta))
print(type(d1))

for (k, v) in dmeta.items():
  print "key:" + k + ", val:" + str(v)

print("d1 begin:")
for el in d1:
  print el

print("d1 end.")

for (k, v) in d1.items():
  print "key:" + k + ", val:" + str(v)


#i = 0
#for (k, v) in d1.items():
#  ++i
#  if ( i > 10):
#     break
#  print "key:" + k + ", val:" + str(v)
 

