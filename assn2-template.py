import time

List = input("List:")
nums = List.split()
nums = [int(i) for i in nums]

def recbinsearch(L,l,u,target):
    if len(L)<1:
        return -1
    else:
        if l == u:
            target = l
        elif l < u:
            middle = int((l + u)//2)
            if  L[middle] < target:
                recbinsearch(L,middle+1,u,target)
            elif L[middle] == target:
                target = L[middle]
            else:
                recbinsearch(L,l,middle-1,target)
        else:
            return -1

def binsearch(nums, target):
    lower = 0
    upper = len(nums)-1
    idx = -1
    while(lower<=upper):
        middle = int((lower + upper)//2)
        if nums[middle] == target:
            idx = middle
            break
        elif nums[middle] < target:
            lower = middle + 1
        else:
            upper = middle - 1
    return idx

while True:
    target = int(input("target :"))
    ts = time.time()
    idx= binsearch(nums, target)
    if idx == -1:
        break
    ts = time.time() - ts
    print("Binary Search %d: not found time %.13f" %(target, ts))

    ts = time.time()
    idx = recbinsearch(nums, 0, len(nums)-1, target)
    if idx == -1:
        break
    ts = time.time() - ts
    print("Binary Search %d: not found time %.13f" %(target, ts))