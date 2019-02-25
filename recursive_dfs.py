import stacks
import graphss
class dfs:

    def dfs_iterative(self,graph, start):
        stack, path = [start], []

        while stack:
            vertex = stack.pop()
            if vertex in path:
                continue
            path.append(vertex)
            for neighbor in graph[vertex]:
                stack.append(neighbor)

        return path
