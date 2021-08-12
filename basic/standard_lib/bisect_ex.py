from bisect import bisect_left, bisect_right

# returns a number of data which has value of left_value or right_value
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    print("right_index : ", right_index)
    print("left_index : ", left_index)
    return right_index - left_index

# list assigned
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))
