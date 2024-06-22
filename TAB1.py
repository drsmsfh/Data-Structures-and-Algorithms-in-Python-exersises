class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self,value):
        new_Node = Node(value)
        self.head = new_Node
        self.tail = new_Node
        self.length = 1
    def print_list(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.value)
            tmp =tmp.next
    def append(self,value):    
        new_Node = Node(value)
        if self.length == 0:
            self.head = new_Node
            self.tail = new_Node
        else:
            self.tail.next =new_Node
            self.tail = new_Node
        self.length += 1
    def prepend(self,value):
        new_Node = Node(value)
        if self.length == 0:
            self.head = new_Node
            self.tail = new_Node
        else:
            new_Node.next = self.head
            self.head= new_Node
        self.length +=1
        return True
    def pop(self):
        if self.length == 0:
            return None
        tmp = self.head
        pre = self.head
        while tmp.next:
            pre = tmp
            tmp =tmp.next
        self.head = pre
        pre.next = None
        self.length -= 1
        if self.length == 0:
            self.head =None
            self.tail = None
        return tmp
    def pop_first(self):
        if self.length == 0 :
            return None
        tmp = self.head
        self.head = self.head.next
        tmp.next = None
        self.length -=1
        if self.length == 0:
            self.head =None
            self.tail = None
        return tmp
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        tmp = self.head
        for _ in range(index):
            tmp = tmp.next
        return tmp
    def set_value(self,index,value):
        new_Node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        new_Node = Node(value)
        pre = self.get(index-1)
        new_Node.next = pre.next
        pre.next = new_Node
        
    



my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

print('LL before set_value():')
my_linked_list.print_list()

my_linked_list.set_value(1,4)

print('\nLL after set_value():')
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    LL before set_value():
    11
    3
    23
    7

    LL after set_value():
    11
    4
    23
    7
"""
            