def sum_primes(number):
    result = 0
    for num in (2, number):
        is_prime = True
        if num == 17:
            continue
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
    
    if is_prime:
        result += num
        
