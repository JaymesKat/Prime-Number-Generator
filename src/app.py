# this python function  returns a list containing sequence of prime numbers below the given argument
def prime_num_generator(end):
    noprimeNums = set(j for i in range(2, 8) for j in range(i*2, end, i))      
    primeNums = [x for x in range(2, end) if x not in noprimeNums]
    return primeNums

def is_prime(num):
     #Return true if *num* is prime.
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

       