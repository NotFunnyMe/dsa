def sum():
    sum = 0
    num = int(input("Enter the number : "))
    while num>0:
        rem = num%10
        sum += rem
        num //= 10
    return sum
print(sum())