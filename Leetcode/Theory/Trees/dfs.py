# Use the stack, keep on storing the child and go deep


def depth_first_search(self,root):
    stack = [root]
    while len(stack) > 0:
        current_node = stack.pop()
        print(current_node.value)
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)