import graph_lib

class Vertex:
    def __init__(self, name,edges={}):
        self.name = name
        self.edges = edges

    def __init__(self,name):
        self.name=name


    def add_edge(self,name):
        if name not in self.edges:
            self.edges[name] = 1
        else:
            self.edges[name] =  self.edges[name] + 1

    def add_edges(self,edges):
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

    # Find the distinct list of edges
    def find_edges(self):
        output    = {}
        for vertex in self.vertices:
            for edge in self.vertices[vertex].edges:
                count = 0
                if edge in output:
                    count = output[edge]
                output  [edge] = self.vertices[vertex].edges[edge] + count
        return output

    # Add the vertex as a key
    def add_vertex(self, vertex_name):
       if vertex_name not in self.vertices:
            self.vertices[vertex_name] = Vertex(vertex_name)

    def add_edge(self, fromVertex,toVertex):
        if fromVertex not in self.vertices:
            self.vertices[fromVertex] = Vertex(fromVertex)

        self.vertices[fromVertex].add_edge(toVertex)

    def union(self, graph2):
        out_graph = Graph({})
        for vertex in self.vertices:
            out_graph.add_vertex(vertex)
            out_graph.vertices[vertex].add_edges(self.vertices[vertex].edges)

        for vertex in graph2.vertices:
            out_graph.add_vertex(vertex)
            out_graph.vertices[vertex].add_edges(graph2.vertices[vertex].edges)

        return out_graph

    def log(self):
        print("-----------graph--------------")
        for vertex in self.vertices:
            print("vertex : ", vertex, ", edges : ", self.vertices[vertex].edges)
        print("------------------------------")