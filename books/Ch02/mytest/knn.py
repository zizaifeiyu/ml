import numpy as np
#from numpy import *
import operator

def CreateDataSet() :
  group = np.array([[1.0, 1.1], [1.0, 1.0], [0,0],[0,0.1]])
  labels = ['A', 'A', 'B', 'B']
  return group, labels

def Classify0(in_x, data_set, labels, k) :
  data_set_size = data_set.shape[0]
  diff_mat = np.tile(in_x, (data_set_size,1)) - data_set
  sq_diff_mat = diff_mat ** 2
  sq_distance = sq_diff_mat.sum(axis=1)
  distances = sq_distance**0.5
  sorted_distance_indicies = distances.argsort()
  class_cnt = {}
  for i in range(k):
    vote_i_lable = labels[sorted_distance_indicies[i]]
    class_cnt[vote_i_lable] = class_cnt.get(vote_i_lable,0) + 1

  sorted_class_cnt = sorted(class_cnt.iteritems(),key=operator.itemgetter(1), reverse=True)

  return sorted_class_cnt[0][0]

def File2Matrix(file):
  f = open(file)
  lines=f.readlines()
  l_num = len(lines)
  mat = np.zeros((l_num, 3)) # obj's features
  l_vec = [] # labels
  idx = 0
  for line in lines:
    line = line.strip()
    l_list = line.split('\t')
    mat[idx,:] = l_list[0:3]
    l_vec.append(int(l_list[-1]))
    idx +=1

  return mat, l_vec

# File2Matrix("/Users/guanxiao.wd/per/python/ml/books/ch02/datingTestSet2.txt")
 
def AutoNorm(data_set):
  min_vals = data_set.min(0)
  max_vals = data_set.max(0)
  sacles = max_vals - min_vals
  m = data_set.shape[0]
  norm_data_set = data_set - np.tile(min_vals, (m, 1))
  norm_data_set = norm_data_set/np.tile(sacles, (m , 1))

  return norm_data_set, sacles, min_vals

def DatingClassTest():
  ratio = 0.1
  g, l = File2Matrix('../datingTestSet2.txt')
  ng, rg, mv = AutoNorm(g)
  m = ng.shape[0]
  test_num = int(m*ratio)
  err_num = 0

  for i in range(test_num):
    classify_res = Classify0(ng[i,:], ng[test_num:m, :], l, 7)
    print "classify res:%d, real res:%d" % (classify_res, l[i])
    if (classify_res != l[i]) : err_num += 1

  print "tot err num:%d, err rate:%f%%" % (err_num, 100*err_num/float(test_num))

DatingClassTest()


