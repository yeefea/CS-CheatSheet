"""
给定一个非负整数 num_rows，生成杨辉三角的前 num_rows 行。
"""
from typing import List


def generate(num_rows: int) -> List[List[int]]:
    if num_rows == 0:
        return []
    current_row = [1]
    triangle = [current_row]
    if num_rows == 1:
        return triangle
    current_row = [1, 1]
    triangle.append(current_row)
    if num_rows == 2:
        return triangle
    for i in range(num_rows - 2):  # n=3, i = 0
        tmp_row = [1]
        for j in range(i + 1):
            tmp_row.append(current_row[j] + current_row[j + 1])
        tmp_row.append(1)
        current_row = tmp_row
        triangle.append(current_row)
    return triangle


print(generate(0))
print(generate(1))
print(generate(2))
print(generate(3))
print(generate(4))
