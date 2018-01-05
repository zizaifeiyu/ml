import numpy as np
#from numpy import *

def LoadDataSet():
  posting_list=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
    ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
    ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
    ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
    ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
    ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
  class_vec = [0,1,0,1,0,1]    #1 is abusive, 0 not
  return posting_list,class_vec

def CreateVocabList(data_set):
  vocab_set = set([])
  for doc in data_set:
    vocab_set = vocab_set | set(doc)
  return list(vocab_set)

def SetOfWords2Vec(vocab_list, input_set):
  res_vec = [0]*len(vocab_list)
  for word in input_set:
    if word in vocab_list:
      res_vec[vocab_list.index(word)] = 1
    else: print "the word: %s is not in my Vocabulary!" % word

  return res_vec

def SetOfWords2VecN(vocab_list, input_set):
  res_vec = [0]*len(vocab_list)
  for word in input_set:
    if word in vocab_list:
      res_vec[vocab_list.index(word)] += 1
    else: print "the word: %s is not in my Vocabulary!" % word

  return res_vec

# tm: train matrix
# tc: train category
def TrainNB0(tm, tc):
  doc_num = len(tm)
  word_num = len(tm[0])
  p_abusive = sum(tc)/float(doc_num)
  p0_num = np.ones(word_num)
  p1_num = np.ones(word_num)
  p0_denom = 2.0
  p1_denom = 2.0

  for i in range(doc_num):
    if tc[i] == 1:
      p1_num += tm[i]
      p1_denom += sum(tm[i])
    else:
      p0_num += tm[i]
      p0_denom += sum(tm[i])

    p1_vec = np.log(p1_num/p1_denom)   
    p0_vec = np.log(p0_num/p0_denom)   
  return p0_vec, p1_vec, p_abusive

def ClassifyNB(vec2classify, p0_vec, p1_vec, p_class1):
  p1 = sum(vec2classify * p1_vec) + log(p_class1)
  p0 = sum(vec2classify * p0_vec) + log(1.0 - p_class1)
  if p1 > p0:
    return 1
  else:
    return 0

def TestingNB():
  listOPosts,listClasses = LoadDataSet()
  myVocabList = CreateVocabList(listOPosts)
  trainMat=[]
  for postinDoc in listOPosts:
    trainMat.append(SetOfWords2Vec(myVocabList, postinDoc))

  p0V,p1V,pAb = TrainNB0(array(trainMat),array(listClasses))
  testEntry = ['love', 'my', 'dalmation']
  thisDoc = array(SetOfWords2Vec(myVocabList, testEntry))
  print testEntry,'classified as: ',ClassifyNB(thisDoc,p0V,p1V,pAb)
  testEntry = ['stupid', 'garbage']
  thisDoc = array(SetOfWords2Vec(myVocabList, testEntry))
  print testEntry,'classified as: ',ClassifyNB(thisDoc,p0V,p1V,pAb)


