class Node(object):
    def __init__(self,name):
        self.name = name
        self.adjency = []
        self.visited = False

class DepthFirstSearch(object):

    def dfs(self,starNode):

        starNode.visited = True
        print(starNode.name)

        for n in starNode.adjency:
            if not n.visited:
                self.dfs(n)

if __name__ == "__main__":
    Node1 = Node("A")
    Node2 = Node("B")
    Node3 = Node("C")
    Node4 = Node("D")

    Node1.adjency.append(Node2)
    Node1.adjency.append(Node3)
    Node2.adjency.append(Node4)

    d = DepthFirstSearch()
    d.dfs(Node1)