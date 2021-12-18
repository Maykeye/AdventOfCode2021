import sys
import math
import time
import random

input1 = """\
[1,1]
[2,2]
[3,3]
[4,4]
"""
input2="""\
[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]
"""
input3="""\
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]    
"""

class Explode:
    def __init__(self):
        self.path = []
        self.path_to_int = []
        self.replacing_left = True
        self.entered_list = []
        self.replacing_right = False
        self.right_add = 0
        self.just_replaced = None
        self.just_replaced_idx =0 
        
        

    def enter(self, node):
        if type(node) == int:
            self.path_to_int = self.path[-1]
            if self.replacing_right:
                if type(self.path_to_int[0]) == int:
                    if self.just_replaced_idx != 0 or self.path_to_int is not self.just_replaced:
                        self.path_to_int[0] += self.right_add
                        self.replacing_right = False
            if self.replacing_right:
                if type(self.path_to_int[1]) == int:
                    if self.just_replaced_idx != 1 or self.path_to_int is not self.just_replaced:
                        self.path_to_int[1] += self.right_add
                        self.replacing_right = False

        
        self.entered_list.append(type(node) == list)
        if type(node) == list:
            if len(self.path) == 4 and self.replacing_left:                
                self.replacing_left = False
                self.entered_list[-1] = False
                lhs, rhs = node
                if self.path_to_int:
                    if type(self.path_to_int[1]) == int:                        
                        self.path_to_int[1] += lhs                  
                    else:
                        self.path_to_int[0] += lhs

                self.just_replaced_idx = 0 if self.path[-1][0] is node else 1

                self.right_add = rhs       
                self.replacing_right = True 
                self.just_replaced = self.path[-1]       

                return 0

            self.path.append(node)

    def leave(self, node):        
        if self.entered_list.pop():
            self.path.pop()
        
class Split:
    def __init__(self):
        self.done = False 
    def enter(self, node):
        if type(node) == int:
            if node >= 10 and not self.done:
                self.done = True
                return self.split(node)

    def leave(self,node):
        pass
    
    def split(self, n):
        return [math.floor(n/2), math.ceil(n/2)]




def traverse(numbers, callback):
    res = callback.enter(numbers)
    if res is not None:
        callback.leave(res)
        return res
    if type(numbers) == list:
        for i in range(len(numbers)):
            res = traverse(numbers[i], callback)
            if res is not None:
                numbers[i] = res
    return callback.leave(numbers)


def do_explode(nums):
    exp = Explode()
    #print("T0", nums)
    traverse(nums, exp)
    #print("T1", nums)        
    return nums



def test(start, end):
    do_explode(start) 
    if start != end:
        print(start)
        print(end)
        assert start == end
def test3(x, y, end):
    start = add(x,y)
    numreduce(start) 
    if start != end:
        print("GOT: ", start)
        print("EXP: ", end)
        assert start == end

def numreduce(z):
    verbose = False
    if verbose:
        print("ORIG", z)

    while True:
        old = repr(z)
        #if verbose:
        #    print("ORIG", z)
        do_explode(z)
        new = repr(z)
        if verbose:
            print("EXPL", z)
        if old != new:
            continue
        traverse(z, Split())
        new = repr(z)
        if verbose:        
            print("SPLT", z)
        if old == new:
            break
    
    #START:  [[[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]], [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]]
    #EXPECT: [[[[4, 0], [5, 4]], [[7, 7], [6,0]]],  [[8,[7,7]],[[7,9],[5,0]]]]
    #GOT:    [[[[4, 0], [5, 4]], [[7, 7], [8, 5]]], [[[5, 5], [5, 6]], [[7, 6], [7, 0]]]]

def add(x,y):
    return [x,y]

def magnitude(node):
    if type(node) == int:
        return node
    return 3 * magnitude(node[0]) + 2*magnitude(node[1])

def main(s : str):
    lines = [eval(x) for x in s.strip().splitlines()]    
    #z=[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
    #z=[[3,[2,[[7,3],1]]],[6,[5,[4,[3,2]]]]]
    if 0:
        test([[[[[9,8],1],2],3],4], [[[[0,9],2],3],4])
        test([7,[6,[5,[4,[3,2]]]]], [7,[6,[5,[7,0]]]])
        test([[6,[5,[4,[3,2]]]],1], [[6,[5,[7,0]]],3])
        test([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]], [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
        test([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]], [[3,[2,[8,0]]],[9,[5,[7,0]]]])         
        test([[[[4, 0], [5, 4]], [[7, 0], [[7, 8], 5]]], [10, [[11, 9], [11, 0]]]],
            [[[[4, 0], [5, 4]], [[7, 7], [0, 13]]], [10, [[11, 9], [11, 0]]]])
        test3([[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],
            [7,[[[3,7],[4,3]],[[6,3],[8,8]]]],
            [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]])
        
    if 0:
        test3(
            [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],
            [7,[[[3,7],[4,3]],[[6,3],[8,8]]]],
            [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
        )
        test3([[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]],
            [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]],
            [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]
        )
        test3([[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]],
            [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]],
            [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]
        )
        test3([[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]],
            [7,[5,[[3,8],[1,4]]]],
            [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]
        )
        test3([[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]],
            [[2,[2,2]],[8,[8,1]]],
            [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]
        )
        test3([[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]],
            [2,9],
            [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]
        )
        test3([[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]],
            [1,[[[9,3],9],[[9,0],[0,7]]]],
            [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]
        )
        test3( [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]],
            [[[5,[7,4]],7],1],
            [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]])
        test3([[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]],
            [[[[4,2],2],6],[8,7]],
            [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]])


    current = add(lines[0], lines[1])
    numreduce(current)
    print("start", current)
    lines = lines[2:]
    for line in lines:
        current = add(current, line)        
        numreduce(current)
    
    print("end  ", magnitude(current))
    
    

def runme():
    z=open("p18.input").read()
    #z=input3
    start=time.time()
    main(z)
    print(f"Time: {time.time() - start}")


runme()
