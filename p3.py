inp="""00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

def main(inp:str):

    inp = inp.strip()

    common = ""
    rare = ""


    lines=inp.splitlines()

    for bitpos in range(len(lines[0].strip())):
        freq={'0':0,'1':0}

        for line in lines:
            freq[line[bitpos]] += 1
        if freq['0'] > freq['1']:
            common += '0'
            rare += '1'
        else:
            common += '1'
            rare += '0'
            

    c = int(common,2)
    r = int(rare, 2)

    print(f"{c*r}")

#main(inp)
main(open("p3.input").read())