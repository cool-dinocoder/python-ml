MOD = 10**9 + 7

n = 5
dp = [0] * (n + 1)
dp[0] = 1  # Base case

# prefix_odd[i] = sum of dp[j] for j <= i where j has the same parity as i (odd)
# prefix_even[i] = sum of dp[j] for j <= i where j has the same parity as i (even)
prefix_odd = [0] * (n + 1)
prefix_even = [0] * (n + 1)

# Initialize prefix sums for i=0 (even)
prefix_even[0] = dp[0]

for i in range(1, n + 1):
    # The sum of dp[i - k] for all odd k <= i is either prefix_even[i-1] or prefix_odd[i-1]
    if i % 2 == 1:
        # i is odd: previous parity must be even (i - k is even when k is odd)
        dp[i] = prefix_even[i - 1] % MOD
    else:
        # i is even: previous parity must be odd
        dp[i] = prefix_odd[i - 1] % MOD
    
    # Update prefix sums
    if i % 2 == 1:
        prefix_odd[i] = (prefix_odd[i - 1] + dp[i]) % MOD
        prefix_even[i] = prefix_even[i - 1]
    else:
        prefix_even[i] = (prefix_even[i - 1] + dp[i]) % MOD
        prefix_odd[i] = prefix_odd[i - 1]

print(dp[n] % MOD)