class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
        
        

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        tmp = self.root
        while True :
            if tmp.value == new_node.value:
                return False
            if tmp.value > new_node.value:
                if tmp.left == None:
                    tmp.left = new_node
                    return True
                tmp = tmp.left
            else :
                if tmp.right == None:
                    tmp.right = new_node
                    return True
                tmp = tmp.right
                
    def contains(self,value):
        if self.root == None:
            return False
        tmp = self.root
        while tmp is not None :
            if tmp.value < value:
                tmp = tmp.right
            elif tmp.value > value:
                tmp = tmp.left
            else:
                return True
        return False
    
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
                
            if current_node.right is not None:
                queue.append(current_node.right)
                
        return results
    
    def dfs_pre_order(self):
        results = []
        def treverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                treverse(current_node.left)
            if current_node.right is not None:
                treverse(current_node.right)
        
        treverse(self.root)
        return results
    
    def dfs_post_order(self):
        results = []
        def treverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                treverse(current_node.left)
            if current_node.right is not None:
                treverse(current_node.right)
        
        treverse(self.root)
        return results
    
    def dfs_in_order(self):
        results = []
        def treverse(current_node):
            if current_node.left is not None:
                treverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                treverse(current_node.right) 
        treverse(self.root)
        return results
        
    

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.dfs_in_order())



"""
    EXPECTED OUTPUT:
    ----------------
    [18, 21, 27, 47, 52, 76, 82]

 """

   