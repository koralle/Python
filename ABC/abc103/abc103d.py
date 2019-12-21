n, m = map(int, input().split())
a = [0] * m
b = [0] * m
for i in range(0, m):
    a[i], b[i] = map(int, input().split())


def solve():
    # b[i]の値でソートする
    bridges = sorted(list(zip(a, b)), key=lambda tup: tup[1])

    ans, tmp = 0, 1

    for bi in range(0, len(bridges)):
        # まだ橋を撤去していなかったら
        # 最も右端の端を撤去する
        if tmp <= (bridges[bi])[0]:
            tmp = (bridges[bi])[1]
            ans += 1


    print(ans)

def main():
    solve()

if __name__ == "__main__":
    main()