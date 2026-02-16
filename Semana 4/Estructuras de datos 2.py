class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class Deque:
    def __init__(self):
        self.head=None
        self.tail=None

    def is_empty(self):
        return self.head is None
    
    def push_left(self,value):
        new_node=Node(value)
        if self.is_empty():
            self.head=self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    
    def push_right(self,value):
        new_node=Node(value)
        if self.is_empty():
            self.head=self.tail=new_node
        else:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node
    
    def print_queue(self):
        if self.is_empty():
            print("Deque is empty")
            return
        current=self.head
        print("None <-", end="")
        while current:
            print(current.data,end=" <-> ")
            current=current.next
        print("None")

dq=Deque()
dq.push_left(10)
dq.push_left(5)
dq.push_right(20)
dq.push_right(30)

dq.print_queue()
