# TO-DO: complete the help function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # Still need to figure out what to do with
    # a single element

    for i in range(len(merged_arr)):
        if(len(arrA) == 0):
            merged_arr[i] = arrB[0]
            arrB.pop(0)
        elif(len(arrB) == 0):
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        elif(arrA[0] < arrB[0]):
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        elif(arrA[0] > arrB[0]):
            merged_arr[i] = arrB[0]
            arrB.pop(0)

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if(len(arr) > 1):
        m = len(arr)//2
        arrA = merge_sort(arr[:m])
        arrB = merge_sort(arr[m:])
        arr = merge(arrA, arrB)

    return arr


test_list = [r]
print(merge_sort(test_list))
# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
