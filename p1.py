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
    arr = [arr[0]] + arr
    incr = 0
    for i in range(1, len(arr)):
        if int(arr[i]) > int(arr[i-1]):
            incr += 1

    print(incr)

input_file = open("p1.input").read()
main(input_file)

#main(input1)    