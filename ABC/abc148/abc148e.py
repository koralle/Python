n = int(input())

dp = []
dp.append(1)
dp.append(1)

def solve():
  sum_10 = 0
  if n % 2 == 1:
    print(0)
    return

  elif n == 0:
    print(0)
    return
  # nが2以上の偶数の場合
  else:
    num = 2
    count_5 = 0
    count_digit = 0
    count_10 = 0
    while num <= n:
      dp.append((num) * dp[num - 2])
      dp.append(0)
      if count_5 == 5:
        count_5 = 0
        sum_10 += (count_digit + 1)
      else:
        count_5 += 1

      if dp[num] % 10 == 0:
        count_10 += 1
        if count_10 == 10:
          count_10 = 0
          count_digit += 1

      num += 2

  print(sum_10)


def main():
  solve()


if __name__ == "__main__":
  main()