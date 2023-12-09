def day6b():
    T = 40829166
    R = 277133813491063
    for i in range(0,T//2+1):
        if i * (T-i) > R:
            print(i)
            break
    print(T + 1 - 2 * i)    