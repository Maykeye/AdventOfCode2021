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
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

def main(s : str):
    score = 0
    part2=[]
    for line in s.splitlines():
        expect = []
        for ch in line:
            if ch == '[': expect.append(']')
            if ch == '<': expect.append('>')
            if ch == '{': expect.append('}')
            if ch == '(': expect.append(')')            
            if ch in '])}>':
                expected = expect.pop()
                if ch != expected:
                    score += scores[ch]

                    break
                
        
            
    print(score)

main(open("p10.input").read())
#main(input1)    