from itertools import islice

def sliding_window(iterable, size):
    it = iter(iterable)
    window = tuple(islice(it, size))

    if len(window) == size:
        yield window
    for x in it:
        window = window[1:] + (x,)
        
        yield window

def pairwise(iterable):
    return sliding_window(iterable, 2)

def deep_enumerate(iterable):
    for i, v in enumerate(iterable):
        try:
            for j, u in deep_enumerate(iter(v)):
                yield ((i,) + j, u)
        except TypeError:
            yield ((i,), v)

def in_bounds(array, indices):
    i = indices[0]
    valid = i >= 0 and i < len(array)

    if len(indices) > 1:
        valid = valid and in_bounds(array[i], indices[1:])

    return valid

inclusion = {
    dict: lambda d, k: k in d,
    list: lambda l, i: i >= 0 and i < len(l),
     set: lambda s, k: k in s,
}

def deep_in(collection, keys):
    k = keys[0]
    valid = inclusion[type(collection)](collection, k)

    if len(keys) > 1 and valid:
        return deep_in(collection, keys[1:])

    return valid
    
def deep_get(collection, keys):
    v = collection[keys[0]]

    if len(keys) > 1:
        return deep_get(v, keys[1:])

    return v

def deep_set(collection, keys, value):
    k = keys[0]

    if len(keys) > 1:
        return deep_set(collection[k], keys[1:], value)
    
    collection[k] = value

def deep_update(collection, keys, updater, default=None):
    value = updater(
        deep_get(collection, keys) if deep_in(collection, keys) else default
    ) 

    deep_set(collection, keys, value)

    return value

def surrounding(
    grid,
    position,
    radius=1,
    diagonals=False,
    include=False
):
    x = position[0]

    neighboring = range(max(0, x - radius), min(len(grid), x + radius + 1))

    if len(position) <= 1:
        return {(i,): grid[i] for i in neighboring if include or i != x}

    neighbors = {}

    for i in neighboring:
        s = surrounding(
            grid[i],
            position[1:],
            radius=radius if diagonals else radius - abs(i - x),
            diagonals=diagonals,
            include=include or i != x
        )

        for p, v in s.items():
            neighbors[(i,) + p] = v

    return neighbors

def flood_fill(grid, position, predicate, diagonals=False, visited=None):
    if visited is None:
        visited = {}
    
    if position in visited:
        return visited

    v = deep_get(grid, position)

    if not predicate(v):
        return visited

    visited[position] = v

    for n in surrounding(grid, position).keys():
        flood_fill(grid, n, predicate, diagonals, visited)

    return visited
