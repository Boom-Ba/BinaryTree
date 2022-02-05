def helper(root,path,res):
  if not root:
    return 
  #backtrack
  path.append(root.val)
  if not root.left and not root.right:
    res.append(path[:])
  helper(root.left,path,res)
  helper(root.right,path,res)
  path.pop()

def printPath(root):
  res=[]
  if not root:
    return res
  helper(root,[],res)
  return res
