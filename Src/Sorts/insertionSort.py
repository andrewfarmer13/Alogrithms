def insertionSort(arr):

    n = len(arr)

    for i in range(1, n):

        key = arr[i]
        j = i -1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key


if __name__ == "__main__":
    arr = [12, 14, -7, 12000, 34, 6, -10, 11]
    print("Array before sorting: " + str(arr))
    insertionSort(arr)
    print("Array after sorting: " + str(arr))
