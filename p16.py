import time
import functools
input1 = """D2FE28"""
input2 = "38006F45291200"
input3 = "EE00D40C823060"
part1 = True

PKT_TYPE_LITERAL=4

PKT_LEN_BITS = "bits"
PKT_LEN_PKTS = "pkts"
PKT_LIT = "lit"

class Packet:
    def __init__(self, version, type):
        self.version = version
        self.type = type
        self.children = []
        self.value = None
    def __repr__(self):
        return f"(version: {self.version} type: {self.type} value:{self.value} children:{self.children})"

    

class BinaryReader:
    def __init__(self, s):
        self.string = s        
        self.byte_offset = -2
        self.bit_offset = 7
        self.counter = 0

    def move_next_bit(self):
        self.bit_offset += 1
        if self.bit_offset >= 8:
            self.bit_offset = 0
            self.byte_offset += 2
            if self.byte_offset >= len(self.string):
                return False
            self.current_byte = int(self.string[self.byte_offset:self.byte_offset+2],16)

        return self.byte_offset < len(self.string)

    def peek_bit(self):
        mask = (1 << (7-self.bit_offset))
        bit_value = self.current_byte & mask
        if (self.current_byte & bit_value) != 0:
            return 1
        return 0

    def read_next_bit(self):
        self.counter += 1
        self.move_next_bit()
        return self.peek_bit()
    
    def read_version(self):
        return self.read_nbit_int(3)
    
    def read_nbit_int(self, n):
        value = 0
        for _ in range(n):
            value <<= 1
            value |= self.read_next_bit()
        return value

    def read_packet_type(self):
        return self.read_nbit_int(3)

    def read_literal_value_packet(self):
        value = 0

        n = self.read_next_bit()
        while True:
            part = self.read_nbit_int(4)
            value = value << 4
            value |= part
            if n == 0:
                break
            n = self.read_next_bit()

        return value

    def read_packet_len(self):
        mode = self.read_next_bit()
        if mode == 0:
            return (PKT_LEN_BITS, self.read_nbit_int(15))
        return (PKT_LEN_PKTS, self.read_nbit_int(11))

    def read_tree(self):
        v = self.read_version()
        mode = self.read_packet_type()
        p = Packet(v, mode)
        if mode == PKT_TYPE_LITERAL:            
            p.value = self.read_literal_value_packet()
            return p
            
        (mode, n) = self.read_packet_len()
        
        if mode == PKT_LEN_BITS:
            start_at = self.counter            
            while self.counter < start_at + n:                
                p.children.append(self.read_tree())
        else:
            for _ in range(n):
                p.children.append(self.read_tree())
        return p
            
            
        
def calc_version_sum(node:Packet):
    s = node.version
    for c in node.children:
        s += calc_version_sum(c)
    return s

def node_eval(node:Packet):
    if node.type == 4:
        return node.value
    values = [node_eval(child) for child in node.children]
    if node.type == 0:
        return sum(values)
    if node.type == 1:
        return functools.reduce(lambda x,y:x*y, values, 1)
    if node.type == 2:
        return functools.reduce(lambda x,y:min(x,y), values, values[0])
    if node.type == 3:
        return functools.reduce(lambda x,y:max(x,y), values, values[0])
    if node.type == 5:
        return 1 if values[0] > values[1] else 0
    if node.type == 6:
        return 1 if values[0] < values[1] else 0
    if node.type == 7:
        return 1 if values[0] == values[1] else 0
    

def main(s : str):
    lines = s.splitlines()
    br = BinaryReader(lines[0])
    #print(br.read_tree())
    root = br.read_tree()
    print(f"V: {calc_version_sum(root)}, E:{node_eval(root)}")

    

def runme():
    z=open("p16.input").read()
    #z=input3
    #z="A0016C880162017C3686B18A3D4780"
    #z="CE00C43D881120"
    start=time.time()
    main(z)
    print(f"Time: {time.time() - start}")


runme()
