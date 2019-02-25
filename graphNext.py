import graphss

def sample1():
   i=0


g = graphss.Graph({})
g.add_vertex("a")
g.add_vertex("b")
g.add_vertex("c")
g.add_vertex("d")
g.add_vertex("f")
g.add_edge('a','e')
g.add_edge('a','c')
g.add_edge('a','d')
g.add_edge('f','a')
g.add_edge('v','w')
g.add_edge('v','w')
g.log()




