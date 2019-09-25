def First_half(str):
    return str[:len(str)/2]
def without_end(str):
    return str[1:-1]
def combo_string(a, b):
    if len(a) > len(b):
        return b + a + b
        return a + b + a
def non_start(a, b):
    return a[1:] + b[1:]
def left2(str):
    return str[2:] + str[:2]
