# This function returns the number of contiguous runs of 1-bits
# in the binary representation of the argument.
#
# A "run" is a maximal consecutive sequence of 1s.
#
# For instance:
# 0:     0        → 0 runs
# 1:     1        → 1 run
# 2:    10        → 1 run
# 3:    11        → 1 run
# 4:   100        → 1 run
# 5:   101        → 2 runs
# 6:   110        → 1 run
# 7:   111        → 1 run
# 9:  1001        → 2 runs
# 13: 1101        → 2 runs
# 27: 11011       → 2 runs
#
# You can assume that the argument to count_runs() is an integer
# at least equal to 0.
#
# The output is returned, not printed.
# 02
def count_runs(n):
    b = bin(n)[2:]  # 转二进制字符串并去掉前缀 0b
    runs = 0  # 记录 1-bit 连续段的数量
    prev = '0'  # 前置一个 0，便于识别以 1 开头的新段
    for ch in b:  # 逐位扫描二进制字符
        if ch == '1' and prev == '0':  # 只有从 0 跳到 1 才代表新 run 开始
            runs += 1  # 新 run 计数加一
        prev = ch  # 更新上一位
    return runs  # 返回 run 总数


# def count_runs(n):
#     '''
#     >>> count_runs(0)
#     0
#     >>> count_runs(1)
#     1
#     >>> count_runs(2)
#     1
#     >>> count_runs(3)
#     1
#     >>> count_runs(4)
#     1
#     >>> count_runs(5)
#     2
#     >>> count_runs(6)
#     1
#     >>> count_runs(7)
#     1
#     >>> count_runs(9)
#     2
#     >>> count_runs(13)
#     2
#     >>> count_runs(37)
#     3
#     '''
#     return -1
#     # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE


print(count_runs(1223))