a= [5,7,1,15,9,2,14,8,7]
#constructing - in order 

class Node:
  def __init__(self,val =None):
    self.left=None
    self.right=None
    self.val =val 
class BST:
  def __init__(self):
    self.root=None
  
  def insert(self,value):
    ##check if root has value
    if self.root==None:
      self.root= Node(value)
    else:
      self._insert(value,self.root)
  def _insert(self,value,curr):
    #val<curr
    if value<curr.val:
      #if curr doesn't have left child
      if curr.left ==None:
        #create new node 
        curr.left=Node(value)
      #if has left_child, call recursion to insert_ the left of node
      else:
        self._insert(value,curr.left)
    elif value>curr.val:
      if curr.right==None:
        curr.right=Node(value)
      #if has left_child, call recursion to insert_ the left of node
      else:
        self._insert(value,curr.right)
    else:
      print('duplicates')

  def printT(self):
    if self.root!=None:
       self._printT(self.root)
    
  def _printT(self, node):
    if node !=None:
      self._printT(node.left)
      print(node.val)
      self._printT(node.right)
  
  def height(self):
    if self.root!=None:
      return self._height(self.root)
  
  def _height(self,node):
    if not node:
      return 0
    left_height =self._height(node.left)
    right_height=self._height(node.right)
    return max(left_height,right_height) +1
  def search(self,val):
    if self.root !=None:
      return self._search(val,self.root)
    return False
  def _search(self,value,curr_node):
    if curr_node.val==value:
      return True
    if value<curr_node.val and curr_node.left:
      self._search(value,curr_node.left)
    elif value>curr_node.val and curr_node.right:
      self._search(value,curr_node.right)
    else:
      return False
bst=BST()
for i in a:
  bst.insert(i)
# bst.printT()
# bst.height()
bst.search(5)
