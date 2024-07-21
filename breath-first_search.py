class Node():
    def __init__(self,state,parent):
        self.state = state
        self.parent = parent

class QueqeFrontier():
    def __init__(self, frontier = []):
        self.frontier = frontier
    def add(self,state):
        self.frontier.append(state)
    def empty(self):
        return len(self.frontier) == 0
    def contains_state(self,state):
        return any(node.state == state for node in self.frontier)
    def remove(self):
        if self.empty():
            raise Exception('Empty Frontier')
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class Graph():
    def __init__(self,graph=[]):
        self.graph = graph
    def readfile(self):
        file = open('maze.txt', mode= 'r')
        m,n = map(int, file.readline().split())
        for i in range(n):
            self.graph.append([])
        for i in range (m):
            j = file.readline()
            self.graph[int(j[0])-1].append(int(j[2]))
    def solve(self):
        frontier = QueqeFrontier()
        start = Node(state=1,parent=None)
        frontier.add(start)
        self.explored = set()
        while True:
            if frontier.empty():
                raise Exception('No solution')
            node = frontier.remove()
            if node.state == 5:
                cells = []
                while node.parent is not None:
                    cells.append(node.state)
                    node = node.parent
                cells.append(node.state)
                cells.reverse()
                print(cells)
                return
            self.explored.add(node.state)
            for state in self.graph[node.state - 1]:
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node)
                    frontier.add(child)
_graph = Graph()
_graph.readfile()
_graph.solve()

