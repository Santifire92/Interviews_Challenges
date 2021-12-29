def flatten(arr):
    flattened = []
    for item in arr:
        if type(item) == list:
            for item in item:
                flattened.append(item)
        else:
            flattened.append(item)
    return flattened

def mergeSortedArrays(arrayOne, arrayTwo):
    result_array = []
    idx_a = idx_b = 0
    while (idx_a < len(arrayOne) or idx_b < len(arrayTwo)):
        if idx_a > (len(arrayOne) - 1):
            result_array.append(arrayTwo[idx_b:])
            return flatten(result_array)
        if idx_b > (len(arrayTwo) - 1):
            result_array.append(arrayOne[idx_a:])
            return flatten(result_array)
        if arrayOne[idx_a] <= arrayTwo[idx_b]:
            result_array.append(arrayOne[idx_a])
            idx_a += 1
        else:
            result_array.append(arrayTwo[idx_b])
            idx_b += 1
    return result_array

print(mergeSortedArrays([0,3,4,31], [4,6,30]))