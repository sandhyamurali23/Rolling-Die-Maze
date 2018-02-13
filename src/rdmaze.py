
import copy
import math

'''
file: rdmaze.py
language: python3
author: Rohan Shiroor(rss1103@g.rit.edu),Sandhya Murali(sm2290@g.rit.edu)
description: Determines shortest path from start to goal using A* search


'''

class Queue:

    __slots__ = 'list'

    def __init__(self):
        '''
            Creates a Queue object
        '''
        self.list=[]



    def enqueue(self,Node):

        '''
        Adds a Node into a sorted list.
        :param Node: Node object representing the cell of a maze

        '''

        list=self.list

        if(len(list)==0):
            list.append(Node)

        else:
            flag=0
            for i in range(len(list)):

                node=list[i]

                if(node.f>Node.f):
                    list.insert(i,Node)
                    flag=1
                    break

            if(flag==0):
                list.append(Node)

    def dequeue(self,i):

        '''
        Remove a node from the list at that index.
        :param i: index location to remove the node

        '''

        return self.list.pop(i)


class Node:
    __slots__ = 'i', 'j', 'f', 'g', 'h', 'dice_orientation','parent_i','parent_j','dice_top','parent'

    def __init__(self,i,j,f,g,h,dice,parent_i,parent_j,dice_top,parent):
        '''
        Creates a Node object object
        :param i: row value
        :param j:column value
        :param f:f value of the cell
        :param g: g value of the cell
        :param h: h value of the cell
        :param dice_orientation: dice object to store current configuration of the node
        :param parent_i: parent row
        :param parent_j: parent column
        :param dice_top: top of the die
        :param parent: parent Node
        '''
        self.i=i
        self.j=j
        self.f=f
        self.g=g
        self.h=h
        self.dice_orientation=dice
        self.parent_i=parent_i
        self.parent_j=parent_j
        self.dice_top=dice_top
        self.parent=parent


class make_pair:
    __slots__ = 'row', 'col','dice'

    def __init__(self,row,col,dice):
        '''
        Creates a make pair object to for tracing the path
        :param row: row value
        :param col: column value
        :param dice: dice object
        '''
        self.row=row
        self.col=col
        self.dice=dice


class dice:
    __slots__ = 'north','south','east','west','top','bottom'

    def __init__(self):
        '''
        Creates a dice object
        :param north: north face
        :param south: south face
        :param east:  east face
        :param west: west face
        :param top: top face
        :param bottom: bottom face

        '''
        self.north=2
        self.south=5
        self.east=3
        self.west=4
        self.top=1
        self.bottom=6




def take_input():
    '''
    Takes input from user to specify file name
    :return:
    '''
    file_name=input('Enter file name : ')

    read_maze(file_name)

def read_maze(file_name):
    '''
    Read maze from file
    :param file_name: file name from user
    :return:
    '''
    ins = open(file_name, "r")

    data = [] #stores the data from file into list
    for line in ins:
        line_strings = line.rstrip()
        maze_point = [n for n in line_strings]
        data.append(maze_point)

    displayboard(data)
    print()


    max_row=len(data) #computes max row
    max_col=len(data[0]) #computes max col
    maze_state(data,max_row,max_col)


def maze_state(data,max_row,max_col):
    '''
    Determines the start and goal position
    :param file_name: file name from user
    :param max_row: maximum row of the maze
    :param max_col: maximum col of the maze
    :return:
    '''

    start_node_i=-1
    start_node_j=-1
    dest_node_i=-1
    dest_node_j=-1
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j]=='S':
                start_node_i=i
                start_node_j=j

            if(data[i][j]=='G'):
                dest_node_i=i
                dest_node_j=j



    dice_initial=dice()  #initial dice configuration
    node=Node(start_node_i,start_node_j,0.0,0.0,0.0,dice_initial,start_node_i,start_node_j,dice_initial.top,None)
    #node for stat cell

    Heuristics=[Eucledian,Manhatten,Diagonal]
    heuristic_name=['Eucledian Distance','Manhatten Distance','Diagonal Distance']

    for i in range(len(Heuristics)):
        print('For Heuristics :',heuristic_name[i])
        print()
        b=copy.deepcopy(data)
        Asearch(node,dest_node_i,dest_node_j,b,max_row,max_col,Heuristics[i]) #perform A* search
        print()
        print('-----------------------------------')


def displayboard(data):
    '''
    Displays the maze
    :param data: 2D list of maze
    :return:
    '''

    for row in data:
        for item in row:
            print(item, end=" ")
        print()

