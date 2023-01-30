def selectionSort(arr):
    
    for i in range(len(arr)):
        min = i

        for j in range(i+1,len(arr)):
            if arr[min] > arr[j]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]


if __name__ == "__main__":
    arr = [34, 12, 46, 8, 90, 123, 0, -2]
    print("Array before being sorted: " + str(arr))
    selectionSort(arr)
    print("Array after being sorted: " + str(arr))