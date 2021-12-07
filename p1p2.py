input1 = """
199
200
208
210
200
207
240
269
260
263"""


def main(s : str):
    s = s.strip()
    arr = s.splitlines()
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    incr = 0
    for i in range(1, len(arr)-2):
        prev = arr[i-1] + arr[i+0] + arr[i+1]
        now =  arr[i] + arr[i+1] + arr[i+2]
        if prev < now:
            incr += 1

    print(incr)

input_file = open("p1.input").read()
main(input_file)
#main(input1)    