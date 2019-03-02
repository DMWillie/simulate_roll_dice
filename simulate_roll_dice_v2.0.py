"""
    作者:北辰
    功能:模拟掷骰子
    版本:2.0
    日期:05/07/2018
    2.0新增功能:模拟投掷两个骰子
"""

import random

def roll_dice():
    """
    模拟掷骰子
    """
    roll = random.randint(1,6)
    return roll

def main():
    """
    主函数
    """
    total_times = 10000
    # 初始化次数列表
    result_list = [0] * 11
    # 初始化点数列表
    roll_list = list(range(2,13))
    # 结果字典
    roll_dict = dict(zip(roll_list,result_list)) # zip()函数将两个列表转换为一个元组

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        for j in roll_list:
            if roll1+roll2 == j:
                roll_dict[j]+=1

    for i,result in roll_dict.items():
        print('点数为{}的次数为:{},频率为{}'.format(i,result,result/total_times))

if __name__=='__main__':
    main()