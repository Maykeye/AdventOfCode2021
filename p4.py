inp="""7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

class Board:
    def __init__(self):
        self.rows = []        

    def add_row(self, row:str):
        nums = map(int, row.split())
        self.rows.append(list(nums))

    def mark(self, n):
        for row in self.rows:
            for i in range(5):
                if row[i] == n:
                    row[i] = -n
        
        return self.win_h() or self.win_v()

    def win_h(self):
        for row in self.rows:
            n = sum(1 for value in row if value < 1)
            if n == 5:
                return True
        return False
    
    def win_v(self):
        for col in range(5):            
            n = sum(1 for row in self.rows if row[col] < 0)
            if n == 5:
                return True
        return False

    def score(self):
        s = 0
        for row in self.rows:
            s += sum(v for v in row if v > 0)
        return s




def main(inp):
    lines = inp.splitlines()    
    rng = list(map(int, lines[0].split(",")))
    row = 2

    boards = []    
    while row < len(lines):
        b = Board()
        boards.append(b)
        for _ in range(5):
            b.add_row(lines[row])
            row += 1
        row += 1
    
    for r in rng:
        for b in boards:
            if b.mark(r):
                print(b.score() * r)
                return

    
main(open("p4.input").read())
#main(inp)