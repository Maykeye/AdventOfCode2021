input1 = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


scores = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4
}

def main(s : str):
    part2=[]
    line_scores = []
    for line in s.splitlines():
        expect = []
        good=True

        for ch in line:
            if ch == '[': expect.append(']')
            if ch == '<': expect.append('>')
            if ch == '{': expect.append('}')
            if ch == '(': expect.append(')')            
            if ch in '])}>':
                expected = expect.pop()
                if ch != expected:
                    good=False
                    break
        if good:
            score = 0
            while expect:
                n = expect.pop()
                score = score * 5 + scores[n]
                line += n
            line_scores.append(score)
    line_scores = list(sorted(line_scores))
    mid_point = len(line_scores)//2

    print(line_scores[mid_point])

    

main(open("p10.input").read())
#main("{")
#main("[({(<(())[]>[[{[]{<()<>>")
#main(input1)    