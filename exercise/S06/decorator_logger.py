import time


def logger(fn):
    def inner(*args):
        out = time.time() + fn.__name__ + fn(*args)
        return out
    return inner


@logger
def getlog(s):
    return s

print(getlog("a"))