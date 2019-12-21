n = int(input())
s = input()


def solve():
    a = 0
    b = n - 1

    while a <= b:
        left = False
        i = 0
        while a + i <= b:

            """
            e.g.) s = "aaabcdefgaaa"のとき
            ===> a++
            aaabcdefgaaa
                b-- <===

            最初に辞書順の大小が決まる文字でbreakする。
            """

            # 頭の方が辞書順で早い時
            if(s[a + i] < s[b-i]):
                left = True
                break
            # ケツの方が辞書順で早い時
            # ケツの方が辞書順で早い時
            elif (s[a + i] > s[b-i]):
                left = False
                break
            i+=1
        if left == True:
            print(s[a], end='')
            a += 1
        else:
            print(s[b], end='')
            b -= 1

def main():
    solve()

if __name__ == "__main__":
    main()