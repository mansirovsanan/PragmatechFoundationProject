nums=[5,6,7,9,9,10,10]
maaslar=[400,700,900,1200]

def cemTap(arr):
    cem=0
    for eded in arr:
        cem+=eded
    return cem
print(cemTap(maaslar))
print(cemTap(nums))