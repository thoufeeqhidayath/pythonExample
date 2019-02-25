class Vertex:
    def __init__(self, name,edges={}):
        self.name = name
        self.edges = edges


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

    def find_edges(self):
        output = {}
        for vertex in self.vertices:
            for edge in self.vertices[vertex].edges:
                count = 0
                if edge in output:
                    count = output[edge]
                output[edge] = self.vertices[vertex].edges[edge] + count
        return output



    # Add the vertex as a key
    def add_vertex(self, vertex_name):
       if vertex_name not in self.vertices:
            self.vertices[vertex_name] = Vertex(vertex_name,{})

    def add_edge(self, fromVertex,toVertex):
        if fromVertex not in self.vertices:
            self.vertices[fromVertex] = Vertex(fromVertex,{})

        self.vertices[fromVertex].add_edge(toVertex)


    def log(self):
        print("-----------graph--------------")
        for vertex in self.vertices:
            print vertex,self.vertices[vertex].edges
        print self.vertices['a'].edges.keys()

    def logs(self):
        graph={}
        for vertex in self.vertices:
            graph[vertex]=self.vertices[vertex].edges
        return graph

    def get_the_graph(self):
        graph = {}
        for vertex in self.vertices:
            graph[vertex] = self.vertices[vertex].edges
        return graph

    def get_the_vertex(self):
        vertex_list=[]
        for vertex in self.vertices:
            vertex_list.append(vertex)
        return vertex_list

    def vertex_more_two(self):
        vertex_list =self.get_the_vertex()
        return vertex_list


    def get_edges_of_vertex(self,vertex):
        return self.vertices[vertex].edges.keys()



    def get_the_key_of_vertex(self):
        keys={}
        for vertex in self.get_the_vertex():
            keys[vertex] = self.get_edges_of_vertex(vertex)
        print keys
        print keys['c']

        print self.vertices['a'].edges[(keys['a'])[1]]

    def get_the_key_of_vertex(self,vertex):
        keyss = []
        keyss.append(self.get_edges_of_vertex(vertex))
        print (keyss[0])[0]







