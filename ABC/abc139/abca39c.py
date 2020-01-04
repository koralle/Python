n = int(input())

height = list(map(int, input().split()))

ok = [False] * n

def solve():
  ans = 0
  for i in range(0, n - 1):
    tmp = 0
    while height[i] >= height[i + 1]:
      tmp += 1
      if ok[i]

def main():
  solve()


if __name__ == "__main__":
  main()