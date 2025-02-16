import subprocess

def primesum(x):
    # Call the primesum executable
    result = subprocess.run(["./primesum.exe", str(x)], capture_output=True, text=True)
    
    # Parse the output
    primesum = result.stdout

    return int(primesum)
    # return result,""

def pi(x):
    # Calculate the value of pi using the prime number theorem
    result = subprocess.run(["./primecount.exe", str(x)], capture_output=True, text=True)
    
    # Parse the output
    primecount = int(result.stdout)

    return primecount

if __name__ == "__main__":
    # Example usage
    x = 10**12

    pi_x = pi(x)
    psum = primesum(x)
    print("Sum of primes ≤ : ",psum)
    print("Number of primes ≤  ",pi_x)
