def initial_state():
    return (8, 0, 0)


def is_goal(s):
    a, b, c = s
    return a == 4 and b == 4


def successors(s):
    x, y, z = s
    # Pouring from x
    if x > 0:
        # x to y
        t = 5 - y
        if t > 0:
            yield (max(0, x - t), y + min(x, t), z), min(x, t)
        # x to z
        t = 3 - z
        if t > 0:
            yield (max(0, x - t), y, z + min(x, t)), min(x, t)

    # Pouring from y
    if y > 0:
        # y to x
        t = 8 - x
        if t > 0:
            yield (x + min(y, t), max(0, y - t), z), min(y, t)
        # y to z
        t = 3 - z
        if t > 0:
            yield (x, max(0, y - t), z + min(y, t)), min(y, t)

    # Pouring from z
    if z > 0:
        # z to x
        t = 8 - x
        if t > 0:
            yield (x + min(z, t), y, max(0, z - t)), min(z, t)
        # z to y
        t = 5 - y
        if t > 0:
            yield (x, y + min(z, t), max(0, z - t)), min(z, t)
    return []