def tracepath(node,node_dest,data,count_queue,count_visited):
    '''
    Traces the path
    :param node: start node
    :param node_dest: destination node
    :param data: 2D list
    :param count_queue: Nodes generated in frontier
    :param count_visited: Nodes visited
    :return:
    '''
    print('the path is :')
    print()
    path=[]
    row=node_dest.i #dest row
    col=node_dest.j #dest col
    while (not (node_dest.dice_top == node.dice_top and node_dest.dice_orientation.east == node.dice_orientation.east
                and node_dest.dice_orientation.west == node.dice_orientation.west and node_dest.dice_orientation.north == node.dice_orientation.north
                and node_dest.dice_orientation.south == node.dice_orientation.south and node_dest.dice_orientation.bottom == node.dice_orientation.bottom
                and row == node.i and col == node.j)): #runs until not reached start node with initial configuration of die
        path.insert(0,make_pair(row,col,node_dest.dice_orientation)) #insert value
        node_temp=node_dest.parent #consider parent of the node
        node_dest=node_temp
        row=node_dest.i #update row and column values
        col=node_dest.j

    path.insert(0,make_pair(row,col,node.dice_orientation)) #insert start

    list_path=[]
    while(len(path)!=0):
        path_val=path.pop(0)
        temp_list=[path_val.row,path_val.col]
        list_path.append(temp_list)
        data[path_val.row][path_val.col]='~'
        print('Iteration :')
        print()
        print('point selected : ',[path_val.row,path_val.col])
        print()
        displayboard(data)
        print()
        print('dice orientation :')
        print()
        print('east :',path_val.dice.east)
        print('west :', path_val.dice.west)
        print('north :', path_val.dice.north)
        print('south :', path_val.dice.south)
        print('top :', path_val.dice.top)
        print('bottom :', path_val.dice.bottom)
        print()

    print()
    print('Total path is : ',list_path)
    print('Nodes Generated : ', count_queue)
    print('Nodes visited : ', count_visited)
    print('Number of moves in the Solution : ',len(list_path))




