def lcm():
    no1 = int(input("Enter the first number : "))
    no2 = int(input("Enter the second number : "))
    lcm = 1
    gcd = 1
    if no1<no2:
        no2,no1 = no1,no2
    for i in range(2,no1+1):
        if no1%i == 0 and no2%i == 0:
            gcd = i

    lcm = (no1*no2)//gcd
    print("The LCM of the given numbers is : ",lcm)

lcm()