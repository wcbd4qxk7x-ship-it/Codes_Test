"""
Python 列表（常被称为“数组”）常见用法一览。
每个用法都包含 1-2 个可直接运行的示例程序，运行本文件即可看到示例输出。
"""

from __future__ import annotations

import copy
from pprint import pprint


# 1. 创建列表
def demo_create_literal() -> None:
    cities = ["北京", "上海", "深圳"]
    mixed = [42, 3.14, "Python", True]
    print("[创建列表-字面量]", cities, mixed)


def demo_create_constructor() -> None:
    numbers = list(range(5))
    empty = list()
    print("[创建列表-constructor]", numbers, empty)


# 2. 索引与切片
def demo_index_access() -> None:
    colors = ["red", "green", "blue", "yellow"]
    first = colors[0]
    last = colors[-1]
    print("[索引访问]", first, last)


def demo_slice_access() -> None:
    data = [0, 1, 2, 3, 4, 5]
    left = data[:3]
    step = data[::2]
    reverse = data[::-1]
    print("[切片访问]", left, step, reverse)


# 3. 添加元素
def demo_append_extend_insert() -> None:
    fruits = ["apple"]
    fruits.append("banana")
    fruits.extend(["cherry", "date"])
    fruits.insert(1, "blueberry")
    print("[添加元素]", fruits)


# 4. 删除元素
def demo_remove_pop_clear() -> None:
    nums = [10, 20, 30, 20]
    nums.remove(20)  # 删除首个匹配值
    popped = nums.pop()  # 删除最后一个
    nums.clear()  # 清空
    print("[删除元素]", popped, nums)


# 5. 搜索与计数
def demo_search_count() -> None:
    letters = ["a", "b", "a", "c", "a"]
    first_idx = letters.index("a")
    total_count = letters.count("a")
    print("[搜索与计数]", first_idx, total_count)


# 6. 排序与反转
def demo_sort_reverse() -> None:
    scores = [88, 75, 90, 100]
    scores.sort()
    scores_desc = sorted(scores, reverse=True)
    scores.reverse()
    print("[排序与反转]", scores, scores_desc)


# 7. 列表推导式
def demo_list_comprehension() -> None:
    squares = [n * n for n in range(6)]
    nested = [(x, y) for x in range(2) for y in range(2)]
    print("[列表推导式]", squares, nested)


# 8. 遍历列表
def demo_iteration_enumerate() -> None:
    animals = ["cat", "dog", "bird"]
    for idx, name in enumerate(animals, start=1):
        print(f"[遍历-enumerate] {idx}: {name}")


def demo_iteration_zip() -> None:
    names = ["Alice", "Bob", "Cathy"]
    scores = [95, 88, 91]
    for name, score in zip(names, scores):
        print(f"[遍历-zip] {name} -> {score}")


# 9. 复制与浅/深拷贝
def demo_copy() -> None:
    original = [[1, 2], [3, 4]]
    shallow = original.copy()
    deep = copy.deepcopy(original)
    original[0][0] = 99
    print("[复制]", original, shallow, deep)


# 10. 条件过滤
def demo_filter() -> None:
    ages = [12, 19, 25, 16, 30]
    adults = [age for age in ages if age >= 18]
    print("[条件过滤]", adults)


# 11. 列表作为栈与队列
def demo_stack_queue() -> None:
    stack = []
    stack.append("task1")
    stack.append("task2")
    stack_top = stack.pop()

    queue = ["first", "second", "third"]
    queue.append("fourth")
    first_out = queue.pop(0)

    print("[栈与队列]", stack_top, first_out, queue)


# 12. 嵌套列表与二维结构
def demo_nested_lists() -> None:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    pprint({"matrix": matrix, "transposed": transposed}, compact=True)


# 13. 解包与多变量赋值
def demo_unpacking() -> None:
    values = [100, 200, 300]
    first, *middle, last = values
    a, b, c = values
    print("[解包]", first, middle, last, a, b, c)


# 14. 成员测试与聚合
def demo_membership_and_aggregate() -> None:
    nums = [3, 7, 2, 9]
    exists = 7 in nums
    total = sum(nums)
    maximum = max(nums)
    print("[成员与聚合]", exists, total, maximum)


USAGE_TABLE = [
    ("创建列表", (demo_create_literal, demo_create_constructor)),
    ("索引与切片", (demo_index_access, demo_slice_access)),
    ("添加元素", (demo_append_extend_insert,)),
    ("删除元素", (demo_remove_pop_clear,)),
    ("搜索与计数", (demo_search_count,)),
    ("排序与反转", (demo_sort_reverse,)),
    ("列表推导式", (demo_list_comprehension,)),
    ("遍历列表", (demo_iteration_enumerate, demo_iteration_zip)),
    ("复制与浅/深拷贝", (demo_copy,)),
    ("条件过滤", (demo_filter,)),
    ("列表作为栈/队列", (demo_stack_queue,)),
    ("嵌套列表", (demo_nested_lists,)),
    ("解包赋值", (demo_unpacking,)),
    ("成员测试与聚合", (demo_membership_and_aggregate,)),
]


def run_examples() -> None:
    for title, funcs in USAGE_TABLE:
        print("=" * 20, title, "=" * 20)
        for func in funcs:
            func()


if __name__ == "__main__":
    run_examples()

