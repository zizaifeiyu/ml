from math import log
import operator

def CreateDataSet():
  dataSet = [[1, 1, 'yes'],
    [1, 1, 'yes'],
    [1, 0, 'no'],
    [0, 1, 'no'],
    [0, 1, 'no']]
  labels = ['no surfacing','flippers']
#change to discrete values
  return dataSet, labels

def CreateDataSet2():
  dataSet = [[1, 1, 'yes'],
    [1, 1, 'yes'],
    [1, 0, 'no'],
    [0, 1, 'no'],
    [0, 1, 'no']]
  labels = ['has house','xxx']
#change to discrete values
  return dataSet, labels

def CalcShannonEnt(data_set):
  num = len(data_set)
  labels = {}
  for feat_vec in data_set:
    cur_label = feat_vec[-1]
    if cur_label not in labels.keys():
      labels[cur_label] = 0
    labels[cur_label] += 1

  shannonEnt = 0.0
  for key in labels:
    prob = float(labels[key])/num
    shannonEnt -= prob * log(prob, 2)
  return shannonEnt
      
def SplitDataSet(data_set, axis, value):
  res_data_set = []
  for feat_vec in data_set:
    if feat_vec[axis] == value:
      reduced_feat_vec = feat_vec[:axis]
      reduced_feat_vec.extend(feat_vec[axis+1:])
      res_data_set.append(reduced_feat_vec)

  return res_data_set

def ChooseBestFeatureToSplit(data_set):
  f_num = len(data_set[0]) - 1
  base_entropy = CalcShannonEnt(data_set)
  best_info_gain = 0.0
  best_feature = -1
  for i in range(f_num):
    feat_list = [example[i] for example in data_set]
    unique_vals = set(feat_list)
    new_entropy = 0.0
    for val in unique_vals:
      sub_data_set = SplitDataSet(data_set, i, val)
      prob = len(sub_data_set)/float(len(data_set))
      new_entropy += prob * CalcShannonEnt(sub_data_set)
    info_gain = base_entropy - new_entropy
    if (info_gain > best_info_gain):
      best_info_gain = info_gain
      best_feature = i

  return best_feature

def MajorityCnt(class_list):
  class_cnt = {}
  for vote in class_list:
    if vote not in class_cnt.keys(): class_cnt[vote] = 0;
    class_cnt[vote] += 1;
  sorted_class_cnt = sorted(class_cnt.iteritems(), key=operator.itemgetter(1), reverse=True)
  return sorted_class_cnt[0][0]

def CreateTree(data_set, labels):
  class_list = [example[-1] for example in data_set]
  if class_list.count(class_list[0]) == len(class_list):
    return class_list[0];
  if len(data_set[0]) == 1:
    return MajorityCnt(class_list)
  best_feat = ChooseBestFeatureToSplit(data_set)
  best_feat_label = labels[best_feat]
  my_tree = {best_feat_label:{}}
  del(labels[best_feat])
  feat_val = [example[best_feat] for example in data_set]
  unique_vals = set(feat_val)
  for val in unique_vals:
    sub_labels = labels[:]
    my_tree[best_feat_label][val] = CreateTree(SplitDataSet(data_set, best_feat, val), sub_labels)

  return my_tree




