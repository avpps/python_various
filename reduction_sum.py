''' What will be sum of n first natural numbers if
we remove firstly every k element of this list, 
then every k-1 and etc. till k=2 inclusive?

'''


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
