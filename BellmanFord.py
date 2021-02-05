import sys

class Node(object):
    def __init__(self,name):
        self.name = name
        self.minDist = sys.maxsize
        self.precedence = None
        self.visited = False

class Edge(object):
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex

class BellmanFord(object):

    has_Cycle = False

    def ford(self,vertexList, edgeList, startVertex):

        startVertex.minDist = 0

        for _ in range(len(vertexList)-1):

            for edge in edgeList:
                u = edge.startVertex
                v = edge.targetVertex
                newDist = u.minDist + edge.weight

                if newDist < v.minDist:
                     v.minDist = newDist
                     v.precedence = u

        for edge in edgeList:
            if self.hasCycle(edge):
                print("Negative Cycle is Present")
                has_Cycle = True
                return;
    def hasCycle(self,edge):
        if (edge.startVertex.minDist + edge.weight) < edge.targetVertex.minDist:
            return True
        else:
            return False

    def getSortestPath(self,targetVertex):
        if not BellmanFord.has_Cycle:
            print(targetVertex.minDist)

            currnt = targetVertex

            while currnt is not None:
                print(currnt.name)
                currnt = currnt.precedence

        else:
            print("It has negative Cycle")

if __name__ == "__main__":

    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")

    edge1 = Edge(8,node1,node2)
    edge2 = Edge(12,node2,node3)
    edge3 = Edge(1, node1, node4)
    edge4 = Edge(5,node2, node3)
    edge5 = Edge(3,node3,node1)
    edge6 = Edge(10,node2,node4)

    vertexList = [node1,node2,node3,node4]
    edgeList = [edge1,edge2,edge3,edge4,edge5,edge6]

    bf = BellmanFord()
    bf.ford(vertexList,edgeList,node3)
    bf.getSortestPath(node2)
