class Node: 
    def __init__(self, val=0, left=None, right=None):
       self.left = left 
       self.right = right 
       self.val = val  

    def inOrder(self, root): 
        res = [] 
        def calc(root):
            if not root: 
                return 
            
            calc(root.left)
