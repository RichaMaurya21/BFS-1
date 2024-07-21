# Problem 1
#Binary Tree Level Order Traversal (https://leetcode.com/problems/binary-tree-level-order-traversal/)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            val = []
            for i in range(len(q)):
                current = q.popleft()
                val.append(current.val) #To add all nodes at a level
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            res.append(val) 
        return res
       