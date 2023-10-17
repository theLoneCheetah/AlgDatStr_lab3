def sort(final):
    if len(final) == 1:
        return final
    arr1 = sort(final[: len(final) // 2])
    arr2 = sort(final[len(final) // 2:])
    i = j = f = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            final[f] = arr1[i]
            i += 1
        else:
            final[f] = arr2[j]
            j += 1
        f += 1
    while i < len(arr1):
        final[f] = arr1[i]
        i += 1
        f += 1
    while j < len(arr2):
        final[f] = arr2[j]
        j += 1
        f += 1
    return final


n = int(input("Введите размер массива: "))
arr = [int(i) for i in input("Введите элементы массива: ").split()]
print(sort(arr))