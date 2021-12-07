input1="16,1,2,0,4,2,7,1,2,14"

def sum_upto(x):
    return x * (x+1) // 2

def calc_cost(pos, target):
    cost = sum( sum_upto(abs(target - x)) for x in pos)
    return cost

def main(inp:str):
    pos = list(map(int, inp.split(",")))

    
    x1,x2 = min(pos), max(pos)

    best_pos = x1
    best_cost = 1
    for x in range(x1, x2+1):        
        current = calc_cost(pos, x)
        if current < best_cost or x == x1:
            best_cost = current
            best_pos = x
    print(best_pos, best_cost)


#main(input1)
main(open("p7.input").read())