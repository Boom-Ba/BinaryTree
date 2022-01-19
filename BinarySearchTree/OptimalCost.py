"""
       25  - level1 w/cost= 25*level =25
  10      -  level2 w/cost= 10*2 =20 
      30  -  level3 w/cost = 30*3=90 
 total cost = sum() 
Find minimal cost arrangement. 
"""

def findOptimalCost(self, freq: List[int]) -> int:
	#[25, 10, 20]
	def findOptimalCost(freq, i, j, level,lookup):
	    # base case
	    if j < i:
	        return 0
        
		key =(i,j,level)
		if key in lookup:
			return lookup[key]
    
    optimalCost = sys.maxsize

    # consider each key as a root and recursively find an optimal solution
    for k in range(i, j + 1):

        leftOptimalCost = findOptimalCost(freq, i, k - 1, level + 1,lookup)

        rightOptimalCost = findOptimalCost(freq, k + 1, j, level + 1,lookup)

        # current node's cost is `freq[k]×level`

       # update the optimal cost
        optimalCost = min(optimalCost, freq[k] * level + leftOptimalCost
                                  + rightOptimalCost)
      lookup[key] =optimalCost
	    # Return minimum value
	    return lookup[key]
	if not freq:
		return 0
	lookup={}
	return findOptimalCost(freq,0,len(freq)-1, 1,lookup )

