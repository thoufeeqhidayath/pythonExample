import graph_lib
def main():
    sample1()

def sample1():
    g = graph_lib.Graph({})
    g.add_vertex("a")
    g.add_vertex("d")
    g.add_vertex("f")
    g.add_edge('a', 'd')
    g.add_edge('f', 'a')
    return g


g = graph_lib.Graph({})
g.add_vertex("a")
g.add_vertex("b")
g.add_vertex("c")
g.add_vertex("d")
g.add_vertex("f")
g.add_edge('a','e')
g.add_edge('a','c')
g.add_edge('a','d')
g.add_edge('f','a')

print(g.get_edges())

if __name__ == '__main__':
    main()
