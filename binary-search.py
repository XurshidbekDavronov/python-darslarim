myList=[1,3,4,6,7,8,10,12,23,45,56,78,99]
def linear_search(myList, item):
    for n in range(len(myList)):
        if myList[n]==item:
            return n
    return None
        
def binary_search(myList, item):
    low=0
    high=len(myList)-1
    while low<=high:
        mid=(low+high)//2
        guess=myList[mid]
        if guess==item:
            return mid
        if guess>item:
            high=mid-1
        else:
            low=mid+1
    return None
print(binary_search(myList, 12))
print(linear_search(myList, 12))
