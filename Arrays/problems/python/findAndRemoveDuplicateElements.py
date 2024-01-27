myList = [1, 1, 2, 2, 3, 4, 5]

myList.pop(3)

print(myList)

def remove_duplicates(arr):
    newlist = []
    
    for i in range(len(arr)):
        if arr[i] in newlist:
            continue
        else:
            newlist.append(arr[i])
            
    return newlist


print(remove_duplicates(myList))    
        