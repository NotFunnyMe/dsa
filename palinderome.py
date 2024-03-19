def palindrome():
    n = input("Enter the number : ")
    s = n[::-1]
    if (n == s):
        print ("The given number is a Palindrome")
    else:
        print ("The given number is not a palindrome")

palindrome()