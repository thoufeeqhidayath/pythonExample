import graphss
import bfsPro
import stacks

str=['cat','q','a','m','d','rat','hat','s','z','q','p','cat','q','a','m','d','s','rat','hat']

class programx:
    def __init__(self):
        self.bfs_list=[]
        self.graph={}
        self.q = stacks.stack()
        self.sequences=[]
        self.count=0

    def main(self):
        self.add_into_graph()

    def add_into_graph(self):
        g = graphss.Graph({})
        for i in range(0, len(str) - 1):
            g.add_edge(str[i], str[i + 1])
        self.graph = g.logs()
        self.find_bfs()

    def find_bfs(self):
        b = bfsPro.bfs()
        b.bfs(self.graph)
        self.bfs_list = b.get_bfs_list()
        self.find_sequences()


    def find_sequences(self):
        for vertex in self.bfs_list:
            for edge in self.graph[vertex].keys():
                if self.graph[vertex][edge] > 1:
                    self.sequences.append("||")
                    self.sequences.append(vertex)
                    self.depth_search(edge)

        print self.sequences


    def depth_search(self ,Node ,path=[]):
        for x in self.graph[Node].keys():
            if self.graph[Node][x] > 1:
                self.graph[Node][x] = self.graph[Node][x] - 2
                self.q.push(x)
        while (self.q.size() > 0):
            s = self.q.pop()
            if self.graph[s].keys() > 1:
             self.sequences.append(s)
             self.depth_search(s)