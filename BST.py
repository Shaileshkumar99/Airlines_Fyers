class BST:
    def __init__(self, value):
        self.value = value
        self.left =  None
        self.right  = None

    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False

def validateBST(tree):
    return validateBSTHelper(tree, float('-inf'), float('inf'))

def validateBSTHelper(tree, minVal, maxVal):
    if tree is None:
        return True
    if tree.value < minVal or tree.value >= maxVal:
        return False
    leftValid = validateBSTHelper(tree.left, minVal, tree.value)
    return  leftValid and validateBSTHelper(tree.right, tree.value, maxVal)

def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swap(current)
        queue.append(current.left)
        queue.append(current.right)

def swap(tree):
    tree.left, tree.right = tree.right, tree.left