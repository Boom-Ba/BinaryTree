def construct(postorder,inorder):
  if not postorder or not inorder:
    return None
  root_val=postorder.pop()
  root= Node(root_val,None,None)
  
  while postorder:
    for idx, value in enumerate(inorder):
      if value ==root_val:
        root.left = construct(postorder.copy(),inorder[:index])
        root.left = construct(postorder.copy(),inorder[index+1:])
        return root
    
