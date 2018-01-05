import matplotlib.pyplot as plt

decision_node = dict(boxstyle="sawtooth", fc="0.8")
leaf_node = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

def PlotNode(node_txt, center_pt, parent_pt, node_type):
  CreatePlot.ax1.annotate(node_txt, xy=parent_pt, xycoords='axes fraction',
      xytext=center_pt, textcoords='axes fraction', 
      va="center", ha="center", bbox=node_type, arrowprops=arrow_args);

#
#def CreatePlot():
#  fig = plt.figure(1, facecolor='white');
#  fig.clf();
#  CreatePlot.ax1 = plt.subplot(111, frameon=False);
#  PlotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decision_node);
#  PlotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leaf_node);
#  plt.show();

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

def PlotMidText(cntr_pt, parent_pt, txt_str):
  x_mid = (parent_pt[0]-cntr_pt[0])/2.0 + cntr_pt[0]
  y_mid = (parent_pt[1]-cntr_pt[1])/2.0 + cntr_pt[1]
  CreatePlot.ax1.text(x_mid, y_mid, txt_str, va="center", ha="center", rotation=30)

def PlotTree(tree, parent_pt, node_txt):#if the first key tells you what feat was split on
    leaf_num = getNumLeafs(tree)  #this determines the x width of this tree
    depth = GetTreeDepth(tree)
    first_str = tree.keys()[0]     #the text label for this node should be this
    cntr_pt = (plotTree.xOff + (1.0 + float(leaf_num))/2.0/plotTree.totalW, plotTree.yOff)
    plotMidText(cntr_pt, parent_pt, node_txt)
    plotNode(first_str, cntr_pt, parent_pt, decisionNode)
    secondDict = tree[first_str]
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':#test to see if the nodes are dictonaires, if not they are leaf nodes   
            plotTree(secondDict[key],cntr_pt,str(key))        #recursion
        else:   #it's a leaf node print the leaf node
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntr_pt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntr_pt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD
#if you do get a dictonary you know it's a tree, and the first element will be another dict

def CreatePlot(tree):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    CreatePlot.ax1 = plt.subplot(111, frameon=False, **axprops)    #no ticks
    #createPlot.ax1 = plt.subplot(111, frameon=False) #ticks for demo puropses 
    PlotTree.totalW = float(getNumLeafs(tree))
    PlotTree.totalD = float(GetTreeDepth(tree))
    PlotTree.xOff = -0.5/PlotTree.totalW; PlotTree.yOff = 1.0;
    PlotTree(tree, (0.5,1.0), '')
    plt.show()
