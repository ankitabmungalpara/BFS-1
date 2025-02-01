"""

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

Time Complexity: O(N) since each node is processed once.
Space Complexity: O(N) in the worst case, where all nodes at the last level are stored in the queue.

Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

"""

# Approach: 
# Performed a level-order traversal using a queue, processing nodes level by level. 
# Enqueue the root node first, then iteratively dequeue a node, record its value, and enqueue its children. 
# Continue until the queue is empty, storing each level's values in a list.


from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        q = Queue()
        q.put(root)

        res = []

        while not q.empty():
            level = q.qsize()
            temp = []
            for i in range(level):
                node = q.get()
                if node:
                    temp.append(node.val)
                    q.put(node.left)
                    q.put(node.right)
            if temp:
                res.append(temp)

        return res

