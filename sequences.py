import graphss
import bfsPro
import stacks

str=['cat','q','m','a','m','d','rat','hat','s','z','q','p','cat','q','a','m','d','rat','hat','z','q','p','a','z','a','m','d','rat','w','a','m','d','rat']

class sequenceFind:

    def __init__(self):
        self.bfs_list=[]
        self.graph={}
        self.stacks = stacks.stack()
        self.sequences=[]
        self.count=0
        self.bfs = bfsPro.bfs()


    #add the elements of the string to graphs as Nodes
    def add_to_graph(self):
        graph = graphss.Graph({})
        for vertex in range(0, len(str) - 1):
            graph.add_edge(str[vertex], str[vertex + 1])
        self.graph = graph.get_the_graph()
        self.get_bfs_list()

    #get the bfs list from the graph
    def get_bfs_list(self):
        self.bfs.bfs(self.graph)
        self.bfs_list = self.bfs.get_bfs_list()
        self.get_the_sequences()
        print self.sequences

    #get the sequnces from the bfs list first breadth wise search take each element
    def get_the_sequences(self):
        for vertex in self.bfs_list:
            for inner_edge in self.graph[vertex].keys():
              if self.graph[vertex][inner_edge]>1:
                 self.recursive_depth_edges(vertex,inner_edge)

    def recursive_depth_edges(self,vertex,inner_edge):
        self.sequences.append("|")
        self.sequences.append(vertex)
        self.depth_search(vertex)
        #after findin sequence still the seqnce exist
        if self.graph[vertex][inner_edge]>1:
            return self.recursive_depth_edges(vertex,inner_edge)

    #from the breadth elemnt go depth wise
    def depth_search(self,vertex):
           for inner_edge in self.graph[vertex].keys():
               if self.graph[vertex][inner_edge]>1:
                self.graph[vertex][inner_edge]=self.graph[vertex][inner_edge]-2
                self.stacks.push(inner_edge)
                self.recursive_search()

    def recursive_search(self):
        while (self.stacks.size() > 0):
            edge = self.stacks.pop()
            if self.graph[edge].keys() > 1:
                self.sequences.append(edge)
                self.depth_search(edge)

