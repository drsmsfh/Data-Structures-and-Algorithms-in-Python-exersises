class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail=new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True
    def prepop(self,value):
        if self.length == 0:
            return None
        tmp = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
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
        tmp = self.get(index)
        if tmp:
            tmp.value = value
            return True
        return False
    def insert(self,index,value):
        if index > self.length:
            return False
        if index == 0:
            self.prepend(value)
        if index == self.length:
            self.append(value)
        new_node = Node(value)
        tmp = self.get(index-1)
        new_node.next = tmp.next
        tmp.next = new_node
        self.length +=1
        return True
    def remove(self,index):
        if index < self.length or index >= self.length:
            return False
        if index == 0:
            self.prepop()
        if index == self.length() -1:
            self.pop()
        pre = self.get(index-1)
        tmp = pre.next
        pre.next = tmp.next
        tmp.next = None
        self.length += 1
        return tmp
    def revers(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        befor = None
        for _ in range(self.length):
            after = temp.next
            temp.next = befor
            befor = temp
            temp = after
            
        
        
        
        
        
        
            

my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

# (2) Items - Returns 2 Node
print(my_linked_list.get(3).value)
# (1) Item -  Returns 1 Node



"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""