import matplotlib.pyplot as plt

decision_node = dict(boxstyle="sawtooth", fc="0.8")
leaf_node = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

def PlotNode(node_txt, center_pt, parent_pt, node_type):
  CreatePlot.ax1.annotate(node_txt, xy=parent_pt, xycoords='axes fraction',
      xytext=center_pt, textcoords='axes fraction', 
      va="center", ha="center", bbox=node_type, arrowprops=arrow_args);

def CreatePlot():
  fig = plt.figure(1, facecolor='white');
  fig.clf();
  CreatePlot.ax1 = plt.subplot(111, frameon=False);
  PlotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decision_node);
  PlotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leaf_node);
  plt.show();

def GetNumLeafs(tree):
  num_leafs = 0
  first_str = tree.keys()[0]
  second_dict = tree[first_str]
  for key in second_dict.keys():
    # test to see if the nodes are dictonaires, if not they are leaf nodes
    if type(second_dict[key]).__name__=='dict':
      num_leafs += GetNumLeafs(second_dict[key]);
    else:
      num_leafs +=1
  return num_leafs;

def GetTreeDepth(tree):
  max_depth = 0
  first_str = tree.keys()[0]
  second_dict = tree[first_str]
  for key in second_dict.keys():
    if type(second_dict[key]).__name__=='dict':
      # test to see if the nodes are dictonaires, if not they are leaf nodes
      this_depth = 1 + GetTreeDepth(second_dict[key])
    else:
      this_depth = 1
    if this_depth > max_depth: max_depth = this_depth
  return max_depth

def RetrieveTree(i):
  tree_list =[{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
      {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}
    ]
  return tree_list[i]
