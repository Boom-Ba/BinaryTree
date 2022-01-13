"""
construct Tree from pre-order and isLeaf
preorder = [1, 2, 4, 5, 3, 6, 8, 9, 7]      Root Left Right
isLeaf    =[0, 0, 1, 1, 0, 0, 1, 1, 1]
            1
        2      3      
      4   5   6  7
            8  9
            
"""
def construct(preorder, isLeaf, pIndex):
 
    # base case
    if pIndex == len(preorder):
        return None, pIndex
 
    # construct the current node, check if it is an internal node,
    # and increment `pIndex`
    node = Node(preorder[pIndex])
    isInternalNode = (isLeaf[pIndex] == 0)
    pIndex = pIndex + 1
 
    # if the current node is an internal node, construct its 2 children
    if isInternalNode:
        node.left, pIndex = construct(preorder, isLeaf, pIndex)
        node.right, pIndex = construct(preorder, isLeaf, pIndex)
 
    # return current node
    return node, pIndex
