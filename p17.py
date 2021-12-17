import time
import random
input1 = """target area: x=20..30, y=-10..-5"""
pos="""
23,-10  25,-9   27,-5   29,-6   22,-6   21,-7   9,0     27,-7   24,-5
25,-7   26,-6   25,-5   6,8     11,-2   20,-5   29,-10  6,3     28,-7
8,0     30,-6   29,-8   20,-10  6,7     6,4     6,1     14,-4   21,-6
26,-10  7,-1    7,7     8,-1    21,-9   6,2     20,-7   30,-10  14,-3
20,-8   13,-2   7,3     28,-8   29,-9   15,-3   22,-5   26,-8   25,-8
25,-6   15,-4   9,-2    15,-2   12,-2   28,-9   12,-3   24,-6   23,-7
25,-10  7,8     11,-3   26,-7   7,1     23,-9   6,0     22,-10  27,-6
8,1     22,-8   13,-4   7,6     28,-6   11,-4   12,-4   26,-9   7,4
24,-10  23,-8   30,-8   7,0     9,-1    10,-1   26,-5   22,-9   6,5
7,5     23,-6   28,-10  10,-2   11,-1   20,-9   14,-2   29,-7   13,-3
23,-5   24,-8   27,-9   30,-7   28,-5   21,-10  7,9     6,6     21,-5
27,-10  7,2     30,-9   21,-8   22,-7   24,-9   20,-6   6,9     29,-5
8,-2    27,-8   30,-5   24,-7
"""


part1 = True


def round(x1, x2, y1, y2, xv, yv):
    yv0=yv
    yvm = yv * (yv + 1) // 2
    x=0
    y=0
    xr = range(x1, x2+1)
    yr = range(y2, y1-1,-1)
    
    turns_to_y0 = 0 if yv == 0 else yv * 2 + 1
    turns_to_vx0 = abs(xv)

    if False  and turns_to_y0  and yv > 0 and turns_to_y0 > turns_to_vx0:
        #turns_to_slide = min(turns_to_y0, turns_to_vx0)
        #delta = turns_to_vx0 * (turns_to_vx0 + 1) // 2
      
        x = turns_to_vx0 * (turns_to_vx0 + 1) // 2
        if xv < 0:
            x *= -1
        xv = 0
        yv = -yv0-1
        y = 0

        



    while x < x2 and y > y1:

        yvm = max(y, yvm)
        x += xv
        y += yv
        if x == 28:
            x = x
        if x in xr and y in yr:
            return yvm

        if xv != 0:
            if xv > 0:                
                xv -= 1
            else:
                xv += 1

        yv -= 1
    return None







def main(s : str):
    _, xy = s.split(": ")
    tx, ty = xy.split(", ")
    x1, x2 = map(int, tx[2:].split(".."))
    y1, y2 = map(int, ty[2:].split(".."))

    dx = x2-x1+1
    best = None

    #print(round(x1, x2, y1, y2, 6, 3))
    res = []
    for p in pos.splitlines():
        res += list(tuple(map(int, x.split(","))) for x in p.split(" ") if x != "")
    
    #print(round(x1, x2, y1, y2, 6, 6))
    
    total = set()
    for xv in range(-500, 500):
        if xv % 25 == 0:
            print(xv)
        for yv in range(-500, 500):
            cur = round(x1, x2, y1, y2, xv, yv)
            if not best or (cur and cur > best):
                best = cur
            if cur is not None:
                total.add((xv,yv))
    print(best, len(total))


    

def runme():
    z=open("p17.input").read()
    #z=input1
    start=time.time()
    main(z)
    print(f"Time: {time.time() - start}")


runme()
