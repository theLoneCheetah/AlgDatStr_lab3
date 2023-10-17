def heap_sort(arr, n):
    if n == 2:   #если осталось всего два элемента, упорядочить по возрастанию
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    else:
        for i in range (n // 2 - 1, -1, -1):   #проход всех вершин, имеющих потомков
            # если левый потомок единственный и больше предка
            if 2 * i + 2 >= n and arr[2 * i + 1] > arr[i]:
                arr[i], arr[2 * i + 1] = arr[2 * i + 1], arr[i]
            #если левый потомок больше правого и предка
            elif 2 * i + 2 < n and arr[2 * i + 1] > arr[i] and arr[2 * i + 1] > arr[2 * i + 2]:
                arr[i], arr[2 * i + 1] = arr[2 * i + 1], arr[i]
            #если правый потомок больше левого и предка
            elif 2 * i + 2 < n and arr[2 * i + 2] > arr[i]:
                arr[i], arr[2 * i + 2] = arr[2 * i + 2], arr[i]
        arr[0], arr[n - 1] = arr[n - 1], arr[0]   #максимальный переносится в конец
        newarr = [arr[i] for i in range (n - 1)]
        newarr = heap_sort(newarr, n - 1)   #рекурсия для массива без последнего элемента
        newarr.append(arr[n - 1])   #последний присоединяется обратно
        return newarr


n = int(input("Введите размер массива (от 2): "))
arr = [int(i) for i in input("Введите элементы массива: ").split()]
print(heap_sort(arr, n))