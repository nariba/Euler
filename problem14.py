#!/usr/local/bin/python3

def func(x):
    if x % 2 == 0:
        ans = x / 2
    elif x % 2 == 1:
        ans = 3 * x + 1
    else:
        ans = 0
    return ans

if __name__ == '__main__':
    count_m = 1
    for i in range(1000000):
        x = i+1
        count = 1
        while True:
            if x == 1:
                if count_m < count:
                    count_m = count
                    i_m = i+1
                break
            else:
                count += 1
                x = func(x)

        print(i+1, count)
    print(i_m, count_m)
