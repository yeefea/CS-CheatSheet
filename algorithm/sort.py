def bubble_sort(a: list):
    """
    time:
        avg: O(N^2), best: O(N), worst: O(N^2)
    space:
        O(1)
    stability:
        stable
    :param a:
    :return:
    """
    for i in range(len(a)):
        for j in range(len(a) - 1, i, -1):
            if a[j - 1] > a[j]:  # 大数在前
                a[j], a[j - 1] = a[j - 1], a[j]  # 交换


def insertion_sort(a: list):
    """
    time:
        avg: O(N^2), best: O(N), worst: O(N^2)
    space:
        O(1)
    stability:
        stable
    :param a:
    :return:
    """
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i > -1 and a[i] > key:
            a[i + 1] = a[i]  # 大数向后移动
            i -= 1
        a[i + 1] = key


def merge_sort(a: list):
    """
    time:
        avg: O(NlogN), best: O(NlogN), worst: O(NlogN)
    space:
        O(N)
    stability:
        stable
    :param a:
    :return:
    """

    def _merge_sort(left: int, right: int):
        """
        center = (left + right) // 2
        :param left:
        :param right:
        :return:
        """
        if left < right:
            center = (left + right) >> 1
            _merge_sort(left, center)
            _merge_sort(center + 1, right)
            _merge(left, center, right)

    def _merge(left: int, center: int, right: int):
        """
        merge a[left:center] and a[center+1,right]
        :param left:
        :param center:
        :param right:
        :return:
        """
        tmp_ptr = left  # tmp array pointer
        l_ptr = left  # left array pointer
        r_ptr = center + 1  # right array pointer
        while l_ptr <= center and r_ptr <= right:
            if a[l_ptr] <= a[r_ptr]:
                tmp_arr[tmp_ptr] = a[l_ptr]
                l_ptr += 1
            else:
                tmp_arr[tmp_ptr] = a[r_ptr]
                r_ptr += 1
            tmp_ptr += 1
        while l_ptr <= center:
            tmp_arr[tmp_ptr] = a[l_ptr]
            tmp_ptr += 1
            l_ptr += 1
        while r_ptr <= right:
            tmp_arr[tmp_ptr] = a[r_ptr]
            tmp_ptr += 1
            r_ptr += 1
        for i in range(left, right + 1):
            a[i] = tmp_arr[i]

    tmp_arr = [None] * len(a)
    _merge_sort(0, len(a) - 1)


def quick_sort(a):
    """
    time:
        avg: O(NlogN), best: O(NlogN), worst: O(N^2)
    space:
        O(logN)
    stability:
        unstable
    :param a:
    :return:
    """

    def _quick_sort(start, end):
        """
        sort [start, center-1] [center+1, end]
        :param start:
        :param end:
        :return:
        """
        if start < end:
            center = _partition(start, end)
            _quick_sort(start, center - 1)
            _quick_sort(center + 1, end)

    def _partition(start, end):
        pivot = a[end]
        i = start - 1
        for j in range(start, end):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        center = i + 1
        a[center], a[end] = a[end], a[center]  # swap center and end
        return center

    _quick_sort(0, len(a) - 1)
