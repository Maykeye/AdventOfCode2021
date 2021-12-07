input1="3,4,3,1,2"

def main(inp):
    arr = list(map(int,inp.strip().split(",")))

    for x in range(80):
        print(x)
        l = []        
        for i in range(len(arr)):
            if arr[i] == 0: 
                arr[i] = 6
                l.append(8)
            else:
                arr[i] -= 1
        arr += l
    print("---")
    print(len(arr))  
        

#main(input1)
main(open("p6.input").read())