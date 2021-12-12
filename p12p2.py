input1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
input2="""dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""
input3="""fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""


def visit(edges, current_node, path_so_far, all_paths, small_visited):
    if current_node == "end": 
        #all_paths.append([x for x in path_so_far])
        all_paths.append(1)
        return

    for next_node in edges[current_node]:
        new_small_visited = False

        if next_node.islower():
            if next_node == "start":
                continue
            if next_node in path_so_far and small_visited:              
                continue
            if next_node in path_so_far and not small_visited:
                new_small_visited = True
                small_visited = next_node            
            
        visit(edges, next_node, path_so_far+[next_node], all_paths, small_visited)
        if new_small_visited:
            small_visited = ""        
    
    

def main(s : str):
    edges = {}
    for l in s.splitlines():
        lhs, rhs = l.split('-')
        if lhs not in edges: edges[lhs] = []
        if rhs not in edges: edges[rhs] = []
        edges[lhs].append(rhs)
        edges[rhs].append(lhs)
    
    all_paths = []
    visit(edges, "start", ["start"], all_paths, "")
    print(len(all_paths))


main(open("p12.input").read())
#main(input1)
#main(input2)
#main(input3)
