# Given a number n, check whether it is even or odd. Return true for even and false for odd.
# 1) Bitwise Operator

# def isEven(n):
#     if (n & 1) == 0:
#         return True
#     else:
#         return False
    
# if __name__ == "__main__":
#     n = 11

#     if isEven(n):
#         print(True)
#     else:
#         print(False)


# 2) modulus Operator

def isEven(n):
    if(n % 2) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    n= 19
    if isEven(n):
        print(True)
    else:
        print(False)