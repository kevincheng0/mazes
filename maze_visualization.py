from maze import *
from pathfind import *
import PySimpleGUI as sg


def get_board():
    dimensions = start = goal = []*2
    sg.theme('DarkAmber')
    layout = [  [sg.Text('Enter the dimensions, start, and goal')],
                [sg.Text('Width:'), sg.InputText()],
                [sg.Text('Height:'), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    window = sg.Window('Board Dimensions', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        else:
            dimensions = [int(values[0]), int(values[1])]
            break

    window.close()

    u = Grid(dimensions[0], dimensions[1])
    u.grid = [[Node(x, y, value=' ') for x in range(dimensions[1])] for y in range(dimensions[0])]

    layout = [[sg.Button('', size=(4, 2), key=(i,j), pad=(0,0)) for i in range(dimensions[0])] for j in range(dimensions[1])]
    layout.extend([[sg.Text('Start:'), sg.InputText()],
                  [sg.Text('Goal:'), sg.InputText()],
                  [sg.Button('Apply'), sg.Button('Ok'), sg.Button('Cancel')]])
 
    window = sg.Window('Setup Board', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        elif event == 'Apply':
            print('applying')
            start = [int(x) for x in values[0].split(' ')]
            goal = [int(x) for x in values[1].split(' ')]
            window[(start[0], start[1])].update('st', button_color=('white','green'))
            window[(goal[0], goal[1])].update('fin', button_color=('white','red'))
        elif event == 'Ok':
            pathfind(u, start, goal)
            print(u.path)
            for node in u.path:
                window[(node.x, node.y)].update('path', button_color=('white','blue'))
                print('')
        else:
            window[event].update('#', button_color=('white','black'))
            u.grid[event[1]][event[0]].value = '#'
            print(event)

    for y in range(u.height):
        for x in range(u.width):
            print(u.grid[y][x].value, end='')
        print('')
    window.close()


if __name__ == '__main__':
    get_board()



