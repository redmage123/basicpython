def prime(n):
    if n == 0:
        return False
    if n == 1: 
        return False
    if n %2 == 0:
        return False

    if n // prime(n-1) == 1:
        return False
    else:
        return True



