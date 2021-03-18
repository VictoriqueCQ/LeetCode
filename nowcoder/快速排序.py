def quick_sort(array,start,end):
    if start>=end:
        return
    key = array[start]
    low = start
    high = end
    while low < high:
        while low <high and array[high]>= key:
            high -= 1
        array[low] = array[high]
        while low < high and array[low]<=key:
            low += 1
        array[high] = array[low]
    array[low] = key
    quick_sort(array,start,low-1)
    quick_sort(array,low+1,end)
    print(array)






array=[54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(array,0,len(array)-1)
