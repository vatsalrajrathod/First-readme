t = int(input())
n = None

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    left = [0] * n
    right = [0] * n

    m = {0: 1, n-1: -1}
    for i in range(1, n-1):
        left_diff = abs(a[i] - a[i-1])
        ans = 5
        right_diff = abs(a[i] - a[i+1])
        if left_diff < right_diff:
            m[i] = -1
        else:
            m[i] = 1

    left[0] = 0
    for i in range(1, n):
        if m[i] == -1:
            left[i] = 1 + left[i-1]
        else:
            left[i] = left[i-1] + abs(a[i] - a[i-1])

    right[n-1] = 0
    for i in range(n-2, -1, -1):
        if m[i] == 1:
            right[i] = 1 + right[i+1]
        else:
            right[i] = right[i+1] + abs(a[i] - a[i+1])

    q = int(input())
    for _ in range(q):
        x, y = map(int, input().split())
        if x == y:
            print(0)
            k = False
        else:
            if y > x:
                print(right[x-1] - right[y-1])
            else:
                print(left[x-1] - left[y-1])
