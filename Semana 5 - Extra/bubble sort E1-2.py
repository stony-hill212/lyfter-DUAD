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
    
    def pop_left(self):
        if self.is_empty():
            raise Exception("Deque is empty.")
        removed_node=self.head
        if self.head==self.tail:
            self.head=self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None
        return removed_node.data
    
    def pop_right(self):
        if self.is_empty():
            raise Exception("Deque is empty.")
        removed_node=self.tail
        if self.head==self.tail:
            self.head=self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
        return removed_node.data
    
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
    
    def bubble_sort(self):
        if self.is_empty() or self.head.next is None:
            return
        end=None
        swapped=None
        while swapped:
            swapped=True
            current=self.head
            while current.next!=end:
                if current.data>current.next.data:
                    current.data,current.next.data=current.next.data,current.data
                    swapped=True
                current=current.next
            end=current

dq=Deque()
dq.push_right(4)
dq.push_right(1)
dq.push_right(3)
dq.push_right(2)
dq.print_queue()
dq.bubble_sort()

dq.print_queue()

