a = input()

def solve():
    ans = ''
    if a == 'a':
        print(-1)
        return

    if len(a) == 1:
        print('a')
        return
    
    if len(a) > 1:
        tmp = ''
        for i in range(0, len(a)-1):
            tmp += 'a'
        print(tmp)
        return


def main():
    solve()

if __name__ == "__main__":
    main()