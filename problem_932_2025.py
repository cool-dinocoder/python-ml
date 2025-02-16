import math

def is2025(n):
    d = len(str(n))
    for i in range(1,d):
        n1 = int(str(n)[:i])
        n2 = int(str(n)[i:])
        if n2==0:
            return False
        if (n1+n2)**2 == int(str(n1)+str(n2)):
            return True
    return False

def t(n):
    ans=0
    for i in range(1,int(math.sqrt(-1+10**n))+1):
        if is2025(i*i):
            ans+=i*i
            print(i*i)
    return ans

if __name__ == "__main__":
    n=16
    print(t(n))