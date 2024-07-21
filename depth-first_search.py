class node():
    def __init__(self,state,parent):
        self.state = state
        self.parent = parent

class stackFrontier():
    def __init__(self, frontier = []):
        self.frontier = frontier
    def add(self, node):
        self.frontier.append(node)
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    def empty(self):
        return len(self.frontier) == 0
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
class maze():
    def __init__(self, _maze):
        self.file = open('maze.txt', mode = 'r')
        self.maze = _maze
    def rfile(self):
        m, n = map(int, self.file.readline().split())
        for i in range(n):
            self.maze.append([])
        for i in range (m):
            j = self.file.readline()
            self.maze[int(j[0])-1].append(int(j[2]))
    def get(self):
        return self.maze
    def solve(self):
        frontier = stackFrontier()
        start = node(state = 1, parent=None)
        frontier.add(start)
        self.explored = set()
        while True:
            if frontier.empty():
                raise Exception("No solution")
            Node = frontier.remove()
            if Node.state == 5:
                cells = []
                while Node.parent is not None:
                    cells.append(Node.state)
                    Node = Node.parent
                cells.append(Node.state)
                cells.reverse()
                print(cells)
                return
            self.explored.add(Node.state)
            for state in self.maze[Node.state-1]:
                if not frontier.contains_state(state) and state not in self.explored:
                    child = node(state = state,parent=Node)
                    frontier.add(child)

maz = maze([])
maz.rfile()
maz.solve()             

                

