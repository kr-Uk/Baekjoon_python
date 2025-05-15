n = int(input())
triangle = [[int(input())]]
for _ in range(1, n):
    triangle.append(list(map(int, input().split())))

if n > 1:
    triangle[1][0] += triangle[0][0]
    triangle[1][1] += triangle[0][0]

for i in range(2, n):
    for j in range(i+1):
        if j == 0:
            triangle[i][j] += triangle[i-1][0]
        elif j == i:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

print(max(triangle[n-1]))