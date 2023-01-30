def bubblesort(arr):
    size = len(arr)

    for x in range(size):

        for j in range(0, size-x-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


if __name__ == "__main__":
    arr = [1,3,45, 6, 0, 2, 34]
    print(arr)
    bubblesort(arr)
    print(arr)