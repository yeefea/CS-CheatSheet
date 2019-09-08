"""
给定一个非负整数 row_index，生成杨辉三角的前 row_index 行。
"""
from typing import List


def get_row(row_index: int) -> List[int]:
    if row_index == 0:
        return [1]
    current_row = [1, 1]
    if row_index == 1:
        return current_row
    for i in range(row_index - 1):  # n=3, i = 0
        tmp_row = [1]
        for j in range(i + 1):
            tmp_row.append(current_row[j] + current_row[j + 1])
        tmp_row.append(1)
        current_row = tmp_row
    return current_row


print(get_row(0))
print(get_row(1))
print(get_row(2))
print(get_row(3))
print(get_row(4))
print(get_row(5))
