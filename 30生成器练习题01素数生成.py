def is_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):#浮点类型不能有指数
        if n % i == 0:
            return False
    return True


def premier(stop):  # 素数生成器
    n = 2
    while True:
        if is_premier(n):
            yield n
        n += 1
        if n==10:
            break


if __name__=="__main__":
    gen = premier(10)
try:
    while True:
        print(gen.__next__())
except Exception:
    pass




