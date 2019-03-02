"""
    作者:北辰
    功能:模拟掷骰子
    版本:1.0
    日期:04/07/2018
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
    # 初始化结果列表[0,0,0,0,0,0]
    result_list = [0] * 6

    for i in range(total_times):
        roll = roll_dice()
        for j in range(1,7):
            if roll==j:
                result_list[j-1]+=1
    # enumerate()函数用于遍历列表的索引和元素值
    for i,result in enumerate(result_list):
        print('点数为{}的次数为:{},频率为{}'.format(i+1,result,result/total_times))

if __name__=='__main__':
    main()