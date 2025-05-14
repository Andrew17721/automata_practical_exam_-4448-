def is_odd_palindrome(string: str) -> bool:
    n = len(string)
    if n % 2 == 0:
        return False  

    stack = []
    mid = n // 2

    for i in range(mid):
        stack.append(string[i])

    for i in range(mid + 1, n):
        if not stack or string[i] != stack.pop():
            return False

    return True


print(is_odd_palindrome("aba"))      
print(is_odd_palindrome("abcba"))     
print(is_odd_palindrome("abccba"))  
print(is_odd_palindrome("abca"))     
