def findMaxSumPath(root,max_sum=float('-inf')):
	if root is None:
	return 0, max_sum

    # find the maximum sum node-to-leaf path starting from the left child
    left, max_sum = findMaxSumPath(root.left, max_sum)

    # find the maximum sum node-to-leaf path starting from the right child
    right, max_sum = findMaxSumPath(root.right, max_sum)

    # it is important to return the maximum sum node-to-leaf path starting from the
    # current node

    # case 1: left child is None
    if root.left is None:
	return (right + root.data), max_sum

    # case 2: right child is None
    if root.right is None:
	return (left + root.data), max_sum

    # find the maximum sum path "through" the current node
    cur_sum = left + right + root.data



max_sum = max(cur_sum, max_sum)

    # case 3: both left and right child exists
    return (max(left, right) + root.data), max_sum
