input1 = """5877777777
8877777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777"""


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
    total_count = len(arr[0])**2
    current_step = 0
    while True:
        current_step+=1        
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

        if len(flashed_this_round) == total_count:
            break
    print(current_step)

    
        
    
    print(arr)

input_data = input1
input_data = open("p11.input").read()
#input_data=mini
main(input_data)


