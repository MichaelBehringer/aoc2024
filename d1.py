data = [*map(int, open('d1.txt').read().split())]
A, B = sorted(data[0::2]), sorted(data[1::2])

sum1 = 0
sum2 = 0

for i in range(len(A)):
    diff = abs(A[i] - B[i])
    sum1 += diff

print(sum1)

for i in range(len(A)):
    count = B.count(A[i])
    sum2 += count * A[i]

print(sum2)
