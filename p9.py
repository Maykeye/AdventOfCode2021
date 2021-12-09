input1 = """2199943210
3987894921
9856789892
8767896789
9899965678"""

def is_lower_than_adjecent(grid, current_risk, y, x):
    if y < 0 or y >= len(grid):
        return True
    if x < 0 or x >= len(grid[0]):
        return True 
    adjecent = grid[y][x]
    return current_risk < adjecent

def main(s : str):
    grid = s.splitlines()

    risk_level = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
        
            is_lower_than_all = True
            current = grid[y][x]
            is_lower_than_all = is_lower_than_all and is_lower_than_adjecent(grid, current, y, x-1)
            is_lower_than_all = is_lower_than_all and is_lower_than_adjecent(grid, current, y, x+1)
            is_lower_than_all = is_lower_than_all and is_lower_than_adjecent(grid, current, y-1, x)
            is_lower_than_all = is_lower_than_all and is_lower_than_adjecent(grid, current, y+1, x)
            if is_lower_than_all:
                risk_level += 1 + int(current)
    print(risk_level)
                

        




#main(input1)
main(open("p9.input").read())

