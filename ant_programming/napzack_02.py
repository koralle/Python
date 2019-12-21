import numpy as np

N = int(input())
wv = np.array([list(map(int, input().split())) for i in range(0, N)])
W = int(input())

# メモ化テーブル
memo = np.zeros((N+1, W+1), dtype=int)

def rec(n, uplimit_w):

  # 既に記録済みならその値を返すだけ
  if memo[n, uplimit_w] > 0:
    return memo[n, uplimit_w]

  ans = 0
  if n == N:
    return 0

  # n番目の品物を使えない場合 -> (n+1)番目の品物を使った結果と同じ
  elif wv[n, 0] > uplimit_w:
    return rec(n + 1, uplimit_w)

  # n番目の品物が使える時
  # -> n番目の品物は使った方がいいのか、使わない方がいいのか...?
  else:
    ans = max(
      rec(n + 1, uplimit_w),
      rec(n + 1, uplimit_w - wv[n, 0]) + wv[n, 1]
    )

    memo[n, uplimit_w] = ans
    return memo[n, uplimit_w]

def solve():
  print(rec(0, W))

def main():
  solve()

if __name__ == "__main__":
  main()