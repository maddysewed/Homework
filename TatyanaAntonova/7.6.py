def odd_primes(n):
    primes = list(range(2, n+1))
    for i in primes:
        j = 2
        while i*j <= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j = j + 1
    primes.remove(2)
    return primes

def goldbach_conj(n):
    x, y = 0, 0
    result = 0
    if n % 2 == 0:
        prime = odd_primes(n)
        while result != n:    
            for i in range(len(prime)):
                if result == n: break 
                x = prime[i]
                for j in range(len(prime)):
                    y = prime[j]
                    result = x + y
                    if result == n: break 
    return f"{x} + {y}" 

def main():
    while True:
        num = input()
        if num != "q":            
            if int(num) <= 4:
                raise ValueError("You have to input a number > 4")                
            if not isinstance(int(num), int):
                raise ValueError("Incorrect input")
            print(goldbach_conj(int(num)))
        else:
            break
        
if __name__ == "__main__":
    main()