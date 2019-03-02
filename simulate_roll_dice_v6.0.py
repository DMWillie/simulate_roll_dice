"""
    作者:北辰
    功能:模拟掷骰子
    版本:6.0
    日期:06/07/2018
    2.0新增功能:模拟投掷两个骰子
    3.0新增功能:可视化投掷两个骰子的结果
    4.0新增功能:直方图可视化结果
    5.0新增功能:科学计算
    6.0新增功能:增加骰子个数到3个
"""

import numpy as np
import matplotlib.pyplot as plt

#解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False



def main():
    """
    主函数
    """
    total_times = 10000
    # 记录骰子结果(生成一个1-6之间形状为size的随机数组
    roll1_arr = np.random.randint(1, 7, size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)
    roll3_arr = np.random.randint(1, 7, size=total_times)
    result_arr = roll1_arr + roll2_arr + roll3_arr

    hist,bins = np.histogram(result_arr,bins=range(3,20))
    print(hist)
    print(bins)
    # 数据可视化

    # 直方图(第一个参数为数据,bins为边界,normed为归一化,edgecolor为边界颜色,linewidth为边界线的宽度
    # rwidth边界的宽度
    plt.hist(result_arr,bins=range(3,20),normed=1,edgecolor='black',linewidth=1,rwidth=0.8)
    #设置x轴坐标点显示
    tick_labels = ['2点','3点','4点','5点','6点',
                   '7点','8点','9点','10点','11点','12点'
                   '13点', '14点', '15点', '16点', '17点','18点']
    tick_pos = np.arange(3,20) + 0.5
    plt.xticks(tick_pos,tick_labels) # 位置,名称
    plt.title('骰子点数统计')
    plt.xlabel('点数和')
    plt.ylabel('频率')
    plt.show()

if __name__=='__main__':
    main()