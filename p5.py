input1="""0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

def main(inp):
    m = [[0 for x in range(1000)] for y in range(1000)]
    z = 0
    for line in inp.splitlines():
        l, r = line.split(" -> ")
        x1, y1 = l.split(",")
        x2, y2 = r.split(",")
        x1,x2,y1,y2=map(int, (x1,x2,y1,y2))

        xd = x2-x1
        yd = y2-y1

        if xd != 0:
            xd = xd // abs(xd)          
        if yd != 0:
            yd = yd // abs(yd)
        #if xd == 0 or yd == 0:
        if True:
            while True:
                m[y1][x1] += 1
                x1 += xd 
                y1 += yd
                if x1 == x2 and y1 == y2:
                    m[y1][x1] += 1
                    break

    d = sum(sum(1 for v in row if v >= 2) for row in m)
    print(d)        

#main(input1)
main(open("p5.input").read())