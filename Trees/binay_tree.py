class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root=new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left=new_node;
                    return True
                else:
                    temp=temp.left
                    continue;
            elif temp.right == None:
                temp.right=new_node;
                return True
            else:
                temp=temp.right
   
    def contains(self,value):
        if self.root == None:
            return False
        else:
            temp = self.root
            while (temp):
                if temp.value == value:
                    return True
                elif temp.value > value:
                    temp=temp.left
                else:
                    temp=temp.right
                    
            return False  
                
    def min_value(self):
        if self.root == None:
            return False
        else:
            temp = self.root
            while temp.left != None:
                temp = temp.left
                
            return temp.value
    def display_inorder(self,root):
        if root == None:
            return;
        self.display_inorder(root.left)
        print(root.value)
        self.display_inorder(root.right)
    
    def display_preorder(self,root):
        if root == None:
            return;
        
        print(root.value)
        self.display_preorder(root.left)
        self.display_preorder(root.right)
        
    def display_postorder(self,root):
        if root == None:
            return;
        
        self.display_postorder(root.left)
        self.display_postorder(root.right)
        print(root.value)
                
                
                
        
my_Tree = BinarySearchTree()
print(my_Tree.insert(2))
print(my_Tree.insert(1))
print(my_Tree.insert(3))
print(my_Tree.insert(9))
print(my_Tree.insert(10))

# print(my_Tree.insert(3))
# print(my_Tree.insert(9))
# print(my_Tree.root.value)
# print(my_Tree.root.left.value)
# print(my_Tree.root.right.value)

print(my_Tree.contains(9))
# print(my_Tree.contains(6))


print("InOrder Display  : ")
my_Tree.display_inorder(my_Tree.root)
print("")
print("preOrder Display  : ")
my_Tree.display_preorder(my_Tree.root)
print("")
print("postOrder Display  : ")
my_Tree.display_postorder(my_Tree.root)



