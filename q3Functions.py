def is_perfect_num(lst):
    sum = 0
    for i in lst:
        for j in range(1, i):
            if i % j == 0:
                sum += j
        if sum == i:
            print(i)
        sum = 0


is_perfect_num([6, 2, 20, 496, 30, 8128, 500, 1000, 33550336, 999983, 14])