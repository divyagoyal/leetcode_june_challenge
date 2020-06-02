class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if (root == None): 
            return
  
        q = [] 
        q.append(root) 

        while (len(q)): 
            curr = q[0] 
            q.pop(0) 

            curr.left, curr.right = curr.right, curr.left 

            if (curr.left): 
                q.append(curr.left) 
            if (curr.right): 
                q.append(curr.right) 
        
        return root
