def color():
    def sabz(fn):
        def inner(*args):
            out = "\033[31m" + fn(*args) + "\033[0m"
            return out
        return inner
    





@color('sabz')
def change(inpt):
    return inpt