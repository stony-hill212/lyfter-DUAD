class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def is_empty(self):
        return self.head is None
    
    def insert_front(self,data):
        new_node=Node(data)
        if self.is_empty():
            self.head=self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        
    def insert_back(self,data):
        new_node=Node(data)
        if self.is_empty():
            self.head=self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
    
    def delete(self,data):
        if self.is_empty():
            raise Exception("List is empty.")
        if self.head.data==data:
            self.head=self.head.next
            if self.head is None:
                self.tail=None
            return
        previous=self.head
        current=self.head.next
        while current:
            if current.data==data:
                previous.next=current.next
                if current==self.tail:
                    self.tail=previous
                return
            previous=current
            current=current.next
        raise Exception("Value not found in the list.")
    
    def print_all(self):
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

ll=LinkedList()
ll.insert_front(10)
ll.insert_front(20)
ll.print_all()
ll.insert_back(30)
ll.print_all()
ll.delete(10)
ll.print_all()