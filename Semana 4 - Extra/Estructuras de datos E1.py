class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def is_empty(self):
        return self.head is None
    
    def enqueue(self,data):
        new_node=Node(data)
        if self.is_empty():
            self.head=self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty.")
        removed_node=self.head
        self.head=self.head.next
        if self.head is None:
            self.tail=None
        return removed_node.data
    
    def print_all(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        current=self.head
        while current:
            if current.next:
                print(current.data, end=" -> ")
            else:
                print(current.data)
            current=current.next

q=Queue()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

q.print_all()
print(q.dequeue())
q.print_all()