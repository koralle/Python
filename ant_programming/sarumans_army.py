n:int = int(input())
r:int = int(input())
x = sorted(map(int, input().split()))


def solve():
    i:   int = 0
    ans: int = 0
    while (i < n):
        # s := カバーされていない一番左の点の位置
        s: int = x[i]
        i += 1

        # 位置sから距離rを超える点まで右に移動する
        #tmp: int = s + r
        while ((i < n) and x[i] <= s + r):
            i += 1

        # p := 新しく印をつける点の位置
        p: int = x[i-1]

        # 位置pから距離rを超えるまで右に移動する
        # tmp: int = p + r
        while (i < n and x[i] <= p + r):
            i += 1

        ans += 1

    print(ans)

def main():
    solve()


if __name__ == "__main__":
    main()