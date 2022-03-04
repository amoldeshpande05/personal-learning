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
    
    
    def depth_first_search(self,root):
        # stack = [root]
        # while len(stack) > 0:
        #     current_node = stack.pop()
        #     print(current_node.value)
        #     if current_node.right:
        #         stack.append(current_node.right)
        #     if current_node.left:
        #         stack.append(current_node.left)
        # Recurssion Flow
        if root == None:
            return []
        
        left = self.depth_first_search(root.left)
        right = self.depth_first_search(root.right)
        return [root.value, *left,*right]
    
    def breadth_first_search(self,root):
        queue=[root]
        while len(queue)!=0:
            curr_node = queue.pop(0)
            print(curr_node.value)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
                
    def search_element_bfs(self,root,target):
        queue=[root]
        while len(queue)>0:
            curr_node = queue.pop(0)
            if curr_node.val == target:
                return True
            print(curr_node.value)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        return False
    
    def search_element_dfs(self,root,target):
        if root == None:
            return False
        return self.search_element_dfs(root.left,target) or self.search_element_dfs(root.right,target) or root.value == target
    
    
    def tree_sum(self,root):
        if root == None:
            return 0
        return self.tree_sum(root.left) + self.tree_sum(root.right) + root.value
    
    def min_value_tree(self,root):
        if root == None:
            return 9999
        result = min(self.min_value_tree(root.left),self.min_value_tree(root.right),root.value)
        return result
        

        
        
        

                
            
        
        
                
                
                
        
my_Tree = BinarySearchTree()
my_Tree.insert(5)
my_Tree.insert(3)
my_Tree.insert(2)
my_Tree.insert(4)
my_Tree.insert(7)
my_Tree.insert(9)
my_Tree.insert(1)



# print(my_Tree.insert(3))
# print(my_Tree.insert(9))
# print(my_Tree.root.value)
# print(my_Tree.root.left.value)
# print(my_Tree.root.right.value)

# print(my_Tree.contains(9))
# print(my_Tree.contains(6))


# print("InOrder Display  : ")
# my_Tree.display_inorder(my_Tree.root)
# print("")
# print("preOrder Display  : ")
# my_Tree.display_preorder(my_Tree.root)
# print("")
# print("postOrder Display  : ")
# my_Tree.display_postorder(my_Tree.root)



# print("depth first traversal  : ")
# print(my_Tree.depth_first_search(my_Tree.root))

# print(my_Tree.breadth_first_search(my_Tree.root))


# print("The value is Found  : ",my_Tree.search_element_dfs(my_Tree.root,21))



# print("The sum of the tree is  : ",my_Tree.tree_sum(my_Tree.root))

print("The min value of the tree is  : ",my_Tree.min_value_tree(my_Tree.root))
