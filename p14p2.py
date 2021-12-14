import time
input1 = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


part1 = False



def subround(lhs, rhs, n, template, depth, count_template, skip=False):

    if (lhs,rhs,depth, skip) in count_template:
        return count_template[(lhs,rhs,depth, skip)]
    
    if n == 0:        
        if skip:
            return {}
        return {lhs : 1}
    
    value = template.get((lhs, rhs), None)
    if not value:
        assert False

    lhs_count = subround(lhs, value, n-1, template, depth+1, count_template, skip=True)
    rhs_count = subround(value, rhs, n-1, template, depth+1, count_template)
    count={}
    if not skip:
        count[lhs] = 1    

    for cur in (lhs_count, rhs_count):
        for k,v in cur.items():
            if k not in count:
                count[k]=0
            count[k] += v
    count_template[(lhs,rhs,depth, skip)] = count
    return count
    


def main(s : str):
    lines = s.splitlines()
    polymer = list(lines[0])
    template = {}
    for line in lines[2:]:
        lhs, rhs = line.split(" -> ")
        template[tuple(lhs)]  = rhs

    count={}
    for i in range(len(polymer)-1):
        print(f"{i}/{len(polymer)-1}")
        round_count = subround(polymer[i], polymer[i+1], 40, template, 0, {})
        for k, v in round_count.items():
            if k not in count: 
                count[k]=0
            count[k] += v
        i=i
    rhs=polymer[-1]
    if rhs not in count:
        count[rhs]  = 0
    count[rhs] += 1

    s = list(count.items())
    s = sorted(s, key=lambda x:x[1])
    print(count)

    most_common = s[-1]
    least_common = s[0]
    print(most_common[1] - least_common[1])


def runme():
    z=open("p14.input").read()
    #z=input1
    start=time.time()
    main(z)
    print(f"Time: {time.time() - start}")
    #main(input1)
    #main(input2)
    #main(input3)

runme()
