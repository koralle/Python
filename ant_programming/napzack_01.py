N = int(input())
wv = [tuple(map(int, input().split())) for i in range(0, N) ]
W = int(input())

def rec(n, uplimit_w):
  ans = 0
  if n == N:
    return 0

  # n番目の品物を使えない場合 -> (n+1)番目の品物を使った結果と同じ
  elif wv[n][0] > uplimit_w:
    return rec(n + 1, uplimit_w)

  # n番目の品物が使える時
  # -> n番目の品物は使った方がいいのか、使わない方がいいのか...?
  else:
    ans = max(
      rec(n + 1, uplimit_w),
      rec(n + 1, uplimit_w - wv[n][0]) + wv[n][1]
    )
    return ans

def solve():
  print(rec(0, W))

def main():
  solve()

if __name__ == "__main__":
  main()