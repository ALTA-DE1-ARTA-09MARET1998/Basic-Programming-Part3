def prime_number(bilangan):
    if bilangan == 1:
        return False
    elif bilangan > 1:
        for i in range(2, bilangan):
            if (bilangan % i) == 0:
                return False
        else:
            return True
    else:
        return False

def full_prima(N):
    return prime_number(N) and all(prime_number(int(digit)) for digit in str(N))

if __name__ == '__main__':
    print(full_prima(2)) # True
    print(full_prima(3)) # True
    print(full_prima(11)) # False
    print(full_prima(13)) # False
    print(full_prima(23)) # True
    print(full_prima(29)) # False
    print(full_prima(37)) # True
    print(full_prima(41)) # False
    print(full_prima(43)) # False
    print(full_prima(53)) # True