# problem is given inorder and postorder traversal sequence
# and generate pre-order sequence

#algorithm is to definie the range for LST and RST from in-order traversal
#and do POST-ORDER traverlsal (Right)-(Left)-(Root)
def find_preorder(post, post_index, in_o, start, end, curr):
  if start>end:
    return post_index

  if start<=end:
    root =post[post_index]
    index= in_o.index(root)
    post_index-=1 #root of subtree is the last item in the range
    
    post_index= find_preorder(post,post_index,in_o, index+1, end,curr)
    post_index= find_preorder(post,post_index,in_o, start, index-1,curr)
    
    #append the root val last, so the current array stores the reversed sequence of pre-order
    curr.append(root) 
    print(curr) 
    return post_index
 
if __name__ == '__main__':
 
    ''' Construct the following tree
               1
             /   \
            /     \
           2       3
          /       / \
         /       /   \
        4       5     6
               / \
              /   \
             7     8

recursion 
[6]
[6, 8]
[6, 8, 7]
[6, 8, 7, 5]
[6, 8, 7, 5, 3]
[6, 8, 7, 5, 3, 4]
[6, 8, 7, 5, 3, 4, 2]
[6, 8, 7, 5, 3, 4, 2, 1]
'''
 
    inorder = [4, 2, 1, 7, 5, 8, 3, 6]
    postorder = [4, 2, 7, 8, 5, 6, 3, 1]
    curr=[]
    post_index=len(postorder)-1
    find_preorder(postorder,post_index ,inorder, 0, len(inorder)-1, curr)
    print(curr[::-1])
