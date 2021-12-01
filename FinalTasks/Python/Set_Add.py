#Enter  your code here. Read input from STDIN. Print output to STDOUT

country=set()
n=int(input())

for i in range(n):
    country.add(input())
print(len(country))