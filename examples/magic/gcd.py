def gcd(a: int, b: int) -> bool:
    while a != b:
        if a < b:
            b -= a
        else:
            a -= b
    return a