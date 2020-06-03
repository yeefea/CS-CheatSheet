import ctypes


def int_overflow(val):
    maxint = 2147483647
    if not -maxint - 1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val


def unsigned_right_shift(n, i):
    # 数字小于0，则转为32位无符号uint
    if n < 0:
        n = ctypes.c_uint32(n).value
    # 正常位移位数是为正数，但是为了兼容js之类的，负数就右移变成左移好了
    if i < 0:
        return -int_overflow(n << abs(i))
    # print(n)
    return int_overflow(n >> i)


def murmurhash3(key, seed):
    # var remainder, bytes, h1, h1b, c1, c1b, c2, c2b, k1, i;
    remainder = len(key) & 3  # key.length % 4
    bytes_ = len(key) - remainder
    h1 = seed
    c1 = 0xcc9e2d51
    c2 = 0x1b873593
    i = 0

    while i < bytes_:
        k1 = \
            (key[i] & 0xff) | \
            ((key[i + 1] & 0xff) << 8) | \
            ((key[i + 2] & 0xff) << 16) | \
            ((key[i + 3] & 0xff) << 24)
        i += 4

        k1 = ((k1 & 0xffff) * c1 + (((unsigned_right_shift(k1, 16)) * c1) & 0xffff) << 16) & 0xffffffff
        k1 = (k1 << 15) | unsigned_right_shift(k1, 17)
        k1 = ((k1 & 0xffff) * c2 + ((unsigned_right_shift(k1, 16) * c2) & 0xffff) << 16) & 0xffffffff
        h1 ^= k1
        h1 = (h1 << 13) | unsigned_right_shift(h1, 19)
        h1b = ((h1 & 0xffff) * 5 + ((unsigned_right_shift(h1, 16) * 5) & 0xffff) << 16) & 0xffffffff
        h1 = (((h1b & 0xffff) + 0x6b64) + (((unsigned_right_shift(h1b, 16) + 0xe654) & 0xffff) << 16))

    k1 = 0

    while True:
        if remainder == 3:
            k1 ^= (key[i + 2] & 0xff) << 16
        if remainder == 2:
            k1 ^= (key[i + 1] & 0xff) << 8
        if remainder == 1:
            k1 ^= (key[i] & 0xff)

        k1 = (((k1 & 0xffff) * c1) + (((unsigned_right_shift(k1, 16) * c1) & 0xffff) << 16)) & 0xffffffff
        k1 = (k1 << 15) | unsigned_right_shift(k1, 17)
        k1 = (((k1 & 0xffff) * c2) + (((unsigned_right_shift(k1, 16) * c2) & 0xffff) << 16)) & 0xffffffff
        h1 ^= k1
        break
    h1 ^= len(key)
    h1 ^= unsigned_right_shift(h1, 16)
    h1 = (((h1 & 0xffff) * 0x85ebca6b) + (((unsigned_right_shift(h1, 16) * 0x85ebca6b) & 0xffff) << 16)) & 0xffffffff
    h1 ^= unsigned_right_shift(h1, 13)
    h1 = ((h1 & 0xffff) * 0xc2b2ae35 + ((unsigned_right_shift(h1, 16) * 0xc2b2ae35) & 0xffff) << 16) & 0xffffffff
    h1 ^= unsigned_right_shift(h1, 16)
    return unsigned_right_shift(h1, 0)


if __name__ == '__main__':
    print(murmurhash3(b'12333', 0x5f5dfe9))
