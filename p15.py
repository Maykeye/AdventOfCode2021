import time
import heapq
input1 = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""


part1 = True


def make_node(cost_from_start, estimated_cost_to_goal, pos, came_from):
    assert came_from is None or (type(came_from) == tuple and len(came_from) == 2)
    assert (type(pos) == tuple and len(pos) == 2)
    return (cost_from_start, estimated_cost_to_goal, pos, came_from)

def node_known_cost(node):
    return node[0]
def node_estimate_cost(node):
    return node[1]
def node_pos(node):
    return node[2]
def node_prev_node(node):
    return node[3]
def node_update_known_cost(node, new_known_cost):
    return make_node(new_known_cost, node_estimate_cost(node), node_pos(node), node_prev_node(node))

def heur(grid, pos):
    width, height = len(grid[0]), len(grid)
    x, y = pos    
    r = abs(width - x) + abs(height - y)
    return r

def real_cost(grid, cur, dest):
    _ = cur
    x, y = dest
    return grid[y][x]

def main(s : str):
    def calc_neighbours(pos):
        x, y = pos
        res = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (x+dx) in range(width) and (y+dy) in range(height) and (dx != 0 or dy != 0) and (dx == 0 or dy == 0):
                    res.append((x+dx, y+dy))
        return res

        

    lines = s.strip().splitlines()
    grid = [[int(x) for x in row] for row in lines]
    width, height = len(grid[0]), len(grid)

    queue = []
    open_set = set()
    closed_set = set()
    nodes = {}
    start_node = make_node(0, heur(grid, (0,0)), (0,0), None)
    nodes[(0,0)] = start_node
    open_set.add((0,0))
    heapq.heappush(queue, start_node)
    while queue:
        current = heapq.heappop(queue)
        current_id = node_pos(current)
        open_set.remove(current_id)
        if current_id in closed_set:
            continue
        current = node_update_known_cost(current, node_known_cost(nodes[current_id]))
        closed_set.add(current_id)
        if current_id == (width-1, height-1):
            print("X")
            break
        for neighbour in calc_neighbours(current_id):
            new_distance_to_neighbour = node_known_cost(current) + real_cost(grid, current, neighbour)
            if neighbour not in nodes or new_distance_to_neighbour < node_known_cost(nodes[neighbour]):
                new_neighbour_node = make_node(new_distance_to_neighbour, heur(grid, neighbour), neighbour, current_id)
                nodes[neighbour] = new_neighbour_node
                # new or better node
                heapq.heappush(queue, new_neighbour_node)
                open_set.add(node_pos(new_neighbour_node))
    best = 0 
    cost = 0                
    while current_id:
        #print(current_id)
        current = nodes[current_id]
        x, y = current_id
        current_id = node_prev_node(current)
        cost += grid[y][x]
    
    print((current), cost-grid[0][0])



def runme():
    z=open("p15.input").read()    
    #z=input1
    start=time.time()
    main(z)
    print(f"Time: {time.time() - start}")
    #main(input1)
    #main(input2)
    #main(input3)

runme()
