'''arr_size, plus_num, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[arr_size - 1]
second = data[arr_size - 2]

result = 0

while True:
    for i in range(K):
        if plus_num == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

result = 0

count = m // (k+1)
count += m % (k+1)

result += count * first
result += (m - count) * second

print(result)