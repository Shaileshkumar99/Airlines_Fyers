graph = {'a':{'b':10,'c':3}, 'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}

def dijkstra(graph,start,goal):
    sortest_distance = {}
    unvisited = graph
    precedence = {}
    path = []
    infinity = 99999

    for node in unvisited:
        sortest_distance[node]=infinity
    sortest_distance[start] = 0

    while unvisited:
        minNode = None

        for node in unvisited:
            if minNode is None:
                minNode = node
            elif sortest_distance[node] < sortest_distance[minNode]:
                minNode = node

        for child, weight in graph[minNode].items()  :
            if weight + sortest_distance[minNode] < sortest_distance[child]:
                sortest_distance[child] = weight + sortest_distance[minNode]
                precedence[child] = minNode
        unvisited.pop(minNode)

    # print(sortest_distance)

    currnt = goal
    while currnt != start:
        path.insert(0,currnt)
        currnt = precedence[currnt]
    path.insert(0, start)
    print(path)
    print(sortest_distance[goal])


dijkstra(graph,'a','d')