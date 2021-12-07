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

def common_rare(lines, n):
    common = ""
    rare = ""

    bitpos = n
    freq={'0':0,'1':0}

    for line in lines:
        freq[line[bitpos]] += 1

    if freq['0'] > freq['1']:
        common += '0'
        rare += '1'
    else:
        common += '1'
        rare += '0'

    if freq['0'] == freq['1']:
        return '=', '='
            
    return common, rare

def run_filter(lines, bitpos, is_common:bool):
    if len(lines) == 1:
        return lines
    
    common, rare = common_rare(lines, bitpos)

    if common != '=':
        compare = common if is_common else rare
    else:
        compare = '1' if is_common else '0'
    lines = [l for l in lines if l[bitpos] == compare]
        

    return run_filter(lines, bitpos+1, is_common)

    


def main(inp:str):
    lines = inp.strip().splitlines()
    ox = int(run_filter(lines, 0, True)[0], 2)
    co = int(run_filter(lines, 0, False)[0], 2)
    print(ox, co, ox*co)
    


#main(inp)
main(open("p3.input").read())