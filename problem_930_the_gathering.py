import math

ans=set()


def partition(number,a):
    if number < 0:
        return
    elif number == 0:
        ans.add(tuple(sorted(a)))
        return
    else:
        for i in range(1, number+1):
            a.append(i)
            partition(number - i,a)
            a.pop()


if __name__ == '__main__':
    pass