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


part1 = True


def main(s : str):
    lines = s.splitlines()
    polymer = list(lines[0])
    template = {}
    for line in lines[2:]:
        lhs, rhs = line.split(" -> ")
        template[tuple(lhs)]  = rhs
    
    for _ in range(10):
        new_polymer = []
        for j in range(len(polymer) - 1):
            key = polymer[j], polymer[j+1]
            value = template.get(key, None)
            if value:
                new_polymer.append(key[0])
                new_polymer.append(value)
            else:
                new_polymer.append(key[0])
        polymer = new_polymer + [polymer[-1]]
    
    count = {}
    for key in polymer:
        if key not in count:
            count[key] = 0
        count[key] += 1


    s = list(count.items())
    s = sorted(s, key=lambda x:x[1])

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
