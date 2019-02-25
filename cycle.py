import graphss
import stacks
import bfsPro
class cycles:
    def __init__(self):
        self.bfs_list = []
        self.graph = {}
        self.stacks = stacks.stack()
        self.sequences = []
        self.count = 0
        self.bfs = bfsPro.bfs()

    def graphs(self):
        g = graphss.Graph()
        g.add_edge('a', 'b')
        g.add_edge('a', 'c')
        g.add_edge('b', 'd')
        g.add_edge('b', 'e')
        g.add_edge('c', 'f')
        g.add_edge('c', 'g')
        g.add_edge('g', 'a')
        self.graph = g.get_the_graph()
        print self.graph
        self.bfslist()


    def bfslist(self):
        self.bfs.bfs(self.graph)
        self.bfs_list = self.bfs.get_bfs_list()
        print self.bfs_list
        self.recursive()

    def recursive(self):
        for element in self.bfs_list:
            for inner_elemnt in self.graph.keys():
                print ""




