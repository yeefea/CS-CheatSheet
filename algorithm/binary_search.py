"""
二分法
"""


def search(n, nums: list):
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left <= right:  # 注意，因为mid是左偏的，所以要<=
        # left + right 左偏, left + right + 1 右偏
        mid = (left + right) >> 1
        tmp = nums[mid]
        if tmp > n:
            # mid too large
            right = mid - 1
        elif tmp < n:
            # mid too small
            left = mid + 1
        else:
            return mid
    return -1


def search_left(n, nums):
    """
    where an element is if it exists, or where to insert it if it doesn't

    input: 3

    1 2 3 3 3 3 3 3 4 5  => 2
        *

    1 2 4 4 4 4 4  => 2
        *
    :param n:
    :param nums:
    :return:
    """
    if not nums:
        return 0
    left, right = 0, len(nums) - 1
    while left < right:
        """
        这里mid是左偏的
        比如输入 [1 3],目标值是2,要返回1
        """
        mid = (left + right) >> 1
        tmp = nums[mid]
        if tmp < n:
            left = mid + 1
        else:
            # mid too large, do not -1
            right = mid
    return left


def search_right(n, nums):
    if not nums:
        return 0
    left, right = 0, len(nums) - 1
    while left < right:
        """
        这里mid是右偏的
        比如输入 [1 2],目标值是2,要返回1
        比如输入 [1 3],目标值是2,要返回0
        
        [1 2 2 2 2 3] 2
        
        i
        left <- 0
        right <- 5
        mid <- 3, tmp = 2
        
        ii
        left <- 3
        mid <- 4, tmp = 2
        
        iii
        left <- 4
        mid <- 5, tmp = 3
        
        iv
        right <- 4
        
        stop loop
        """
        mid = (left + right + 1) >> 1
        tmp = nums[mid]
        if tmp > n:
            right = mid - 1
        else:
            left = mid
    return right


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(search(i, lst) for i in range(12)))
    lst = [1, 2, 3, 4, 6, 7, 8, 9, 10]
    print(list(search(i, lst) for i in range(12)))
    print(search(2, [1, 2, 2, 2, 3]))
    print(search_left(4, [1, 1, 2, 2, 2, 2, 2, 3]))
    print(search_left(5, [1, 1, 3, 3, 3, 3, 3, 4]))
    print(search_right(4, [1, 1, 3, 3, 3, 3, 5, 5]))
