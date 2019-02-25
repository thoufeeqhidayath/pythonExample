import graphss
import bfsPro
import stacks

str=['cat','q','m','a','m','d','rat','hat','s','z','q','p','cat','q','a','m','d','s','rat','hat','z','q','p','a','z']

class programx:
    def __init__(self):
        self.bfs_list=[]
        self.graph={}
        self.q = stacks.stack()
        self.sequences=[]
        self.count=0


    def function(self):
        g = graphss.Graph({})
        for i in range(0, len(str) - 1):
            g.add_edge(str[i], str[i + 1])
        self.graph=g.logs()
        b = bfsPro.bfs()
        b.bfs(g.logs())
        self.bfs_list = b.get_bfs_list()
        for node in self.bfs_list:
            for m in self.graph[node].keys():
              if self.graph[node][m]>1:
               self.sequences.append("||")
               self.sequences.append(node)
               self.depth_search(node)

        print self.sequences


    def depth_search(self,Node,path=[]):
           for x in self.graph[Node].keys():
               if self.graph[Node][x]>1:
                self.graph[Node][x]=self.graph[Node][x]-2
                self.q.push(x)
           while(self.q.size()>0):
               s=self.q.pop()
               if self.graph[s].keys()>1:
                self.sequences.append(s)
                self.depth_search(s)
















    if __name__ == '__main__':
     function()