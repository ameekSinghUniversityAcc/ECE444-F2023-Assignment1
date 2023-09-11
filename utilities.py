class utils:
    #function reversed: reverses digits in n, while preserving the sign 
    #input n -> int
    #output n_reversed
    def reversed(n):
        if type(n) != int:
            return "Error!"
        sign = 1
        if n < 0:
            sign = -1
            n *= -1
        listifiedNum = []
        reversedNum = 0
        while n > 0:
            listifiedNum.append(n % 10)
            n = n // 10
        while listifiedNum:
            reversedNum += listifiedNum[0] * 10 ** (len(listifiedNum) - 1)
            listifiedNum.pop(0)
        return sign * reversedNum
    #function formatter: return binary and octal representation
    #input n -> int
    #output (binary representation of n, octal representation of n)
    def formatter(n):
        if type(n) != int:
            return "Error!"
        if n <= 1: return n
        #Referenced from: https://docs.python.org/3/library/functions.html (bin, oct)
        return (bin(n), oct(n))

        