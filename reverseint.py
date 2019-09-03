import sys
import string
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    s = str(x)
    z = ""
    n = False
    for i in s:
        if i in string.punctuation:
            n = True
        else:
            z = i + z
    if int(z) <= 2147483647 and int(z) >= -2147483647:
        if n == True:
            z = int(z) * -1
        elif z == "":
            z = "0" + z
        elif len(z)>1 and z[0]=="0":
            z = z[1:]
            z = "0" + z       
        else:
            pass     
        return int(z)
    else:
        return 0


def main():
    #x = 901000
    x=1534236469
    #x=123
    sol = reverse(x)
    print sol

if __name__ == '__main__':
    main()