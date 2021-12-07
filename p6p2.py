input1="3,4,3,1,2"

def main(inp):
    arr = list(map(int,inp.strip().split(",")))
    
    fish = [0 for _ in range(9)]

    for v in arr:
        fish[v] += 1

    print(fish, sum(fish))
    print()
    for x in range(256):
        respawn = fish[0]
        fish[0:8] = fish[1:9]
        fish[6] += respawn
        fish[8] = respawn

        print(fish, sum(fish))
        
    print(sum(fish))

    #for x in range(256):
    #    print(x)
    #    l = []        
    #    for i in range(len(arr)):
    #        if arr[i] == 0: 
    #            arr[i] = 6
    #            l.append(8)
    #        else:
    #            arr[i] -= 1
    #    arr += l
    #print("---")
    #print(len(arr))  
        

#main(input1)
main(open("p6.input").read())