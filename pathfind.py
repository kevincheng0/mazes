from maze import Grid, Node

WALL = '#'
PATH = ' '

def find_min(list):
    min_node = None
    for node in list:
        if min_node is None or node.f <= min_node.f:
            min_node = node

    return min_node

def get_path(u, node, start):
    if node.x == start[0] and node.y == start[1]:
        u.path.append(node)
        return
    elif node.parent is not None:
        u.path.append(node)
        get_path(u, node.parent, start)
    else:
        return

def compare(list, successor):
    for node in list:
        if node.x == successor.x and node.y == successor.y and node.f < successor.f:
            return True
    return False

def get_h(current, goal):
    x = abs(current[0] - goal[0])
    y = abs(current[1] - goal[1])
    return x * x + y * y

def a_star(grid, start, goal):
    open_list = [Node(start[0], start[1], f=0, g=0)]
    closed_list = []

    while open_list:
        current = find_min(open_list)
        for idx, node in enumerate(open_list):
            if node.x == current.x and node.y == current.y:
                del open_list[idx]

        for neighbour in Grid.find_neighbours(grid, current):
            if neighbour.x == goal[0] and neighbour.y == goal[1]:
                neighbour.set_parent(current)
                closed_list.append(current)
                return closed_list
            
            neighbour.h = get_h((neighbour.x, neighbour.y), goal)
            neighbour.f = neighbour.g + neighbour.h
            if compare(open_list, neighbour) or compare(closed_list, neighbour):
                continue
            else:
                open_list.append(neighbour)

        closed_list.append(current)

def pathfind(grid, start, goal):
    closed_list = a_star(grid, start, goal)
    get_path(grid, closed_list[-1], start)