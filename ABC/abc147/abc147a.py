a, b, c = map(int, input().split())

def solve():
  if (a + b + c) >= 22:
    print('bust')
    return
  else:
    print('win')
    return

def main():
  solve()

if __name__ == "__main__":
  main()