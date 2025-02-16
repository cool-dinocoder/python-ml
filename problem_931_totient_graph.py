import math
from sympy import sieve,primerange
from sympy.functions.combinatorial.numbers import primepi
from math import log
from prime_util import primesum, pi

MOD = 715827883
def generate_prime(n):
    primes = []
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
def prime_factorize(n,primes):
    prime_factors = {}
    for prime in primes:
        if prime> n:
            break
        num = n
        while n % prime == 0:
            n //= prime
            if prime in prime_factors:
                prime_factors[prime] += 1
            else:
                prime_factors[prime] = 1
        n=num
    return prime_factors
    
def t(n,primes):
    a = prime_factorize(n,primes)
    ans=0
    for prime,power in a.items():
        ans+= int((n-(n/prime) - n/(prime**power)))
    return ans

def T(n,primes):
    ans=0
    for i in range(1,n+1):
        print(i,prime_factorize(i,primes))
        ans+=t(i,primes)
    return ans

def T_(n,primes):
    ans=0
    for prime in primes:
        if prime>n:
            break
        p= prime
        ind_sum =0
        while p<=n:
            x=n//p
            ind_sum += (x*(x+1))//2
            p=p*prime
        x=n//prime
        ans += (ind_sum*(prime-1))-(x*(x+1))//2
    return ans

def prime_sum(n):
    n= pi(n)
    s = 0.5*(n*n)*(log(n)+log(log(n))-(3/2))#+(log(log(n))-5/2)/(log(n)))
    return s
def T_large(n,p,s):
    ans = 0
    for m in range(1,10):
        n1 = (n)//m
        n2 = (n)//(m+1)
        print(m,n1,n2)
        primes =pi(n1)-pi(n2)
        prime_add = primesum(n1)-primesum(n2)
        # primes = pi(n1)-pi(n2)
        x= ((prime_add-2*primes)*(m)*(m+1))//2
        print(primes,prime_add,x)
        ans+=x
        # ans=ans%MOD
    return ans

def get_p_s(n):
    p= [0]
    s=[0]
    for i in range(1,10+1):
        m= n//i
        p.append(pi(m))
        s.append(primesum(m))
        # print(i,p[i],s[i])
    print("pi:",len(p),"s:",len(s))
    return p,s



#10**6->1055140129542
#10**8->11982909703689609
# d= {10**6:37550402023,10**7:3203324994356,10**8:279209790387276}
        
if __name__ == '__main__':
    
    n=10**2
    primes = list(primerange(n))
    # print(pi(n))
    # # print(len(primes))
    # # print(prime_factorize(n,primes))
    p,s = get_p_s(n)
    print(T_(10,primes))
    print(T_large(n,p,s))
    # # n=10**8
  
    # print((324017779+11982909703689609)%MOD)