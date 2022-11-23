def systems(p,sys):
    i = 0
    p_sys = 0
    while p >= 1:
        p_sys += (p % sys) * (10**i)
        p = p // sys
        i += 1
    return p_sys

print(systems(12,2))