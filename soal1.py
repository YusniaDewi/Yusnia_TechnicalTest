def rotate_list(list, rotate_count):
    rotate_count = rotate_count % len(list)
    return list[-rotate_count:] + list[:-rotate_count]

original_list = [1, 2, 3, 4, 5]
rotation_count = int(input("rotate count: "))
rotated_list = rotate_list(original_list, rotation_count)
print("Result:", rotated_list)