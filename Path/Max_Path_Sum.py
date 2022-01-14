# construct max sum path between 2 nodes 
import sys

# A class to store a binary tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def MaxSumPath(root,maxRes):
  if not root:
    return 0, maxRes
  #recursively get left return value, and maxSum value
  left, maxRes =  MaxSumPath(root.left, maxRes)
  right, maxRes = MaxSumPath(root.right, maxRes)

  maxRes= max(maxRes, root.data)
  maxRes =max(maxRes, root.data+left)
  maxRes =max(maxRes, root.data+right)
  maxRes =max(maxRes, root.data+left+right)

  return max(root.data, root.data+max(left,right)),maxRes
 
if __name__ == '__main__':
 
    root = None
 
    ''' Construct the following tree
            1
          /   \
         /     \
        2      10
       / \    /  \
     -1  -4  -5   -6
         /   / \
        3   7   4
             \
             -2
    '''
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(-1)
    root.left.right = Node(-4)
    root.right.left = Node(-5)
    root.right.right = Node(-6)
    root.left.right.left = Node(4)
    root.right.left.left = Node(7)
    root.right.left.right = Node(4)
    root.right.left.left.right = Node(-2)

    maxSum =-sys.maxsize
    local_max,global_max=MaxSumPath(root,maxSum)
    print(global_max if global_max>0 else 0 )
