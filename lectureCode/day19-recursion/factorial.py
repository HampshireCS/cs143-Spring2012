def factorial(n):
    if n <= 0 or int(n) != n:
        raise ValueError("factorial takes a positive integer")

    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


if __name__=="__main__":
    assert factorial(3) == 6
    assert factorial(1) == 1
    assert factorial(4) == 24
