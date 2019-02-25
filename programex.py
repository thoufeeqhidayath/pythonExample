import graphss
import bfsss
import dfss
import bfsPro

str=['a','m','d','f','a','k','z','w','d','cat','f','a','k','cat','m','a','m','d','f','a','k','z','w','d','f','a','k','m','d','i','t','i','t']

class programx:
    g = graphss.Graph({})
    for i in range(0,len(str)-1):
        g.add_edge(str[i],str[i+1])

    find_the_sequences(g.logs())

    print(g.logs())



    graph =g.logs()
    b=bfsPro.bfs()
    b.bfs(graph)
    print("------------")


    print("_________>>>>")


    bfslist = b.get_bfs_list()

    print("------")
    for node in bfslist:

        if node in graph.keys():
         for graph_node in graph[node].keys():
             if graph[node][graph_node]>1:
                # graph[node][graph_node]=graph[node][graph_node]-2
                 print node,  graph_node



    def find_the_sequences(self,graph={}):
        graphs=graph
        list=[]
        state=0
        for Node in graphs.keys():
            state=0
            for inner_node in graph[Node].keys:
                if state==0:
                    if graph[Node][inner_node]>1:
                        list.append(Node)
                        list.append(inner_node)
                        graph[Node][inner_node]=graph[Node][inner_node]-2
                        state=1
                elif state==1:
                    if graph[Node][inner_node] > 1:
                        list.append(inner_node)
                        graph[Node][inner_node] = graph[Node][inner_node] - 2

        return list




















