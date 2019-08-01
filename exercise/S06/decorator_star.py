def star(fa):
    def inner(*args):
        out = "*" + fa(*args) + "*"
        return out

    return inner


@star
def echo():
    return "salam"


val = echo()
print(val)