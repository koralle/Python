n = int(input())

s, t = input().split(' ')


def solve():
  ans = ''
  for i in range(0, n):
    ans += (s[i] + t[i])

  print(ans)

def main():
  solve()


if __name__ == "__main__":
  main()