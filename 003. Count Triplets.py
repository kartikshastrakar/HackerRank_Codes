# Problem: https://www.hackerrank.com/challenges/count-triplets-1/problem
#  Score: 25


from collections import defaultdict


def count_triplets(arr, r):
    arr2 = defaultdict(int)
    arr3 = defaultdict(int)
    count = 0
    for i in arr:
        count += arr3[i]
        arr3[i*r] += arr2[i]
        arr2[i*r] += 1
    return count


n, r = map(int, input().split())
arr = list(map(int, input().split()))
print(count_triplets(arr, r))


from collections import defaultdict

def count_triplets(n, r, arr):
    arr2 = defaultdict(int)
    arr3 = defaultdict(int)
    count = 0
    for i in arr:
        count += arr3[i]
        arr3[i * r] += arr2[i]
        arr2[i * r] += 1
    return count

# Example usage
n, r = map(int, input("Enter n and r: ").split())
arr = list(map(int, input("Enter array elements: ").split()))
result = count_triplets(n, r, arr)
print("Number of triplets:", result)
