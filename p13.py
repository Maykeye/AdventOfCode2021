import time
input1 = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


part1 = False


def main(s : str):
    dots_part,fold_part = s.split("\n\n")
    dots = [tuple(map(int, line.split(","))) for line in dots_part.splitlines()]                
    folds = [line[line.find('=')-1:].split("=") for line in fold_part.splitlines()]    
    folds = [(pair[0], int(pair[1])) for pair in folds ]
    
    width = max(x for (x,y) in dots)+1
    height = max(y for (x,y) in dots)+1
    print(width, height)

    paper = [['.' if (x,y) not in dots else '#' for x in range(width)] for y in range(height)]

    for fold in folds:
        print(fold)

        if fold[0] == 'y':
            fold_coord = fold[1]
            for y in range(fold_coord+1, height):
                distance_to_fold = y - fold_coord
                mapped_to = fold_coord - distance_to_fold
                assert mapped_to >= 0, "shifting rows nyi"
                for x in range(width):
                    if '#' in [paper[y][x], paper[mapped_to][x]]:
                        paper[mapped_to][x] = '#'

            height = fold_coord 
            paper = paper[:height]
            
        elif fold[0] == 'x':
            fold_coord = fold[1]
            for x in range(fold_coord+1, width):
                distance_to_fold = x - fold_coord
                mapped_to = fold_coord - distance_to_fold
                assert mapped_to >= 0, "shifting cols nyi"
                for y in range(height):
                    if '#' in (paper[y][x], paper[y][mapped_to]):
                        paper[y][mapped_to] = '#'

            width = fold_coord 
            paper = [row[:width] for row in paper]
        if part1:
            break
    
    total = 0
    for row in paper:
        print("".join(row))
        total += sum(1 for cell in row if cell == '#')
    print(total)

  


def runme():
    #z=open("p13.input").read()
    z=input1
    start=time.time()
    main(z)
    print(f"Time: {time.time() - start}")
    #main(input1)
    #main(input2)
    #main(input3)

runme()
