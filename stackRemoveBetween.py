def delete(arr, value):
    tempArr = []
    found = False
    for item in arr:
        if found == False:
            temp = arr.pop()
            if temp == value:
                arr.pop()
                found = True
                print("arr", arr)
                print("newarr", tempArr)

                break
            else:
                tempArr.append(item)
        



arr = [1,3,5,7,13,4,6,23]
delete(arr, 13)