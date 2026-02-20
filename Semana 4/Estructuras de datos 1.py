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
        removed_node=self.top
        self.top=self.top.next
        return removed_node.data
    
    def print_stack(self):
        if self.is_empty():
            print("The stack is empty.")
            return
        current=self.top
        print("Top ->", end="")
        while current:
            print(current.data,end=" -> ")
            current=current.next
        print("None")

stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.print_stack()
print("Popped:", stack.pop())
stack.print_stack()