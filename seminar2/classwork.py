'''
Что такое функции
'''
def function_name(x, y):
    a = x + y
    b = x - y
    return a*b

x = 634
y = 2534
result = function_name(5, 6)
print(result)
print(x)


def insertion_sort(x):
    for i in range(len(x)):
        min_idx = i
        for j in range(i + 1, len(x)):
            if x[j] < x[min_idx]:
                min_idx = j

        x[i], x[min_idx] = x[min_idx], x[i]
    
    return x


def merge_sort(x):
    if len(x) == 1:
        return x

    left_half = x[:len(x)//2]
    right_half = x[len(x)//2:]
    
    sorted_left_half = merge_sort(left_half)
    sorted_right_half = merge_sort(right_half)
    
    i_left, i_right = 0, 0
    for i in range(len(x)):
        if i_left < len(sorted_left_half) and (i_right == len(sorted_right_half) or sorted_left_half[i_left] < sorted_right_half[i_right]):
            x[i] = sorted_left_half[i_left]
            i_left += 1
        else:
            x[i] = sorted_right_half[i_right]
            i_right += 1

    return x


def counting_sort_for_digits(x):
    counts = [0]*10
    for i in range(len(x)):
        digit = x[i]
        counts[digit] += 1
    
    result = []
    for digit in range(10):
        result += [digit]*counts[digit]
    
    return result


import time

x = list(range(10)) * 100000 + [0, 5, 9]

start_time = time.time()
sorted(x)
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
counting_sort_for_digits(x)
end_time = time.time()
print(end_time - start_time)


start_time = time.time()
merge_sort(x)
end_time = time.time()
print(end_time - start_time)
