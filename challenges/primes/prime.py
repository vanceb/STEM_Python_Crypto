from datetime import datetime

def prime1(count):
    primes = 1
    largestPrime = 2
    test = 3
    while primes < count:
        isPrime = True
        for i in range(2, test):
            if test % i == 0:
                isPrime = False
        if isPrime == True:
            primes += 1
            largestPrime = test
        test += 1
    return largestPrime

def prime2(count):
    primes = 1
    largestPrime = 2
    test = 3
    while primes < count:
        isPrime = True
        for i in range(2, test):
            if test % i == 0:
                isPrime = False
                break
        if isPrime == True:
            primes += 1
            largestPrime = test
        test += 2
    return largestPrime

def prime3(count):
    primes = [2]
    test = 3
    while len(primes) < count:
        isPrime = True
        for i in range(len(primes)):
#            if primes[i] > test/2:
#                break
            if test % primes[i] == 0:
                isPrime = False
                break
        if isPrime == True:
            primes.append(test)
        test += 2
    return primes[-1]

def prime4(count):
    primes = [2]
    test = 3
    maxDivisor = 2
    while len(primes) < count:
        isPrime = True
        for i in range(len(primes)):
            if primes[i] > maxDivisor:
                break
            if test % primes[i] == 0:
                isPrime = False
                break
        if isPrime == True:
            primes.append(test)
        test += 2
        maxDivisor = test/2
    return primes[-1]

def timeIt(function, count):
    start = datetime.now()
    result = function(count)
    stop = datetime.now()
    taken = (stop - start).total_seconds()
    return (taken, result)

if __name__ == '__main__':
    howMany = 1000
    print "Niaeve Prime Testing:"
    taken, result = timeIt(prime1, howMany)
    print str(result) +  " in " + str(taken) +" seconds"
    print "Fast Prime Testing:"
    taken, result = timeIt(prime2, howMany)
    print str(result) +  " in " + str(taken) +" seconds"
    print "Faster Prime Testing:"
    taken, result = timeIt(prime3, howMany)
    print str(result) +  " in " + str(taken) +" seconds"
    print "Fastest Prime Testing:"
    taken, result = timeIt(prime4, howMany)
    print str(result) +  " in " + str(taken) +" seconds"
