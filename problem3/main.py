import sys

def prime_number(num):
    bil_prima = num

    # if ((num == 0) or (num == 1)):
    #     return 'Not Prime'

    # else:
    for i in range(2, (num // 2)):
        if ((num % i) == 0):
            # bil_prima = False
            return 'Not Prime'

    else :
        return 'Prime'


if __name__ == '__main__':
    print(prime_number(11)) # "Prime"
    print(prime_number(13)) # "Prime"
    print(prime_number(17)) # "Prime"
    print(prime_number(20)) # "Not Prime"
    print(prime_number(35)) # "Not Prime"