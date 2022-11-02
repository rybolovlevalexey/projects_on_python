from decimal import *
cnt = 0
ans = 0
for x in range(1, 9):
    for y in range(1, 9):
        for i in range(1, 9):
            for j in range(1, 9):
                if i == x and j == y:
                    continue
                cnt += 1
                if x == i or y == j:
                    ans += 1
print(cnt, ans, 64*63)
res1 = Decimal(ans)
res2 = Decimal(cnt)
res = res1 / res2
print(res)