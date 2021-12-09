input1 = """2199943210
3987894921
9856789892
8767896789
9899965678"""

def is_valid_pos(grid,y, x):
    if y < 0 or y >= len(grid):
        return False
    if x < 0 or x >= len(grid[0]):
        return False
    return True

def main(s : str):
    grid = s.splitlines()
    grid = [[x for x in row] for row in grid]
    print(grid)


    basins = []
    new_basin_found = False
    while True:
        for y in range(len(grid)):
            new_basin_found = False
            for x in range(len(grid[0])):

                if grid[y][x] == '9':
                    continue
                print(f"new basin at y={y} x={x}")
                basin_size = 0
                visited = set()
                to_visit = [(y,x)]

                while to_visit:                
                    next_pos = to_visit.pop()
                    if next_pos in visited:
                        continue
                    y, x = next_pos
                    visited.add(next_pos)                
                    if not is_valid_pos(grid, y, x):
                        continue         
                    if grid[y][x] in '9':
                        continue
                    basin_size += 1                
                    grid[y][x]='9'
                    to_visit.append((y-1,x))
                    to_visit.append((y+1,x))
                    to_visit.append((y,x-1))
                    to_visit.append((y,x+1))
                new_basin_found = True
                basins.append(basin_size)
                break
            if new_basin_found:
                break
        if not new_basin_found:
            break
                
    basins = list(sorted(basins))
    print(basins)
    print(basins[-1]*basins[-2]*basins[-3])


                    
                

        




#main(input1)
main(open("p9.input").read())

