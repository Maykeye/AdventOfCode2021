input1="16,1,2,0,4,2,7,1,2,14"

def calc_cost(pos, target):
    cost = sum(abs(target - x) for x in pos)
    return cost

def main(inp:str):
    pos = list(map(int, inp.split(",")))
    x1,x2 = min(pos), max(pos)

    best_pos = x1
    best_cost = sum(pos)
    for x in range(x1, x2+1):
        current = calc_cost(pos, x)
        if current < best_cost:
            best_cost = current
            best_pos = x
    print(best_pos, best_cost)



#main(input1)
main(open("p7.input").read())