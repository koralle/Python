import numpy as np

N = int(input())
wv = np.array([list(map(int, input().split())) for i in range(0, N)])
W = int(input())

# DPテーブル
dp = np.zeros((N+1, W+1), dtype=int)

def solve():
  for n in range(N - 1, -1, -1):
    for w in range(0, W + 1):
      if w < wv[n, 0]:
        dp[n, w] = dp[n + 1, w]
      else:
        dp[n, w] = max(dp[n+1, w], dp[n+1, w - wv[n, 0]] + wv[n, 1])

  print(dp[0, W])

def main():
  solve()

if __name__ == "__main__":
  main()