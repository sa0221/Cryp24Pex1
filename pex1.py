import math
import time 
import random
from math import sqrt

#Documentation:
# I used Geeks4Geeks to help me with formatting time so that only 4 decimals showed
# I used Geeks4Geeks in the part of my Pollard's Rho Algorithm, specifically in figuring out when to exit the while loop
# I used ChatGPT to build the gcd function
# I also used ChatGPT for the formatting of my Pollard's Rho Algorithm
# I also used ChatGPT to help build strategies for mmy Brute Force
# I used stackOverflow to help refresh me on how to print strings in the correct format
# I found a git repo online that contained a list of 1 million primes https://github.com/srmalins/primelists/blob/master/100000primes/primes.0000#L2 and used it to generate my factor bases
# I got my entire Dixon's Algorithm from Geeks4Geeks and modified it slightly 
# I used scipython.com to help me remember how to split lines from a file in python
# Chat GPT Convo:  https://chat.openai.com/share/124ebb48-c824-4328-a298-b8fbd4b0d4b3
# I asked Chat GPT a lot about Dixon's but didn't implement any of it
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def BruteForce(num):
    print("Brute Force Factoring-")
    x = 1
    start_time = time.time()
    if(num%2!=0):
        while(x<=math.sqrt(num)):
            end_time = time.time()
            if((end_time - start_time) > 120):
                print("Time Limit Exceeded.\n")
                return
            if(num % x == 0 and x!=1):
                end_time = time.time()
                total_time = "{:.4f}".format(end_time-start_time)
                print("Found a factor = {0}\n".format(x))
                print("It took {0} seconds\n".format(total_time))
                return 0
            x+=2                
    elif(num%2==0):
        end_time = time.time()
        total_time = "{:.4f}".format(end_time-start_time)
        print("Found a factor = {0}".format(2))
        print("It took {0} seconds\n".format(total_time))
        return 0
    else:
        end_time = time.time()
        total_time = "{:.4f}".format(end_time-start_time)
        print("Found a factor = {0}".format(num))
        print("It took {0} seconds\n".format(total_time))
        return
    
def PolRho(num):
    print("Pollard's Rho Factoring-")
    def f(x):
        return (math.pow(x,2)+1)%num
    start_time = time.time()
    if(num == 1):
        return 1
    if(num%2 == 0):
        return 2
    a = random.randint(1,num-1)
    b = random.randint(1,num-1)
    d = 1
    count = 0
    
    while(d==1):
        end_time = time.time()
        if((end_time-start_time)>120):
            print("Time Limit Exceeded.")
            return
        a = f(a)
        b = f(f(b))
        d = gcd(abs(a-b),num)
        if(d==num):
            count+=1
        if(count == 3):
            break
        
    end_time = time.time()
    total_time = "{:.4f}".format(end_time-start_time)
    print("Found a factor = {0}".format(d))
    print("a = {0}, b = {1}".format(a,b))
    print("It took {0} seconds\n".format(total_time))
    return

#https://www.geeksforgeeks.org/dixons-factorization-method-with-implementation/
def Dixon(num):
    print("Dixon's Algorithm-")
    f_base = int(input("Enter # of factors in factor base: "))
    base = []
    k = 0
    
    start_time = time.time()
    primes = open('primes.txt','r')
    content = primes.readlines()
    
    for line in content:
        data = line.split('\n')
        if(k<=f_base):
            base.append(int(data[0]))
        k=k+1
    print("Done generating factor base.")
    # Starting from the ceil of the root
    # of the given number N
    start = int(sqrt(num))
 
    # Storing the related squares
    pairs = []
 
    # For every number from the square root 
    # Till N
    for i in range(start, num): 
        # Finding the related squares
        end_time = time.time()
        if((end_time-start_time)>120):
            print("Time exceeded.")
            return 
        for j in range(len(base)):
            if((end_time-start_time)>120):
                print("Time exceeded.")
                return 
            lhs = i**2 % num
            rhs = base[j]**2 % num
             
            # If the two numbers are the 
            # related squares, then append
            # them to the array 
            if(lhs == rhs):
                pairs.append([i, base[j]])
 
    new = []
 
    # For every pair in the array, compute the 
    # GCD such that 
    for i in range(len(pairs)):
        if((end_time-start_time)>120):
            print("Time exceeded.")
            return 
        factor = gcd(pairs[i][0] - pairs[i][1], num)         
        # If we find a factor other than 1, then 
        # appending it to the final factor array
        if(factor != 1):
            new.append(factor)
 
    x = list(set(new))
    end_time = time.time()
    print("Found a Factor: {0}".format(x[0]))
    print("It took {0} seconds".format(end_time-start_time))
    # Returning the unique factors in the array
    return     

print("PEX1 - Factoring! - by Cadet Akolo\nCyS 431\n")
usernum = int(input("Enter a number to factor: "))
print("\n")
BruteForce(usernum)
PolRho(usernum)
Dixon(usernum)


