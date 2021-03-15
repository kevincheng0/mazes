from maze import Grid, Node

WALL = '#'
PATH = ' '

def find_min(list):
    min_node = None
    for node in list:
        if min_node is None or node.f <= min_node.f:
            min_node = node
    return min_node

def find_path(closed_list):
    pass


def a_star(grid, start, goal):
    open_list = [Node(start[0], start[1], f=0, g=0)]
    closed_list = []

    while open_list:
        current = find_min(open_list)
        for idx, node in enumerate(open_list):
            if node.x == current.x and node.y == current.y:
                del open_list[idx]

        neighbours = []
        for neighbour in grid.find_neighbours(current):
            if neighbour.x == goal[0] and neighbour.y == goal[1]:
                neighbour.set_parent(current)
                closed_list.append(current)
                return find_path(closed_list)
        