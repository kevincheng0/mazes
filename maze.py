class Grid:
    WALL = '#'

    def __init__(self, width, height, grid):
        self.width = width
        self.height = height 
        self.grid = grid
        self.path = []

    def find_neighbours(self, node):
        neighbours = []
        for move in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
            new_x = move[0] + node.x 
            new_y = move[1] + node.y
            if new_x < 0 or new_x >= self.width or new_y < 0 or new_y >= self.height or self.grid[new_y][new_x].value == WALL:
                continue
            else:
                neighbours.append(Node(new_x, new_y, parent=node))
        return neighbours

    @staticmethod
    def nodes_equal(node1, node2):
        if node1.x == node2[0] and node1.y == node2[1]:
            return True
        return False

    def __repr__(self):
        return f'{self.grid}'


class Node:

    def __init__(self, x, y, f=None, g=None, h=None, value=None, parent=None):
        self.x = x
        self.y = y
        self.f = f
        self.g = g
        self.h = h
        self.value = value
        self.parent = parent

    def set_parent(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'Node({self.x}, {self.y})'