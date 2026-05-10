# 练习题已拆分到本目录下的独立文件中（编号与主题如下）。
#
#   exercise_01_consecutive_sublists.py   — consecutive_sublists
#   exercise_02_count_runs.py             — count_runs
#   exercise_03_group_by_digit_count.py   — group_by_digit_count
#   exercise_04_letter_pascal.py          — letter_pascal
#   exercise_05_abs_increasing_sublists.py — abs_increasing_sublists
#   exercise_06_words_containing_all.py   — words_containing_all
#   exercise_07_inventory.py              — InventoryError, InventoryItem
#
# 运行某一题的 doctest：python exercise_0N_....py

# ==========================
# 最小可背实现（按题号整理）
# ==========================

# 01
# cheatsheet 第2页｜Comprehensions｜List Comprehensions（列表推导式生成窗口）
# cheatsheet 第2页｜Sets｜Creating Sets（集合去重思路）
# cheatsheet 第2页｜Collections -> Tuples｜Creating tuples（tuple 作为可哈希键）
# cheatsheet 第2页｜Pythonic Constructs｜Remove duplicates（去重技巧）
def consecutive_sublists(L, k):
    windows = [L[i:i + k] for i in range(len(L) - k + 1)]  # 用滑窗切片拿到所有连续子列表
    unique = {tuple(w) for w in windows}  # 列表不可哈希，先转元组做去重
    return sorted([list(t) for t in unique])  # 还原为列表并按字典序排序后返回


# 02
# cheatsheet 第1页｜Loops -> For Loops｜for item in collection（逐字符遍历字符串）
# cheatsheet 第1页｜Strings -> String Indexing & Slicing｜切片 [2:]（去掉 0b 前缀）
# cheatsheet 第1页｜Conditionals｜if 条件判断（识别 0->1 的新 run）
# cheatsheet 说明｜bin() 内置函数在本 cheatsheet 未直接列出（但语法属于内置函数调用）
def count_runs(n):
    b = bin(n)[2:]  # 转二进制字符串并去掉前缀 0b
    runs = 0  # 记录 1-bit 连续段的数量
    prev = '0'  # 前置一个 0，便于识别以 1 开头的新段
    for ch in b:  # 逐位扫描二进制字符
        if ch == '1' and prev == '0':  # 只有从 0 跳到 1 才代表新 run 开始
            runs += 1  # 新 run 计数加一
        prev = ch  # 更新上一位
    return runs  # 返回 run 总数


# 03
from collections import defaultdict


# cheatsheet 第2页｜Dictionaries｜Dictionary Operations（按键分组与读取）
# cheatsheet 第1页｜Strings｜str() 与字符串长度 len() 的组合使用
# cheatsheet 第2页｜Collections｜len() / in 等集合基本操作思想
# cheatsheet 第1页｜Conditionals｜三元表达式风格的单复数分支
def group_by_digit_count(L):
    groups = defaultdict(list)  # 键是位数，值是该位数对应的数字列表
    for x in L:  # 按原顺序遍历输入列表
        d = len(str(x))  # 非负整数的位数等于字符串长度
        groups[d].append(x)  # 追加到对应位数组，天然保持原相对顺序
    for d in sorted(groups):  # 按位数从小到大输出分组
        nums = groups[d]  # 当前位数组
        word1 = "Number" if len(nums) == 1 else "Numbers"  # 单复数：元素个数决定 Number/Numbers
        word2 = "digit" if d == 1 else "digits"  # 单复数：位数决定 digit/digits
        print(f"{word1} with {d} {word2}: {' '.join(map(str, nums))}")  # 按指定格式打印


# 04
from string import ascii_uppercase


# cheatsheet 第1页｜Loops -> For Loops｜for 循环逐行构造
# cheatsheet 第2页｜Comprehensions｜List Comprehensions（行内字母映射）
# cheatsheet 第1页｜Strings｜join() 与格式化输出（拼接并打印）
# cheatsheet 第1页｜Numbers & Math｜算术与取模 %（26 字母循环）
def letter_pascal(n):
    row = [1]  # Pascal 第一行
    width = 2 * n - 1  # 最后一行的显示宽度（用于居中）
    for _ in range(n):  # 一共打印 n 行
        letters = [ascii_uppercase[(x - 1) % 26] for x in row]  # 数值映射字母（1->A，循环取模）
        s = ' '.join(letters)  # 行内字母用单空格连接
        print(s.center(width))  # 当前行按统一宽度居中打印
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]  # 生成下一行 Pascal


