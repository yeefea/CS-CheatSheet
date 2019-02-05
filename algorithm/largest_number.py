class ComparableStr(str):

    def __lt__(self, other):  # Trick!
        return int(self + other) < int(other + self)


def largest_num(nums):
    if len(nums) < 1:
        return '0'
    nums = [ComparableStr(x) for x in nums]
    largest_num = ''.join(sorted(nums, reverse=True))
    return '0' if largest_num[0] == '0' else largest_num


if __name__ == '__main__':
    nums = []
    print(largest_num(nums))
    nums = [0, 0, 0]
    print(largest_num(nums))
    nums = [10, 2]
    print(largest_num(nums))
    nums = [3, 30, 34, 5, 9]
    print(largest_num(nums))
