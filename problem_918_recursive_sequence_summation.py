import math

#S2n= 4- An
#A2n = 2An
#A2n+1 = An - 3An+1

dp = {1:1,2:2}
def A(n):
    if dp.get(n,-1)!=-1:
        return dp[n]
    if n%2 == 0:
        dp[n] = 2*A(n//2)
        return dp[n] 
    if n%2 == 1:
        dp[n] = A((n-1)//2) - 3*A((n+1)//2)
        return dp[n]

if __name__ == '__main__':
    print(4-A(1e12//2))