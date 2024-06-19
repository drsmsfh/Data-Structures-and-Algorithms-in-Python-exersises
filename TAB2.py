class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self,data):
        newNode = Node(data)
        self.head = newNode
        self.tail = newNode
        self.length = 1
        def append(self,data):
            newNode = Node(data)
            if self.head == None:
                self.head = data
                self.tail = data
                self.length = 1
            else:
                self.tail.next = newNode
                self.tail = newNode
            self.length += 1
                
            
            
        



 
my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.data)
print('Tail:', my_linked_list.tail.data)
print('Length:', my_linked_list.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

                                                                                                                    