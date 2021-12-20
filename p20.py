import copy
import time

input1 ="""\
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
"""
round_num=0
def expand_grid(g):
    new_width = len(g[0])+2
    

    new_grid =  [[round_num for _ in range(new_width)]] 
    new_grid += [[round_num] + row + [round_num] for row in g] 
    new_grid += [[round_num for _ in range(new_width)]]


    return new_grid

def print_grid(g):
    arr=".#"
    for row in g:
        print("".join([arr[c] for c in row]))

def get_at(x, y, grid):
    oob = round_num 
    if x < 0 or y < 0:
        return oob
    if y >= len(grid) or x >= len(grid[0]):
        return oob
    return grid[y][x]


def round(grid, template):
    new_grid = copy.deepcopy(grid)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if x == len(grid[0]) - 2 and y == len(grid) - 1:
                pass
            nw = get_at(x-1, y-1, grid)
            n  = get_at(x,   y-1, grid)
            ne = get_at(x+1, y-1, grid)
            cw = get_at(x-1, y,   grid)
            c  = get_at(x,   y,   grid)
            ce = get_at(x+1, y,   grid)            
            sw = get_at(x-1, y+1, grid)
            s  = get_at(x,   y+1, grid)
            se = get_at(x+1, y+1, grid)
            index = 0 + (
                (se << 0) + (s << 1) + (sw << 2) +
                (ce << 3) + (c << 4) + (cw << 5) +
                (ne << 6) + (n << 7) + (nw << 8))
            new_grid[y][x] = template[index]
    return new_grid

            


def main(inp):
    global round_num
    lines = inp.splitlines()
    template = lines[0]
    grid = [[0 if c == '.' else 1 for c in x] for x in lines[2:]]
    template = [0 if c == '.' else 1 for c in template]
    grid = expand_grid(grid)


    #print_grid(grid)        
    for r in range(50):
        print(r)
        round_num = r % 2

        grid = expand_grid(grid)
        grid = round(grid, template)
        #print_grid(grid)
        #print()
        #print()
    total = sum([sum(row) for row in grid])
    print(total)

def runme():
    #z=input1
    z=open("p20.input").read()
    start=time.time()
    main(z)
    print(f"Time: {time.time() - start}")


runme()