input1 = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

mini="""11111
19991
19191
19991
11111"""

deltas = [
    (-1, -1),
    (-1,  0),
    (-1,  1),
    
    ( 0, -1),    
    ( 0,  1),

    ( 1, -1),
    ( 1,  0),
    ( 1,  1),    
]
def r(n):
    return "".join(map(lambda n: hex(n)[2:], n))

def main(s : str):
    arr = [[int(num) for num in item] for item in s.splitlines()]

    
    
    dim = range(len(arr))
    

    total_flashes=0
    for i in range(100):
        
        reflash_from = []
        visited = []
        flashed_this_round = set()
        for y in dim:
            for x in dim:
                arr[y][x] += 1
                if arr[y][x] > 9:                
                    reflash_from.append((y,x))
                    flashed_this_round.add((y,x))
        while reflash_from:
            (y,x) = reflash_from.pop()
            if (y,x) in visited:
                continue
            visited.append((y,x))
            if not y in dim:
                continue
            if not x in dim:
                continue    
            neighbours = [(dy+y, dx+x) for dy, dx in deltas if y+dy in dim and x+dx in dim]
            for ny, nx in neighbours:
                arr[ny][nx] += 1
                if arr[ny][nx] > 9:                
                    reflash_from.append((ny,nx))
                    flashed_this_round.add((ny,nx))


        for y in dim:
            for x in dim:
                if arr[y][x] > 9: 
                    arr[y][x] = 0

        total_flashes += len(flashed_this_round)
    print(total_flashes)

    
        
    
    print(arr)

input_data = input1
input_data = open("p11.input").read()
#input_data=mini
main(input_data)


