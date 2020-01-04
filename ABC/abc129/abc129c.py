n, m = map(int, input().split())
mod = (10 ** 9) + 7

arr = [int(input()) for i in range(0, m)]
dp = [0] * (n + 1)
dp[0] = 1

def solve():
  ok = [True] * (n+1)
  for i in range(0, m):
    ok[arr[i]] = False

  for step in range(1, n+1):
    if ok[step] == False:
      dp[step] = 0
    else:
      if step == 1:
        dp[step] = 1
      else:
        dp[step] = dp[step-1] + dp[step-2]

  print(dp[n] % mod)

def main():
  solve()

if __name__ == "__main__":
  main()