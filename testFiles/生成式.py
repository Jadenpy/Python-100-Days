# -*- coding: utf-8 -*-
# @Author: Jaden Hu
# @Date:   2023-06-28 14:31:04
# @Last Modified by:   Jaden Hu
# @Last Modified time: 2023-06-28 15:25:44


# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# # 用股票价格大于100元的股票构造一个新的字典
# prices2 = {key: value for key, value in prices.items() if value > 100}
# print(prices2)

# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
# # 录入五个学生三门课程的成绩
# # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# # scores = [[None] * len(courses)] * len(names)
# scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
#         print(scores)



"""
从列表中找出最大的或最小的N个元素
堆结构(大根堆/小根堆)
"""
# import heapq

# list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# list2 = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# print(heapq.nlargest(3, list1))
# print(heapq.nsmallest(3, list1))
# print(heapq.nlargest(2, list2, key=lambda x: x['price']))
# print(heapq.nlargest(2, list2, key=lambda x: x['shares']))


"""
迭代工具模块
"""
# import itertools

# # 产生ABCD的全排列
# print(itertools.permutations('ABCD'))
# # 产生ABCDE的五选三组合
# print(itertools.combinations('ABCDE', 3))
# # 产生ABCD和123的笛卡尔积
# itertools.product('ABCD', '123')
# # 产生ABC的无限循环序列
# itertools.cycle(('A', 'B', 'C'))


"""
找出序列中出现次数最多的元素
"""
# from collections import Counter

# words = [
#     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
#     'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
#     'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
#     'look', 'into', 'my', 'eyes', "you're", 'under'
# ]
# counter = Counter(words)
# print(counter.most_common(3))



# 公鸡5元一只 母鸡3元一只 小鸡1元三只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
# for x in range(20):
#     for y in range(33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
#             print(x, y, z)

# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
# fish = 6
# while True:
#     total = fish
#     enough = True
#     for _ in range(5):
#         if (total - 1) % 5 == 0:
#             total = (total - 1) // 5 * 4
#         else:
#             enough = False
#             break
#     if enough:
#         print(fish)
#         break
#     fish += 5



"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
"""
class Thing(object):
    """物品"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        """价格重量比"""
        return self.price / self.weight


def input_thing():
    """输入物品信息"""
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)


def main():
    """主函数"""
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'总价值: {total_price}美元')


if __name__ == '__main__':
    main()

