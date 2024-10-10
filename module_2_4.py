numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes=[]
non_primes=[]
for i in range(1,len(numbers)) :
 #   is_prime=True
    for ii in range(1,i):
        is_prime = numbers[i]%numbers[ii]!=0
        if not is_prime :
            non_primes.append(numbers[i])
            break
    else:
        primes.append(numbers[i])
print(primes)
print(non_primes)


