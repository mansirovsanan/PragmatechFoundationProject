a=int(input("sətirlərin sayını daxil edin:"))
k=2*a-2
for i in range(0, a):

    for j in range(0, k):
        print(end=" ")

    k=k-2

    for j in range(0, i+1):

        print("*", end=" ")

    print()