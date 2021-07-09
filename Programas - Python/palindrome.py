def breakPalindrome(palindromeStr):
    # Write your code here
    
    my_list = list(palindromeStr)
    my_str = 'IMPOSSIBLE'

    if my_list[0] != 'a':
        my_list[0] = 'a'
    else:
        for index, letter in enumerate(my_list):
            if letter != 'a':
                my_list[index] = 'a'
                break

    new_str = ''.join(my_list)

    if new_str != palindromeStr and new_str != new_str[::-1]:
        my_str = new_str

    return my_str

if __name__ == '__main__':
    print(breakPalindrome('aaabbbaa'))
