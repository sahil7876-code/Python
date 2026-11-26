def decorate(n):
    def outer(fuct):
        def inner(**args):
            for i in range(n):
                print("Attempt", i+1)
                res = fuct(**args)
                print("Res", res)
            return res
        return inner
    return outer

@decorate(3)
def calc(num, nm):
    return num*nm
calc(num = 7,nm = 8)