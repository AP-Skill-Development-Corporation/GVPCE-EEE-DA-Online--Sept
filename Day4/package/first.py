# some functions
def factorial(n):
    fact=1
    if n<0:
        return -1
    elif n==0:
        return 0
    else:
        for dig in range(1,n+1):
            fact*=dig
    return fact
#factorial(5)
def is_prime(n):
    count=0
    if n==1:
        return 1
    else:
        for dig in range(1,n+1):
            if n%dig==0:
                count+=1
        if count==2:
            return True
        else:
            return False
# is_prime(val)

def is_even(n):
    if n>0:
        if n%2==0:
            return True
        else:return False
    else:
        return -1