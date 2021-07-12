# linear search - taking all elements,more time consuming
# binary search - first sorting the list,then finding middle element,then finding condition

# binary search
l1=[1,9,8,5,3,2,11,54,13,15,17,19,20]
def bsearch():
    l1.sort()
    print(l1)
    num = int(input("enter number to search"))
    flag = 0
    low = 0
    upp = len(l1)-1
    while low <= upp:
        mid = (low + upp) // 2
        if num > l1[mid]:
            low = mid + 1
        elif num < l1[mid]:
            upp = mid - 1
        elif num == l1[mid]:
            flag = 1
            break
    if flag == 1:
        print("found in position of ",mid)
    else:
        print("not found")
bsearch()

