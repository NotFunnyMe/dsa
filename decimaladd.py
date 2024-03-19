def decimaladd():
    sum = 0
    number = input("Enter the number : ").split(".")
    # print(number)

    h = number[1]
    print(h)
    for i in range(len(h)):
        sum =  int(sum)+int(h[i])
    print(sum)

decimaladd()

    