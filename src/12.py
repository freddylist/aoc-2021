import collections
import inputs

START = "start"
END = "end"

NO_REVISITS = { START, END }

input = inputs.get(12)

# input = """start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end"""

# input = """dc-end
# HN-start
# start-kj
# dc-start
# dc-HN
# LN-dc
# HN-end
# kj-sa
# kj-HN
# kj-dc"""

# input = """fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW"""

graph = collections.defaultdict(set)

for a, b in (line.split("-") for line in input.split("\n")):
    graph[a].add(b)
    graph[b].add(a)

def count_paths(graph, source, target, revisit=False, visited=None, revisited=None):
    if visited is None:
        visited = set()

    if source == target:
        return 1

    if source in visited: 
        if revisit and not revisited and source not in NO_REVISITS:
            revisited = source
        else:
            return 0

    if source.islower():
        visited.add(source)

    paths_count = sum(
        count_paths(graph, v, target, revisit, visited, revisited) for v in graph[source]
    )

    if revisited != source:
        visited.discard(source)

    return paths_count

##########
# Part 1 #
##########

print(count_paths(graph, START, END, False))

##########
# Part 2 #
##########

print(count_paths(graph, START, END, True))
