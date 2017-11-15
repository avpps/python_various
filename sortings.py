import timeit
import random


def my_sort(lis):
    len_lis = len(lis)
    count = 0
    while count < len_lis:
        act = lis[count]
        for i, item in enumerate(lis[count:]):
            if item < act:
                lis[count+i] = act
                act = item
        lis[count] = act
        count += 1
    return lis


def bubble_sort(lis):
    len_lis = len(lis)
    sorted_ = False
    for j in range(len_lis-2):
        if not sorted_:
            sorted_ = True
            for i in range(len_lis-1-j):
                if lis[i+1] < lis[i]:
                    sorted_ = False
                    lis[i+1], lis[i] = lis[i], lis[i+1]
        else:
            break
    return lis


def selection_sort(lis):
    len_lis = len(lis)
    for i in range(len_lis, 0, -1):
        j_max = None
        n_max = None
        for n, j in enumerate(lis[:i]):
            if j_max is None or j < j_max:
                j_max = j
                n_max = n
        lis[i-1], lis[n_max] = lis[n_max], lis[i-1]

    return lis


def insertion_sort(lis):
    len_lis = len(lis)
    for i in range(1, len_lis):
        fur = lis[i]
        back = i - 1
        while back >= 0 and lis[back] > fur:
            lis[back+1] = lis[back]
            back -= 1
        lis[back+1] = fur
    return lis


def gap_insertion_sort(lis, start, gap):
    len_lis = len(lis)
    for i in range(start, len_lis, gap):
        fur = lis[i]
        back = i - gap
        while back >= 0 and lis[back] > fur:
            lis[back+gap] = lis[back]
            back -= gap
        lis[back+gap] = fur
    return lis


def shell_sort(lis):
    inc = 2
    for i in range(inc):
        gap_insertion_sort(lis, i, inc)
    out = insertion_sort(lis)
    return out


def merge_function(m_1, m_2):
    out = []
    len_1 = len(m_1)
    len_2 = len(m_2)
    pos_1 = 0
    pos_2 = 0
    while True:
        if pos_1 < len_1 and pos_2 < len_2:
            if m_1[pos_1] > m_2[pos_2]:
                out.append(m_1[pos_1])
                pos_1 += 1
            elif m_1[pos_1] < m_2[pos_2]:
                out.append(m_2[pos_2])
                pos_2 += 1
            else:
                out.append(m_1[pos_1])
                out.append(m_2[pos_2])
                pos_1 += 1
                pos_2 += 1
        elif pos_1 < len_1:
            out.append(m_1[pos_1])
            pos_1 += 1
        elif pos_2 < len_2:
            out.append(m_2[pos_2])
            pos_2 += 1
        else:
            break
    return out


def merge_sort(lis):
    len_lis = len(lis)
    if len_lis == 1:
        return lis
    elif len_lis == 0:
        return None
    else:
        split = len(lis) // 2
        merge_sort(lis[:split])
        merge_sort(lis[split:])
        if m_1 and m_2:
            return merge_function(m_1, m_2)
        elif m_1:
            return m_1
        elif m_2:
            return m_2


def quick_sort(lis):
    len_lis = len(lis)
    if len_lis == 1:
        print('-  ', lis)
        return lis

    pos_i = 0
    val_i = lis[pos_i]

    pos_l_m = pos_i + 1
    pos_r_m = len_lis - 1
    while True:
        while lis[pos_l_m] < val_i:
            pos_l_m += 1
            if pos_l_m == len_lis:
                break
        while lis[pos_r_m] > val_i:
            pos_r_m -= 1
            if pos_r_m == pos_i:
                break
        if pos_l_m == len_lis or pos_r_m == pos_i:
            print('-- ', lis[pos_i+1:] + [val_i])
            return lis[pos_i+1:] + [val_i]
        if pos_l_m > pos_r_m:
            left = quick_sort(lis[pos_i+1:pos_r_m+1])
            right = quick_sort(lis[pos_r_m+1:])
            result = left + [val_i] + right
            print('---', result, left, [val_i], right, lis)
            return result
        else:
            lis[pos_l_m], lis[pos_r_m] = lis[pos_r_m], lis[pos_l_m]


print('\n', quick_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
# print('\n', sel([1,2,3,4]))

#
# sample = random.sample(range(10), 10)
# print(len(sample))
#
# print(timeit.timeit('my_sort(sample)', globals=globals()))
# print(timeit.timeit('bubble_sort(sample)', globals=globals()))
# print(timeit.timeit('selection_sort(sample)', globals=globals()))
# print(timeit.timeit('insertion_sort(sample)', globals=globals()))
#
#
# sample = random.sample(range(100), 100)
# print(len(sample))

# print(timeit.timeit('my_sort(sample)', globals=globals()))
# print(timeit.timeit('bubble_sort(sample)', globals=globals()))
# print(timeit.timeit('selection_sort(sample)', globals=globals()))
# print(timeit.timeit('insertion_sort(sample)', globals=globals()))
# print(timeit.timeit('shell_sort(sample)', globals=globals()))
