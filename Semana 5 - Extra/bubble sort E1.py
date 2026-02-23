class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
    
    def is_empty(self):
        return self.top is None
    
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        removed=self.top
        self.top=self.top.next
        return removed.data
    
    def print_stack(self):
        current=self.top
        while current:
            if current.next:
                print(current.data, end=" -> ")
            else:
                print(current.data)
            current=current.next
    
    def bubble_sort(self):
        if self.is_empty() or self.top.next is None:
            return
        swapped=True
        while swapped:
            swapped=False
            current=self.top
            while current.next:
                if current.data>current.next.data:
                    current.data,current.next.data=current.next.data,current.data
                    swapped=True
                current=current.next

s=Stack()
s.push(3)
s.push(1)
s.push(4)
s.push(2)
s.print_stack()
s.bubble_sort()
s.print_stack()
