def two_sum(arr: list, target):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]


numbers = [3, -1, 5, 4]
target = 4
print(two_sum(numbers, target))
