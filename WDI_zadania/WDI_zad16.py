def steps_to_one(q):
    steps = 0
    while q != 1:
        steps = steps + 1
    return steps


if __name__ == '__main__':
#    x = (a % 2) * (3 * a + 1) + (1 - a % 2) * (a/2)
    max_steps = 0
    max_steps_val = 1
    for x in range(2, 10001):
        s = steps_to_one(x)
        if s >= max_steps:
            max_steps = s
            max_steps_val = x
    print(max_steps_val)