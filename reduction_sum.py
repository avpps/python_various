def oszcz(n=1000000, k=100):
    suma = n * (n + 1) / 2
    for i in range(k-1):
        c = 0
        m = 0
        while m < n:
            c += 1
            m = k * c - i
            if m <= n:
                suma -= m
    print(int(suma))
    return int(suma)


if __name__ == '__main__':
    oszcz()