# 05
# cheatsheet 第1页｜Loops -> For Loops｜双层 for 遍历起点与终点
# cheatsheet 第1页｜Numbers & Math -> Useful Functions｜abs() 绝对值比较
# cheatsheet 第1页｜Conditionals｜严格递增条件判断
def abs_increasing_sublists(L):
    ans = []  # 保存所有满足条件的子列表
    for i in range(len(L)):  # 枚举每个起点
        cur = [L[i]]  # 从单元素子列表开始扩展
        ans.append(cur[:])  # 单元素总是合法，先加入答案
        for j in range(i + 1, len(L)):  # 向右尝试扩展
            if abs(L[j]) > abs(cur[-1]):  # 仅当绝对值严格递增时可扩展
                cur.append(L[j])  # 扩展当前子列表
                ans.append(cur[:])  # 记录当前长度下的合法结果（拷贝避免引用问题）
    return ans  # 按生成顺序返回


# 06
dictionary_file = 'dictionary.txt'


# cheatsheet 第2页｜File I/O｜with open(..., mode="r") 按行读取
# cheatsheet 第1页｜Loops -> For Loops｜for line in file / for item in collection
# cheatsheet 第2页｜Comprehensions｜列表推导式过滤单词
# cheatsheet 第1页｜Conditionals｜all(...) + in 的全包含判断
# cheatsheet 第1页｜Functions｜lambda（sorted 的 key）
def words_containing_all(required_letters):
    need = set(required_letters)  # 必需字母集合（去重后判断更直观）
    with open(dictionary_file, 'r') as f:  # 打开字典文件读取所有单词
        words = [line.strip() for line in f]  # 去掉换行，得到单词列表
    good = [w for w in words if all(c in w for c in need)]  # 过滤出包含全部必需字母的单词
    for w in sorted(good, key=lambda x: (len(x), x)):  # 先按长度升序，再按字母序
        print(w)  # 每行打印一个单词


# 07
class InventoryError(Exception):
    pass  # 统一库存业务异常类型


# cheatsheet 第1页｜Classes｜class / __init__ / self（类与实例）
# cheatsheet 第2页｜Exceptions｜Raising Exceptions（raise 异常）
# cheatsheet 第1页｜Conditionals｜参数合法性校验 if 分支
# cheatsheet 第1页｜Variables & Assignment｜实例属性赋值与更新
class InventoryItem:
    def __init__(self, name, stock):
        if not isinstance(name, str):  # 名称必须是字符串
            raise InventoryError("Item name must be a string")  # 按题目要求抛出固定消息
        if stock < 0:  # 初始库存不能为负
            raise InventoryError("Negative initial stock")  # 按题目要求抛出固定消息
        self.name = name  # 保存商品名
        self.stock = stock  # 保存当前库存

    def add_stock(self, n):
        if n <= 0:  # 调整量必须是正数
            raise InventoryError("Stock adjustment must be positive")  # 非法调整直接报错
        self.stock += n  # 合法则增加库存

    def remove_stock(self, n):
        if n <= 0:  # 调整量必须是正数
            raise InventoryError("Stock adjustment must be positive")  # 非法调整直接报错
        if n > self.stock:  # 不能扣成负库存
            raise InventoryError("Insufficient stock")  # 库存不足时报错
        self.stock -= n  # 合法则减少库存

    def get_stock(self):
        return self.stock  # 返回当前库存


# ==========================
# 背诵口诀（中英双语关键词）
# ==========================
# 1) 滑窗切片 Sliding Window -> 元组去重 Tuple Dedup -> 列表排序 Lexicographic Sort
# 2) 新段起点 New Run Start = 从0到1 Transition 0->1
# 3) 分组 Grouping 用 defaultdict(list)；输出 Ordering 用 sorted(keys)
# 4) 帕斯卡递推 Pascal Recurrence：next = [1] + 相邻和 Adjacent Sums + [1]
# 5) 绝对值递增 Absolute-Value Increasing：能扩展 Extend 就追加 Append
# 6) 全包含判断 Containment Check：all(c in word for c in need)
# 7) 先校验 Validate First，再改状态 Mutate State；非法即抛异常 Raise Error
