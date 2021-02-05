import os
import sys
def swapNodes(indexes, queries):

    class Node:
        def __init__(self,value,level):
            self.value =value
            self.left = None
            self.right = None
            self.level = level

    def create_tree(indexes):
        from queue import Queue
        q = Queue()
        root = Node(1,1)
        maxlevel = 1
        q.put(root)

        for left , right in indexes:
            curr = q.get()
            if left != -1:
                leftNode = Node(left, curr.level+1)
                curr.left = leftNode
                q.put(leftNode)
            if right != -1:
                rightNode = Node(right, curr.level+1)
                curr.right = rightNode
                q.put(rightNode)

            maxlevel = curr.level

        return root, maxlevel


    def inorder_traverse(tree):
        if root.left :
            inorder_traverse(tree.left)

        item.append(tree.value)

        if root.right:
            inorder_traverse(tree.right)

    def swap_tree(tree, ks):
        if tree.left:
            swap_tree(tree.left,ks)
        if tree.right:
            swap_tree(tree.right, ks)
        if tree.level in ks:
            tree.left, tree.right = tree.right, tree.left
        return tree

    tree , maxlevel = create_tree(indexes)
    ret = []
    for k in queries:
        item = []
        ks = [x for x in range(1,maxlevel+1) if x%k == 0]
        root = swap_tree(tree, ks)
        inorder_traverse(root)
        ret.append(item)

    return ret

if __name__ == '__main__':

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)
