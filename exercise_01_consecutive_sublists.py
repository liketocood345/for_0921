# =============================================================================
# 题目 / Problem
# -----------------------------------------------------------------------------
# 实现 consecutive_sublists(L, k)：返回列表 L 中所有长度为 k 的「连续子列表」的去重结果，
# 并按整数序列的字典序排序；相同内容的子列表只保留一次；结果通过 return 返回，不要 print。
#
# Implement consecutive_sublists(L, k): return every distinct consecutive sublist of
# length k from L, sorted lexicographically as lists of ints; duplicates collapse to one;
# return the value (do not print).
#
# 连续子列表 / Consecutive sublist: 原列表中相邻 k 个元素构成的切片 L[i : i+k]。
# A consecutive sublist is a slice of k adjacent elements: L[i : i+k].
#
# 假设 / Assumptions: L 为 int 列表；0 ≤ k ≤ len(L)。
# =============================================================================

def slice_bounds_are_valid(L, start_index, k):
    """
    EN: True iff start_index and k describe a slice fully inside L (length k).
    ZH: 判断起始下标与长度 k 是否能在 L 上取出长度为 k 的合法连续切片。
    """
    列表长度 = len(L)
    if k < 0:
        return False
    if start_index < 0 or start_index > 列表长度 - k:
        return False
    return True


def extract_consecutive_windows(L, k):
    """
    EN: Collect every contiguous window L[i : i+k] for valid i.
    ZH: 从左到右滑动窗口，提取所有长度为 k 的连续切片（即题目要求的连续子列表）。
    """
    列表长度 = len(L)
    窗口列表 = []
    for 起始下标 in range(列表长度 - k + 1):
        if not slice_bounds_are_valid(L, 起始下标, k):
            continue
        窗口列表.append(L[起始下标 : 起始下标 + k])
    return 窗口列表


def deduplicate_sublists(sublists):
    """
    EN: Lists are unhashable; convert each window to tuple, build a set of distinct tuples.
    ZH: 列表不可哈希；转成元组后放入集合，去除内容完全相同的重复子列表。
    """
    唯一元组集合 = set()
    for 子列表 in sublists:
        唯一元组集合.add(tuple(子列表))
    return 唯一元组集合


def tuples_to_sorted_lists_lex_order(unique_tuples):
    """
    EN: Turn distinct tuples back into lists and sort lexicographically (Python list compare).
    ZH: 将去重后的元组还原为列表，并按字典序排序（整数序列逐项比较）。
    """
    列表形式 = [list(元组项) for 元组项 in unique_tuples]
    return sorted(列表形式)


def consecutive_sublists(L, k):
    """
    >>> consecutive_sublists([], 0)
    [[]]
    >>> consecutive_sublists([7, 7, 7, 7], 1)
    [[7]]
    >>> consecutive_sublists([4, 1, 7, 4], 1)
    [[1], [4], [7]]
    >>> consecutive_sublists([4, 1, 7], 2)
    [[1, 7], [4, 1]]
    >>> consecutive_sublists([4, 1, 7], 3)
    [[4, 1, 7]]
    >>> consecutive_sublists([2, 3, 5, 8], 2)
    [[2, 3], [3, 5], [5, 8]]
    >>> consecutive_sublists([1, 1, 1], 2)
    [[1, 1]]
    >>> consecutive_sublists([5, 2, 5], 2)
    [[2, 5], [5, 2]]
    >>> consecutive_sublists([1, 2, 3, 4, 5], 4)
    [[1, 2, 3, 4], [2, 3, 4, 5]]
    """
    所有连续窗口 = extract_consecutive_windows(L, k)
    去重元组集 = deduplicate_sublists(所有连续窗口)
    return tuples_to_sorted_lists_lex_order(去重元组集)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
