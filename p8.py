input1 = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


def find_all_of_len(arr, n):
    return [x for x in arr if len(x) == n]


def find_match(arr, n, pattern, expected_unknowns=0):
    res = [
        probe
        for probe in find_all_of_len(arr, n)
        if sum(1 for x in probe if x not in pattern) == expected_unknowns
    ]
    return res

def diffstr(a, b):
    return "".join(set(a).difference(b))


def main(inp: str):
    total_n = 0
    sum_n = 0
    inp = inp.strip()
    for line in inp.splitlines():
        #print("XXX", line)
        lhs, rhs = line.split("|")
        lhs = lhs.strip()
        rhs = rhs.strip()

        arr = lhs.split()
        


        # step 1: find C F
        digit_1 = find_all_of_len(arr, 2)[0]
        seg_cf = digit_1

        # find 7
        digit_7 = find_match(arr, 3, digit_1, 1)[0]
        seg_a = diffstr(digit_7, digit_1)
        digit_4 = find_match(arr, 4, digit_1, 2)[0]
        seg_bd = diffstr(digit_4, digit_1)

        # len 5 = 2, 5, 3
        # 2 : A   c? d e    g
        # 3 : A   c? d   f? g
        # 5 : A b    d   f? g

        digs253 = find_all_of_len(arr, 5)
        if sum(1 for x in digs253 if seg_bd[0] in x) == 1: 
            seg_b, seg_d = seg_bd[0], seg_bd[1]
            seg_d = seg_bd[1]
        else:
            seg_d, seg_b = seg_bd[0], seg_bd[1]

        # A B c D e f g | 1 7 4
        digit_5 = [x for x in digs253 if seg_b in x][0]
        # 5 : A B D   f? g
        if seg_cf[0] in digit_5:
            seg_f, seg_c = seg_cf[0], seg_cf[1]        
        else:
            seg_f, seg_c = seg_cf[1], seg_cf[0]
        
        # A B C D e F g 
        # 2 : A   C D e   g
        # 3 : A   C D   F g
        # 5 : A B   D   F g
        seg_g = diffstr(digit_5, seg_a+seg_b+seg_d+seg_f)
        digit_3 = [x for x in digs253 if x != digit_5 and seg_f in x][0]
        digit_2 = [x for x in digs253 if x not in (digit_5, digit_3)][0]
        
        digit_8 = find_all_of_len(arr, 7)[0]
        
        seg_e = diffstr(digit_2, seg_a + seg_c + seg_d + seg_g)
        digit_6 = find_match(arr, 6, seg_a+seg_b+seg_d+seg_e+seg_f+seg_g)[0]
        digit_9 = find_match(arr, 6, seg_a+seg_b+seg_d+seg_c+seg_f+seg_g)[0]
        digit_0 = find_match(arr, 6, seg_a + seg_b + seg_c + seg_e + seg_f + seg_g)[0]
        
        numbers = [digit_0, digit_1, digit_2,digit_3, digit_4, digit_5, digit_6, digit_7, digit_8, digit_9]
        numbers = list(map(sorted, numbers))
            
        s = ""
        for r in rhs.split():
            r = sorted(r)
            r = numbers.index(r)
            if r in (1,4,7,8):
                total_n += 1
            s += str(r)
        sum_n += int(s)
    print(total_n, sum_n)
    
    



#main("fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg")
#main(input1)
main(open("p8.input").read())
