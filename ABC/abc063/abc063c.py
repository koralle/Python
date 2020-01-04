n = int(input())

scores = sorted([int(input()) for i in range(0, n)])

def solve():
  total = sum(scores)
  if total % 10 == 0:
    for i in range(0, n):
      tmp = total- scores[i]
      if (tmp) % 10 != 0:
        print(tmp)
        return
    print(0)
    return

  print(total)
  return

def main():
  solve()

if __name__ == "__main__":
  main()