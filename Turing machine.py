def accepts_0n1n0n1n(s: str) -> bool:
    count = [0, 0, 0, 0]
    index = 0
    i = 0

    while i < len(s):
        if index == 0 and s[i] == '0':
            count[0] += 1
        elif index <= 1 and s[i] == '1':
            index = 1
            count[1] += 1
        elif index <= 2 and s[i] == '0':
            index = 2
            count[2] += 1
        elif index <= 3 and s[i] == '1':
            index = 3
            count[3] += 1
        else:
            return False
        i += 1

    return count[0] == count[1] == count[2] == count[3]

print(accepts_0n1n0n1n("00110011"))  
print(accepts_0n1n0n1n("0101"))      
print(accepts_0n1n0n1n("0001110011"))
