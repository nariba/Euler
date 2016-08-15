#!/usr/local/bin/python3

import itertools

if __name__ == '__main__':
    s = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']
    t = 0
    for i in range(21):
        c = list(itertools.combinations(s, i))
        temp = len(c)**2
        t += temp
    print(t)
