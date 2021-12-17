import time
import random
input1 = """target area: x=20..30, y=-10..-5"""


part1 = True


def round(x1, x2, y1, y2, xv, yv):

    yvm = yv
    x=0
    y=0
    xr = range(x1, x2+1)
    yr = range(y2, y1-1,-1)
    assert y1 < 0
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

    print(round(x1, x2, y1, y2, 7, 0))
    #rounds = 10000
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
    #xr = range(x1, x2+1)
    #yr = range(y1, y2+1)
    
        

    

def runme():
    z=open("p17.input").read()
    #z=input1
    start=time.time()
    main(z)
    print(f"Time: {time.time() - start}")


runme()