def Asearch(node,dest_row,dest_col,data,max_row,max_col,heuristics):

    '''
    Performs A* search
    :param node: start node
    :param dest_row: destination row
    :param dest_col: destination column
    :param data: 2D maze list
    :param max_row: maximum row of the maze
    :param max_col: maximum column of the maze
    :param heuristics: Heuristic function
    :return:
    '''


    visited=[] #visited list

    q=Queue()  #create queue
    count_visited = 0 #count visited nodes
    count_queue = 0 #count nodes generated in the frontier queue
    q.enqueue(node) #push in queue
    count_queue=count_queue+1

    found_dest=False

    while q.list:

        node_pop=q.dequeue(0) #pop the node
        curr_dice_config=node_pop.dice_orientation #get dice configuration of the node
        visited.append(node_pop) #mark it visited
        count_visited=count_visited+1

        if node_pop.i==dest_row and node_pop.j==dest_col: #check if destination is reached

            if(node_pop.dice_top==1): #check if top is 1
                print('GOAL FOUND!!!')
                print()
                found_dest=True
                tracepath(node,node_pop,data,count_queue,count_visited) #trace the path from start to goal
                break

        #check north
        row = node_pop.i - 1
        col = node_pop.j

        if (isValid(row, col,max_row,max_col) == True and isUnBlocked(data, row, col) == True): #check if there is no block
                                                                                                #and row and col is within range
            valid, new_dice_config = check_north(curr_dice_config) #check valid dice configuration in the north

            visited_flag = 0 #check if node with same configuration is visited
            for index in range(len(visited)):
                node_temp = visited[index]
                if (node_temp.i == row and node_temp.j == col):
                    if (node_temp.dice_top == new_dice_config.top and node_temp.dice_orientation.east==new_dice_config.east and
                        node_temp.dice_orientation.west==new_dice_config.west and node_temp.dice_orientation.north==new_dice_config.north
                        and node_temp.dice_orientation.south==new_dice_config.south and node_temp.dice_orientation.bottom==new_dice_config.bottom):
                        visited_flag = 1
                        break

            if valid == True and visited_flag == 0: #if no 6 on top and not visited
                gNew = node_pop.g + 1.0
                hNew = heuristics(row, col, dest_row, dest_col)
                fNew = gNew + hNew

                #check if node with current configuration is present in queue
                present_queue = 0
                queue_node = None
                for index in range(len(q.list)):
                    node_temp = q.list[index]

                    if (node_temp.i == row and node_temp.j == col):
                        if (node_temp.dice_top == new_dice_config.top and node_temp.dice_orientation.east == new_dice_config.east and
                            node_temp.dice_orientation.west == new_dice_config.west and node_temp.dice_orientation.north == new_dice_config.north
                            and node_temp.dice_orientation.south == new_dice_config.south and node_temp.dice_orientation.bottom == new_dice_config.bottom):
                            present_queue = 1
                            queue_node = node_temp
                            break

                if (present_queue == 0): #if not present in the frontier queue
                    node_push = Node(row, col, fNew, gNew, hNew, new_dice_config,node_pop.i, node_pop.j,
                                             new_dice_config.top,node_pop)
                    q.enqueue(node_push)
                    count_queue = count_queue + 1


                elif (present_queue == 1): #if present in the frontie queue, compare cost and consider node with lower f value
                    if (fNew <= queue_node.f):
                        for index in range(len(q.list)):
                            node_temp = q.list[index]
                            if (node_temp.i == row and node_temp.j == col):
                                if (node_temp.dice_top == new_dice_config.top and node_temp.dice_orientation.east == new_dice_config.east and
                                node_temp.dice_orientation.west == new_dice_config.west and node_temp.dice_orientation.north == new_dice_config.north
                                and node_temp.dice_orientation.south == new_dice_config.south and node_temp.dice_orientation.bottom == new_dice_config.bottom):
                                    q.dequeue(index)
                                    node_push = Node(row, col, fNew, gNew, hNew, new_dice_config, node_pop.i,
                                                     node_pop.j,new_dice_config.top, node_pop)
                                    q.enqueue(node_push)
                                    break





        # check south
        row = node_pop.i+1
        col = node_pop.j

        if (isValid(row, col, max_row, max_col) == True and isUnBlocked(data, row, col) == True):
            valid, new_dice_config = check_south(curr_dice_config)

            visited_flag = 0
            for index in range(len(visited)):
                node_temp = visited[index]
                if (node_temp.i == row and node_temp.j == col):
                    if (node_temp.dice_top == new_dice_config.top and node_temp.dice_orientation.east == new_dice_config.east and
                        node_temp.dice_orientation.west == new_dice_config.west and node_temp.dice_orientation.north == new_dice_config.north
                        and node_temp.dice_orientation.south == new_dice_config.south and node_temp.dice_orientation.bottom == new_dice_config.bottom):
                        visited_flag = 1
                        break

            if valid == True and visited_flag == 0:
                gNew = node_pop.g + 1.0
                hNew = heuristics(row, col, dest_row, dest_col)
                fNew = gNew + hNew

                present_queue = 0
                queue_node = None
                for index in range(len(q.list)):
                    node_temp = q.list[index]

                    if (node_temp.i == row and node_temp.j == col):
                        if (node_temp.dice_top == new_dice_config.top and node_temp.dice_orientation.east == new_dice_config.east and
                            node_temp.dice_orientation.west == new_dice_config.west and node_temp.dice_orientation.north == new_dice_config.north
                            and node_temp.dice_orientation.south == new_dice_config.south and node_temp.dice_orientation.bottom == new_dice_config.bottom):
                            present_queue = 1
                            queue_node = node_temp
                            break

                if (present_queue == 0):
                    node_push = Node(row, col, fNew, gNew, hNew, new_dice_config, node_pop.i, node_pop.j,
                                     new_dice_config.top,node_pop)
                    q.enqueue(node_push)
                    count_queue = count_queue + 1


                elif (present_queue == 1):
                    if (fNew <= queue_node.f):
                        for index in range(len(q.list)):
                            node_temp = q.list[index]
                            if (node_temp.i == row and node_temp.j == col):
                                if (node_temp.dice_top == new_dice_config.top and node_temp.dice_orientation.east == new_dice_config.east and
                                    node_temp.dice_orientation.west == new_dice_config.west and node_temp.dice_orientation.north == new_dice_config.north
                                    and node_temp.dice_orientation.south == new_dice_config.south and node_temp.dice_orientation.bottom == new_dice_config.bottom):
                                    q.dequeue(index)
                                    node_push = Node(row, col, fNew, gNew, hNew, new_dice_config, node_pop.i,
                                                     node_pop.j, new_dice_config.top, node_pop)
                                    q.enqueue(node_push)
                                    break


        # check east
        row = node_pop.i
        col = node_pop.j+1

        if (isValid(row, col, max_row, max_col) == True and isUnBlocked(data, row, col) == True):
            valid, new_dice_config = check_east(curr_dice_config)

            visited_flag = 0
            for index in range(len(visited)):
                node_temp = visited[index]
                if (node_temp.i == row and node_temp.j == col):
                    if (node_temp.dice_top == new_dice_config.top and node_temp.dice_orientation.east == new_dice_config.east and
                        node_temp.dice_orientation.west == new_dice_config.west and node_temp.dice_orientation.north == new_dice_config.north
                        and node_temp.dice_orientation.south == new_dice_config.south and node_temp.dice_orientation.bottom == new_dice_config.bottom):
                        visited_flag = 1
                        break

            if valid == True and visited_flag == 0:
                gNew = node_pop.g + 1.0
                hNew = heuristics(row, col, dest_row, dest_col)
                fNew = gNew + hNew

                present_queue = 0
                queue_node = None
                for index in range(len(q.list)):
                    node_temp = q.list[index]

                    if (node_temp.i == row and node_temp.j == col):
                        if (node_temp.dice_top == new_dice_config.top and node_temp.dice_orientation.east == new_dice_config.east and
                            node_temp.dice_orientation.west == new_dice_config.west and node_temp.dice_orientation.north == new_dice_config.north
                            and node_temp.dice_orientation.south == new_dice_config.south and node_temp.dice_orientation.bottom == new_dice_config.bottom):
                            present_queue = 1
                            queue_node = node_temp
                            break

                if (present_queue == 0):
                    node_push = Node(row, col, fNew, gNew, hNew, new_dice_config, node_pop.i, node_pop.j,
                                     new_dice_config.top,node_pop)
                    q.enqueue(node_push)
                    count_queue = count_queue + 1


                elif (present_queue == 1):
                    if (fNew <= queue_node.f):
                        for index in range(len(q.list)):
                            node_temp = q.list[index]
                            if (node_temp.i == row and node_temp.j == col):
                                if (node_temp.dice_top == new_dice_config.top and node_temp.dice_orientation.east == new_dice_config.east and
                                    node_temp.dice_orientation.west == new_dice_config.west and node_temp.dice_orientation.north == new_dice_config.north
                                    and node_temp.dice_orientation.south == new_dice_config.south and node_temp.dice_orientation.bottom == new_dice_config.bottom):
                                    q.dequeue(index)
                                    node_push = Node(row, col, fNew, gNew, hNew, new_dice_config, node_pop.i,
                                                     node_pop.j, new_dice_config.top, node_pop)
                                    q.enqueue(node_push)

                                    break





        # check west
        row = node_pop.i
        col = node_pop.j-1

        if (isValid(row, col, max_row, max_col) == True and isUnBlocked(data, row, col) == True):
            valid, new_dice_config = check_west(curr_dice_config)

            visited_flag = 0
            for index in range(len(visited)):
                node_temp = visited[index]
                if (node_temp.i == row and node_temp.j == col):
                    if (node_temp.dice_top == new_dice_config.top and node_temp.dice_orientation.east == new_dice_config.east and
                        node_temp.dice_orientation.west == new_dice_config.west and node_temp.dice_orientation.north == new_dice_config.north
                        and node_temp.dice_orientation.south == new_dice_config.south and node_temp.dice_orientation.bottom == new_dice_config.bottom):
                        visited_flag = 1
                        break

            if valid == True and visited_flag == 0:
                gNew = node_pop.g + 1.0
                hNew = heuristics(row, col, dest_row, dest_col)
                fNew = gNew + hNew

                present_queue = 0
                queue_node = None
                for index in range(len(q.list)):
                    node_temp = q.list[index]

                    if (node_temp.i == row and node_temp.j == col):
                        if (node_temp.dice_top == new_dice_config.top and node_temp.dice_orientation.east == new_dice_config.east and
                            node_temp.dice_orientation.west == new_dice_config.west and node_temp.dice_orientation.north == new_dice_config.north
                            and node_temp.dice_orientation.south == new_dice_config.south and node_temp.dice_orientation.bottom == new_dice_config.bottom):
                            present_queue = 1
                            queue_node = node_temp
                            break

                if (present_queue == 0):
                    node_push = Node(row, col, fNew, gNew, hNew, new_dice_config, node_pop.i, node_pop.j,
                                 new_dice_config.top,node_pop)
                    q.enqueue(node_push)
                    count_queue = count_queue + 1

                elif (present_queue == 1):
                    if (fNew <= queue_node.f):
                        for index in range(len(q.list)):
                            node_temp = q.list[index]
                            if (node_temp.i == row and node_temp.j == col):
                                if (node_temp.dice_top == new_dice_config.top and node_temp.dice_orientation.east == new_dice_config.east and
                                    node_temp.dice_orientation.west == new_dice_config.west and node_temp.dice_orientation.north == new_dice_config.north
                                    and node_temp.dice_orientation.south == new_dice_config.south and node_temp.dice_orientation.bottom == new_dice_config.bottom):
                                    q.dequeue(index)
                                    node_push = Node(row, col, fNew, gNew, hNew, new_dice_config, node_pop.i,
                                                     node_pop.j, new_dice_config.top, node_pop)
                                    q.enqueue(node_push)
                                    break


    if(found_dest==False): # if destination with required configuration is not met
        print('No solution!!!')
        print()
        print('Nodes Generated : ', count_queue)
        print('Nodes visited : ', count_visited)
        print('Number of Moves is : -1')



