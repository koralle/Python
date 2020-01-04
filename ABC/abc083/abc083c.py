x, y = map(int, input().split())

def solve():
  num = x
  ans = 0

  while num <= y:
    ans += 1
    num *= 2
  print(ans)

def main():
  solve()

if __name__ == "__main__":
  main()