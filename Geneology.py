'''
В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.
Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой. 
У родоначальника высота равна 0, у любого другого элемента высота на 1 больше, чем у его родителя.
Даны два элемента в дереве. Определите, является ли один из них потомком другого.
Программа получает на вход число элементов в генеалогическом древе N. Далее следует N−1 строка, 
задающие родителя для каждого элемента древа, кроме родоначальника. 
Каждая строка имеет вид имя_потомка имя_родителя.
Далее до конца файла идут строки, содержащие имена двух элементов дерева.
Для каждого такого запроса выведите одно из трех чисел: 1, 
если первый элемент является предком второго, 2, 
если второй является предком первого или 0, 
если ни один из них не является предком другого. 
'''


def is_child(node, expected_child):
    if node == expected_child: return True
    for child in nodes[node]:
      if is_child(child, expected_child):
        return True
    return False

def is_parent(node, expected_parent):
    while node is not None: 
      if node == expected_parent: return True
      node = parents.get(node, None)
    return False

def decision_from_parent(file_name='input.txt'):
  parents={}
  answer=[]
  with open(file_name) as f:
    k = int(f.readline())
    for _ in range(k):
      line = f.readline()
      ch, parent = map(str, line.split())
      parents[ch] = parent
    for line in f:
      ch, parent = map(str, line.split())
      y1 = is_parent(ch, parent)
      y2=is_parent(parent,ch)
      ans = 2 if y1 else 0
      ans = 1 if y2 else 0
      answer.append(define_both(parent, ch))
    print(" ".join(map(str,answer)))
def decision_from_child(file_name='input.txt'):
  nodes={}
  answer=[]
  with open(file_name) as f:
    k = int(f.readline())
    for _ in range(k):
      line = f.readline()
      ch, parent = map(str, line.split())
      if parent is not nodes:
        nodes[parent]=[]
      nodes[parent].append(ch)
      nodes[ch]=[]
    for line in f:
      ch, parent = map(str, line.split())
      y1 = is_child(ch, parent)
      y2=is_child(parent,ch)
      ans = 2 if y1 else 0
      ans = 1 if y2 else 0
      answer.append(define_both(parent, ch))
    print(" ".join(map(str,answer)))
    
decision_from_parent('input.txt')
