class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None
    
    def insert(self,value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert_recursive(self.root,value)
    
    def _insert_recursive(self,current,value):
        if value<current.data:
            if current.left is None:
                current.left=Node(value)
            else:
                self._insert_recursive(current.left,value)
        else:
            if current.right is None:
                current.right=Node(value)
            else:
                self._insert_recursive(current.right,value)
    
    def print_tree(self):
        if self.root is None:
            print("Tree is empty")
        else:
            self._print_recursive(self.root,0)
    
    def _print_recursive(self,node,level):
        if node is not None:
            self._print_recursive(node.right,level+1)
            print("  "*level+str(node.data))
            self._print_recursive(node.left,level+1)

tree=BinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)
tree.print_tree()