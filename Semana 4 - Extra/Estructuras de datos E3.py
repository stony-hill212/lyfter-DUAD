class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def is_empty(self):
        return self.head is None
    
    def append(self,data):
        new_node=Node(data)
        if self.is_empty():
            self.head=self.tail=new_node
        else:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node
    
    def prepend(self,data):
        new_node=Node(data)
        if self.is_empty():
            self.head=self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node

    def delete(self,data):
        if self.is_empty():
            raise Exception("List is empty.")
        current=self.head
        while current:
            if current.data==data:
                if self.head==self.tail:
                    self.head=self.tail=None
                elif current==self.head:
                    self.head=current.next
                    self.head.prev=None
                elif current==self.tail:
                    self.tail=current.prev
                    self.tail.next=None
                else:
                    current.prev.next=current.next
                    current.next.prev=current.prev
                return
            current=current.next
        raise Exception("Value not found.")
    
    def print_forward(self):
        if self.is_empty():
            print("List is empty.")
            return
        current=self.head
        while current:
            if current.next:
                print(current.data, end=" -> ")
            else:
                print(current.data)
            current=current.next
    
    def print_backward(self):
        if self.is_empty():
            print("List is empty.")
            return
        current=self.tail
        while current:
            if current:
                print(current.data, end=" -> ")
            else:
                print(current.data)
            current=current.prev

dll=DoublyLinkedList()

dll.append("A")
dll.append("B")
dll.append("C")

dll.print_forward()
dll.print_backward()
dll.prepend("X")
dll.print_forward()
dll.print_backward()
dll.delete("B")
dll.print_forward()
dll.print_backward()
