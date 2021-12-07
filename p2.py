input1 = """
forward 5
down 5
forward 8
up 3
down 8
forward 2"""

def main(inp:str):
    h,v=0,0
    aim=0
    for lin in inp.strip().splitlines():
        (cmd, qty) = lin.split()
        qty = int(qty)

        if cmd == "forward":
            h += qty
            v += aim * qty
        if cmd == "up":
            aim -= qty
        if cmd == "down":
            aim += qty

    print(f"h{h} v{v}=>{h*v}")

    
    pass 

#main(input1)
main(open("p2.input").read())