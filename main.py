
num = int(input("Enter your number here:  "))
n = num
length=len(str(n))

if length>=4:

    length= length//2
    chk = 0

    while n>0:
        rem=n%10
        if chk==length:
            m1=rem
        elif chk==(length-1):
            m2=rem
        num = num//10
        chk=chk+1
    prod = m1*m2
    print("Product is", n)
else:
    print('Enter correct option')

