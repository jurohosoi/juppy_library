# URL : https://atcoder.jp/contests/abc119/tasks/abc119_a

y, m, d = list(map(int, input().split('/')))

if y < 2019:
    print("Heisei")
elif y > 2019:
    print("TBD")
else:
    if m < 4:
        print("Heisei")
    elif m > 4:
        print("TBD")
    else:
        if d <= 30:
            print("Heisei")
        else:
            print("TBD")