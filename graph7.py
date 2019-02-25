class Vertex:
    def __init__(self, name,edges={}):
        self.name = name
        self.edges = edges

    def add_edge(self,name):
        if name not in self.edges:
            self.edges[name] = 1
        else:
            self.edges[name] =  self.edges[name] + 1

    def add_edges(self, edges):
        for name in edges:
            if name not in self.edges:
                self.edges[name] = edges[name]
            else:
                self.edges[name] = self.edges[name] + edges[name]

class Graph:
    def __init__(self, vertices={}):
        self.vertices = vertices

    # Get the keys of the dictionary
    def get_vertices(self):
        return list(self.vertices.keys())

    def get_edges(self):
        return self.find_edges()

