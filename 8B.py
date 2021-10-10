class node:
  def __init__(self, name):
    self.childs = []
    self.name = name
nodes={}
answer=[]
def define_relative(steck, parent, child):
    if child not in steck:
      steck.extend(nodes[parent].childs)
      if len(steck)==0:
        return False
      parent = steck.pop()
      if define_relative(nodes, parent, child):
        return True
    else:
      return True
def define_both(nodes, parent, child):
    y1 = define_relative(nodes, child, parent)
    y2=define_relative(nodes, parent,child)
    #print(y1,y2)
    if y1==True and y2 ==False:
        return 1
    elif y2==True and y1==False:
        return 2
    else:
      return 0
with open('input.txt') as f:
  k = int(f.readline())
  sch = 0
  for line in f:
    
    if sch<k-1:
      ch, parent = map(str, line.split())
      if parent not in nodes:
        nodes[parent] = node(parent)
      nodes[parent].childs.append(ch)
      nodes[ch]=node(ch)
    else:
      
      ch, parent = map(str, line.split())
      answer.append(define_both([], parent, ch))
    sch+=1
print(" ".join(map(str,answer)))
