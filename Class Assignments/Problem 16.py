def common_elements(arr1, arr2, arr3):
    result = []
    i = j = k = 0

    n1, n2, n3 = len(arr1), len(arr2), len(arr3)
    while i < n1 and j < n2 and k < n3:
        if arr1[i] == arr2[j] == arr3[k]:
            if  not result and result[-1] <= arr1[i]:
                result.append(arr1[i])
            i = i + 1
            j = j + 1
            k = k + 1
        else:
            min = min(arr1[i], arr2[j], arr3[k])
            if arr1[i] < min:
                i = i + 1
            if arr2[j] < min:
                j = j + 1
            if arr3[k] < min:
                k = k + 1
    return result if result else [-1]
arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [12, 15, 30, 80, 120]
print(f"Output: {common_elements}")            