def Eucledian(row,col,dest_row,dest_col):
    '''
    Performs Eucledian distance
    :param row: row value
    :param col: column value
    :param dest_row: destination row
    :param dest_col: destination column
    :return:
    '''
    return (
    math.sqrt((row - dest_row) * (row - dest_row)
         + (col - dest_col) * (col - dest_col)))

def Manhatten(row,col,dest_row,dest_col):
    '''
    Performs Manhatten distance
    :param row: row value
    :param col: column value
    :param dest_row: destination row
    :param dest_col: destination column
    :return:
    '''

    return (abs(dest_row-row)+abs(dest_col-col))

def Diagonal(row,col,dest_row,dest_col):
    '''
    Performs Diagonal distance
    :param row: row value
    :param col: column value
    :param dest_row: destination row
    :param dest_col: destination column
    :return:
    '''
    return (max(abs(dest_row-row),abs(dest_col-col)))

def isValid(row,col,max_row,max_col):
    '''
    checks if row and column is within boundary range of the maze
    :param row: row value
    :param col: column value
    :param max_row: maximum row
    :param max_col: maximum column
    :return:
    '''

    if(row>=0 and row<max_row and col>=0 and col<max_col):
        return True

    return False


def isUnBlocked(data,row,col):
    '''
    checks if row and column is within boundary range of the maze
    :param row: row value
    :param col: column value
    :param max_row: maximum row
    :param max_col: maximum column
    :return:
    '''

    if(data[row][col]!='*'):
        return True
    return False

