#Task
#The provided code stub reads two integers,a and b, from STDIN.
#Add logic to print two lines. The first line should contain the result of integer division,
#a//b . The second line should contain the result of float division, a/b.
#No rounding or formatting is necessary.

def main():
    quotient=a//b
    quotientf=a/b
    print(quotient)
    print(quotientf)
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    main()