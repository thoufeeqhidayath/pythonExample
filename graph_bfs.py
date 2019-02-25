import queue
class bfs:
    def __init__(self):
        self.queues = queue.queue()
        self.graphs = {}
        self.graph_vertices = []
        self.list_after_bfs= []
        self.checkVisit = {}

    def bfs(self, graph={}):
        self.graphs = graph
        self.graph_vertex = graph.keys()
        if self.put_initial() == 0:
            self.extract_function()
        print self.bfslist
