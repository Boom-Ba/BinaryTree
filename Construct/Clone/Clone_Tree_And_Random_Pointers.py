##clone a tree and its random pointer by using hashmap

from collections import deque
# A class to store a special binary tree node with a random pointer
class Node:
#     # Constructor
    def __init__(self, data, left=None, right=None, random=None):
        self.data = data
        self.left = left
        self.right = right
        self.random = random

def clone_ST(root,d):
  #pre-order clone Tree
  if not root:
    return d
  d[root]=Node(root.data)
  #clone left subtree and right subtree
  d[root].left= clone_ST(root.left,d)
  d[root].right=clone_ST(root.right,d)
  return d[root]

def clone_random(root,d ):
  if root not in d:
    return 
  #hashmap: {node.random -> copied node of its random node}
  d.get(root).radom =d.get(root.random)
  #create a point from copied root to copied_random_node_of_root
  clone_random(root.left,d)
  clone_random(root.right,d)

def clone_tree(root):
  d={}
  if not root:
    return None
  clone_ST(root,d)
  clone_random(root,d)
  return d


# def get_random_pointers(root):
#   #hashmap to store treeNode
#   d= {}
#   if not root:
#     return root
#   d[root]=None(root.data) 


def level_order_print(root):
  tree=[]

  q =deque()
  q.append(root)
  while q:
    curr_level =[]
    for _ in range(len(q)):
      node =q.popleft()
      curr_level.append(node.data)
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
    tree.append(curr_level)
  return tree


if __name__ == '__main__':
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    tree=level_order_print(root)
    # print(tree)
    """     
                1
              2   3
            4  5  6 7
    """

    ##create random pointers
    root.left.left.random=root.right
    root.left.right.random = root
    root.right.left.random = root.left.left
    root.random = root.left

    d=clone_tree(root)
    for k,v in d.items():
      print(k.data,v.data)

