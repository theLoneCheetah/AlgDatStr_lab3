def block_sort(arr, blocksize):
    if blocksize < 10:   #если минимальный размер блока (= 1), вернуть
        return arr
    else:
        blockarr = [[] for i in range(10)]   #список из 10 блоков
        for i in range(len(arr)):
            blockarr[arr[i] // blocksize % 10].append(arr[i])   #распределение элементов по блокам
        unitedarr = []   #вспомогательный список для объединения блоков
        for i in range(10):
            unitedarr += block_sort(blockarr[i], blocksize // 10)   #рекурсия для каждого блока
        return unitedarr


n = int(input("Введите размер массива от 1 до 10^3: "))
arr = [int(i) for i in input("Введите элементы массива от 1 до 10^6: ").split()]
blocksize = 10 ** 5   #первоначально элементы до 10^6, блоки в 10 раз меньше
print(block_sort(arr, blocksize))