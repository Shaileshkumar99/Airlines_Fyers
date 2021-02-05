class Node(object):
    def __init__(self,name):
        self.name = name
        self.adjency = []
        self.visited = False

class BreathFirstSearch(object):

    def bfs(self,startNode):

        queue = []
        queue.append(startNode)
        startNode.visited = True

        while queue:

            node = queue.pop(0)
            print(node.name)

            for n in node.adjency:
                if not n.visited:
                    n.visited = True
                    queue.append(n)

if __name__ == "__main__":
    node1 = Node("A")
    node2 = Node("b")
    node3 = Node("c")
    node4 = Node("d")
    node5 = Node("e")
    node6 = Node("f")

    node1.adjency.append(node3)
    node1.adjency.append(node6)
    node2.adjency.append(node5)
    node3.adjency.append(node4)
    node4.adjency.append(node2)
    node5.adjency.append(node1)

    b = BreathFirstSearch()
    b.bfs(node1)

