import graphss

str=['a','m','d','s','z','q','a','m','d','s','z','q','a','z']

class programx:
    def __init__(self):
        self.add='adds'

def function():
    g = graphss.Graph({})
    for i in range(0, len(str) - 1):
        g.add_edge(str[i], str[i + 1])
    graph = g.logs()
    print graph
    list = []
    state = 0

    for Node in graph.keys():
        state=0
        for inner_node in graph[Node].keys():
            if (state == 0):
                if graph[Node][inner_node] > 1:
                    list.append(Node)
                    list.append(inner_node)
                    graph[Node][inner_node] = graph[Node][inner_node] - 2
                    state=1
            elif (state==1):
                if graph[Node][inner_node] > 1:
                    list.append(inner_node)
                    graph[Node][inner_node] = graph[Node][inner_node] - 2
            state=0

    print list













