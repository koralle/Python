a, b = map(int, input().split())
from fractions import gcd


def solve():
  ans = (a * b) // gcd(a, b)
  print(ans)

def main():
  solve()


if __name__ == "__main__":
  main()