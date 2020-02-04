# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # TO-DO: swap
        placeHolder = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = placeHolder
    return arr


test_arr = [9, 4, 3, 7, 6, 8, 2, 5, 1]
test_arr = selection_sort(test_arr)

print("SELECTION SORT")
for i in test_arr:
    print(i)

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    no_sort = False

    while no_sort == False:
        no_sort = True
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                place_holder = arr[i + 1]
                arr[i+1] = arr[i]
                arr[i] = place_holder
                no_sort = False

    return arr


test_arr = [9, 4, 1, 5, 5, 3, 7, 6, 8, 2, 5, 1]
test_arr = bubble_sort(test_arr)

print("BUBBLE SORT")
for i in test_arr:
    print(i)

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):
    counter = [0] * (maximum + 1)

    for i in range(0, len(arr) - 1):
        counter[arr[i]] += 1

    for i in range(0, maximum):
        counter[i + 1] = counter[i] + counter[i + 1]

    _arr = [0] * len(arr)

    for i in range(0, len(arr)):
        _arr[counter[arr[i]]] = arr[i]
        counter[arr[i]] -= 1

    arr = _arr
    return arr


test_arr = [9, 4, 3, 7, 6, 8, 2, 5, 1]
test_arr = count_sort(test_arr, 9)

print("COUNT SORT")
for i in test_arr:
    print(i)
