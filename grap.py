import gra

def sample1():
    g = gra.Graph({})
    return g


g = gra.Graph({})
g.add_edge('a','e')
g.add_edge('a','c')
g.add_edge('a','d')
g.add_edge('f','a')
g.add_edge('a','e')
g.add_edge('a','c')
g.add_edge('a','d')
g.add_edge('f','a')


g.log()
