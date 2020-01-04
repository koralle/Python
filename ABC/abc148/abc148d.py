n = int(input())

arr = list(map(int, input().split()))


def solve():
  if 1 not in arr:
    print(-1)
    return

  cnt = 1
  for i in range(0, n):
    if arr[i] == cnt:
      cnt += 1
  print(n - (cnt-1))

def main():
  solve()


if __name__ == "__main__":
  main()