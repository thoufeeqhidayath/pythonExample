import stacks
class dfs:

    def __init__(self):
       self.q=stacks.stack()
       self.graphs={}
       self.graph_vertex=[]
       self.bfslist=[]
       self.visted_list=[]

    def bfs(self, graph={}):
        self.graphs = graph
        self.graph_vertex = graph.keys()
        if self.put_initial() == 0:
            self.extract_insert_remaining_nodes()
            self.check_whether_any_more()
        for x in self.bfslist:
            print(x)

    def put_initial_node(self):
        if len(self.graph_vertex) > 0:
            self.visted_list.append(self.graph_vertex[0])
            self.add_bfs_list(self.graph_vertex[0])
            self.add_to_queue(self.get_edges_list(self.graph_vertex[0]))
            return 0
        else:
            return 1

    def put_nodes(self, nodeName):
        if len(self.graph_vertex) > 0:
            self.visted_list.append(nodeName)
            self.add_bfs_list(nodeName)
            self.add_to_queue(self.get_edges_list(nodeName))
            return 0
        else:
            return 1

    def extract_insert_remaining_nodes(self):
        while self.get_queue_empty() == 0:
            vertex = self.remove_from_queue()
            if self.check_or_not(vertex) == 1:
                self.add_bfs_list(vertex)
                self.add_to_visited_list(vertex)
                if len(self.get_edges_list(vertex)) > 0:
                    self.add_to_queue(self.get_edges_list(vertex))

    def check_whether_any_more(self):
        for nodes in self.graph_vertex:
            if nodes not in self.visted_list:
                if self.put_nodes(nodes) == 0:
                    self.extract_insert_remaining_nodes()

    def getEdges(self, vertex):
        list = []
        for edges in self.graphs[vertex].keys():
            list.append(edges)
        return list

    def check_or_not(self, vertex):
        if vertex in self.visted_list:
            return 0;
        else:
            return 1

    def bfs_list(self, item):
        self.bfslist.append(item)

    def add_to_queue(self, vertices=[]):
        for vertex in range(0, len(vertices)):
            self.q.push(vertices[vertex])

    def remove_from_vertex(self):
        return self.q.pop()



    def get_queue_empty(self):
        if self.q.size() > 0:
            return 0
        else:
            return 1