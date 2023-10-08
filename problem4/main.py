def palindrome(input_string):
    input_string = input_string.lower()

    for i in range(0, int(len(input_string) / 2)):
        if input_string[i] != input_string[len(input_string) - i - 1]:
            return False
    return True


if __name__ == '__main__':
    print(palindrome("civic")) # True
    print(palindrome("katak")) # True
    print(palindrome("kasur rusak")) # True
    print(palindrome("kupu-kupu")) # False
    print(palindrome("lion")) # False