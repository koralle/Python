n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

def solve():
    
    """
    e.g.)
      zip([1, 2, 4, 6, 8], [4, 3, 7, 11, 10]
      => [(1, 4), (2, 3), (4, 7), (6, 11), (8, 10)]
      => [(2, 3), (1, 4), (4, 7), (8, 10), (6, 11)]
    """
    itv = sorted(list(zip(s, t)), key=lambda tup: tup[1])


    ans, _t = 0, 0
    for ti in range(0, n):
        # 現在時刻が開始時刻より前なら仕事をする
        if _t < (itv[ti])[0]:
            ans += 1
            # 現在時刻をその仕事の終了時刻にする
            _t = (itv[ti])[1]

    print(ans)

def main():
    solve()

if __name__ == "__main__":
    main()