def is_prime(n: int) -> bool:
    """
    与えられた数値が奇数であるかを判定する関数

    Args:
        n: 判定する数値

    Return:
        奇数であればTrue、偶数であればFalse

    """

    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3

    while i * i <= n:
        if n % i == 0:
            return False

        i += 2

    return True