def check_north(dice1):
    '''
    rotates die in the north
    :param dice1: dice confiuration

    '''
    dice_temp = copy.deepcopy(dice1)
    temp = dice_temp.north
    dice_temp.north = dice_temp.top
    dice_temp.bottom, temp = temp, dice_temp.bottom
    dice_temp.south, temp = temp, dice_temp.south
    dice_temp.top = temp

    if (dice_temp.top == 6):
        return False, dice1

    else:
        return True, dice_temp

def check_south(dice1):
    '''
    rotates die in the south
    :param dice1: dice confiuration

    '''
    dice_temp = copy.deepcopy(dice1)
    temp = dice_temp.south
    dice_temp.south = dice_temp.top
    dice_temp.bottom, temp = temp, dice_temp.bottom
    dice_temp.north, temp = temp, dice_temp.north
    dice_temp.top = temp

    if(dice_temp.top==6):
        return False,dice1

    else:
        return True,dice_temp


def check_east(dice1):
    '''
    rotates die in the east
    :param dice1: dice confiuration

    '''
    dice_temp = copy.deepcopy(dice1)
    temp = dice1.east
    dice_temp.east = dice_temp.top
    dice_temp.bottom, temp = temp, dice_temp.bottom
    dice_temp.west, temp = temp, dice_temp.west
    dice_temp.top = temp

    if (dice_temp.top == 6):
        return False, dice1

    else:
        return True, dice_temp


def check_west(dice1):
    '''
    rotates die in the west
    :param dice1: dice confiuration

    '''
    dice_temp = copy.deepcopy(dice1)
    temp = dice_temp.west
    dice_temp.west = dice_temp.top
    dice_temp.bottom, temp = temp, dice_temp.bottom
    dice_temp.east, temp = temp, dice_temp.east
    dice_temp.top = temp

    if (dice_temp.top == 6):
        return False, dice1

    else:
        return True, dice_temp




if __name__ == '__main__':
    take_input()