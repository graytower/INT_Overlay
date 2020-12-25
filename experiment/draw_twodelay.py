#!/usr/bin/python
# coding: UTF-8

import matplotlib.pyplot as plt
from pylab import *
from numpy import *
import numpy as np


def main():

    file1_1 = open("delaydata_heavy/processdelay_ft_vxlan.txt")
    file1_2 = open("delaydata_heavy/processdelay_ft_dfs.txt")
    file2_1 = open("delaydata_heavy/queuingdelay_ft_vxlan.txt")
    file2_2 = open("delaydata_heavy/queuingdelay_ft_dfs.txt")
    file3_1 = open("delaydata_heavy/processdelay_sl_vxlan.txt")
    file3_2 = open("delaydata_heavy/processdelay_sl_dfs.txt")
    file4_1 = open("delaydata_heavy/queuingdelay_sl_vxlan.txt")
    file4_2 = open("delaydata_heavy/queuingdelay_sl_dfs.txt")

    lines1_1 = file1_1.readlines()
    lines1_2 = file1_2.readlines()
    lines2_1 = file2_1.readlines()
    lines2_2 = file2_2.readlines()
    lines3_1 = file3_1.readlines()
    lines3_2 = file3_2.readlines()
    lines4_1 = file4_1.readlines()
    lines4_2 = file4_2.readlines()

    delay1_1 = zeros((5, 20), dtype=int)
    delay1_2 = zeros((5, 20), dtype=int)
    delay2_1 = zeros((5, 20), dtype=int)
    delay2_2 = zeros((5, 20), dtype=int)
    delay3_1 = zeros((5, 20), dtype=int)
    delay3_2 = zeros((5, 20), dtype=int)
    delay4_1 = zeros((5, 20), dtype=int)
    delay4_2 = zeros((5, 20), dtype=int)

    for i in range(len(lines1_1)):
        line = lines1_1[i].strip('\n').split(', ')
        line_tmp = [float(x) for x in line]
        delay1_1[i:] = line_tmp
    for i in range(len(lines1_2)):
        line = lines1_2[i].strip('\n').split(', ')
        line_tmp = [float(x) for x in line]
        delay1_2[i:] = line_tmp
    for i in range(len(lines2_1)):
        line = lines2_1[i].strip('\n').split(', ')
        line_tmp = [float(x) for x in line]
        delay2_1[i:] = line_tmp
    for i in range(len(lines2_2)):
        line = lines2_2[i].strip('\n').split(', ')
        line_tmp = [float(x) for x in line]
        delay2_2[i:] = line_tmp
    for i in range(len(lines3_1)):
        line = lines3_1[i].strip('\n').split(', ')
        line_tmp = [float(x) for x in line]
        delay3_1[i:] = line_tmp
    for i in range(len(lines3_2)):
        line = lines3_2[i].strip('\n').split(', ')
        line_tmp = [float(x) for x in line]
        delay3_2[i:] = line_tmp
    for i in range(len(lines4_1)):
        line = lines4_1[i].strip('\n').split(', ')
        line_tmp = [float(x) for x in line]
        delay4_1[i:] = line_tmp
    for i in range(len(lines4_2)):
        line = lines4_2[i].strip('\n').split(', ')
        line_tmp = [float(x) for x in line]
        delay4_2[i:] = line_tmp

    # arr and std
    arr1_1 = []
    arr1_2 = []
    arr2_1 = []
    arr2_2 = []
    arr3_1 = []
    arr3_2 = []
    arr4_1 = []
    arr4_2 = []
    std1_1 = []
    std1_2 = []
    std2_1 = []
    std2_2 = []
    std3_1 = []
    std3_2 = []
    std4_1 = []
    std4_2 = []

    for i in range(len(delay1_1[0])):
        tmp = []
        for j in range(len(delay1_1)):
            tmp.append(delay1_1[j][i])
        arr1_1.append(np.mean(tmp))
        std1_1.append(np.std(tmp, ddof=1))
    for i in range(len(delay1_2[0])):
        tmp = []
        for j in range(len(delay1_2)):
            tmp.append(delay1_2[j][i])
        arr1_2.append(np.mean(tmp))
        std1_2.append(np.std(tmp, ddof=1))
    for i in range(len(delay2_1[0])):
        tmp = []
        for j in range(len(delay2_1)):
            tmp.append(delay2_1[j][i])
        arr2_1.append(np.mean(tmp))
        std2_1.append(np.std(tmp, ddof=1))
    for i in range(len(delay2_2[0])):
        tmp = []
        for j in range(len(delay2_2)):
            tmp.append(delay2_2[j][i])
        arr2_2.append(np.mean(tmp))
        std2_2.append(np.std(tmp, ddof=1))
    for i in range(len(delay3_1[0])):
        tmp = []
        for j in range(len(delay3_1)):
            tmp.append(delay3_1[j][i])
        arr3_1.append(np.mean(tmp))
        std3_1.append(np.std(tmp, ddof=1))
    for i in range(len(delay3_2[0])):
        tmp = []
        for j in range(len(delay3_2)):
            tmp.append(delay3_2[j][i])
        arr3_2.append(np.mean(tmp))
        std3_2.append(np.std(tmp, ddof=1))
    for i in range(len(delay4_1[0])):
        tmp = []
        for j in range(len(delay4_1)):
            tmp.append(delay4_1[j][i])
        arr4_1.append(np.mean(tmp))
        std4_1.append(np.std(tmp, ddof=1))
    for i in range(len(delay4_2[0])):
        tmp = []
        for j in range(len(delay4_2)):
            tmp.append(delay4_2[j][i])
        arr4_2.append(np.mean(tmp))
        std4_2.append(np.std(tmp, ddof=1))

    # draw
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)

    x1 = np.arange(1, 21)
    y1_1 = arr1_1
    y1_2 = arr1_2
    ax1.errorbar(x1, y1_1, yerr=std1_1, fmt='b-o', lw=2, elinewidth=1, capsize=4, capthick=1, marker='s', ms=8, label='VXLAN-based INT')
    ax1.errorbar(x1, y1_2, yerr=std1_2, fmt='g-o', lw=2, elinewidth=1, capsize=4, capthick=1, marker='s', ms=8, label='DFS-based INT')
    ax1.legend(loc='best', ncol=1, frameon=True, framealpha=0.2, fontsize=25)
    ax1.tick_params(labelsize=25)
    ax1.set_xlabel('Interval (ms)', fontsize=25)
    ax1.set_ylabel('Process Delay (us)', fontsize=25)
    ax1.set_title('(a) Process Delay in Fat-Tree Network', fontsize=25, y=-0.3)
    ax1.grid()

    x2 = np.arange(1, 21)
    y2_1 = arr2_1
    y2_2 = arr2_2
    ax2.errorbar(x2, y2_1, yerr=std2_1, fmt='b-o', lw=2, elinewidth=1, capsize=4, capthick=1, marker='s', ms=8, label='VXLAN-based INT')
    ax2.errorbar(x2, y2_2, yerr=std2_2, fmt='g-o', lw=2, elinewidth=1, capsize=4, capthick=1, marker='s', ms=8, label='DFS-based INT')
    ax2.legend(loc='best', ncol=1, frameon=True, framealpha=0.2, fontsize=25)
    ax2.tick_params(labelsize=25)
    ax2.set_xlabel('Interval (ms)', fontsize=25)
    ax2.set_ylabel('Queuing Delay (us)', fontsize=25)
    ax2.set_title('(b) Queuing Delay in Fat-Tree Network', fontsize=25, y=-0.3)
    ax2.grid()

    x3 = np.arange(1, 21)
    y3_1 = arr3_1
    y3_2 = arr3_2
    ax3.errorbar(x3, y3_1, yerr=std3_1, fmt='b-o', lw=2, elinewidth=1, capsize=4, capthick=1, marker='s', ms=8, label='VXLAN-based INT')
    ax3.errorbar(x3, y3_2, yerr=std3_2, fmt='g-o', lw=2, elinewidth=1, capsize=4, capthick=1, marker='s', ms=8, label='DFS-based INT')
    ax3.legend(loc='best', ncol=1, frameon=True, framealpha=0.2, fontsize=25)
    ax3.tick_params(labelsize=25)
    ax3.set_xlabel('Interval (ms)', fontsize=25)
    ax3.set_ylabel('Process Delay (us)', fontsize=25)
    ax3.set_title("(c) Process Delay in Spine-Leaf Network", fontsize=25, y=-0.3)
    ax3.grid()

    x4 = np.arange(1, 21)
    y4_1 = arr4_1
    y4_2 = arr4_2
    ax4.errorbar(x4, y4_1, yerr=std4_1, fmt='b-o', lw=2, elinewidth=1, capsize=4, capthick=1, marker='s', ms=8, label='VXLAN-based INT')
    ax4.errorbar(x4, y4_2, yerr=std4_2, fmt='g-o', lw=2, elinewidth=1, capsize=4, capthick=1, marker='s', ms=8, label='DFS-based INT')
    ax4.legend(loc='best', ncol=1, frameon=True, framealpha=0.2, fontsize=25)
    ax4.tick_params(labelsize=25)
    ax4.set_xlabel('Interval (ms)', fontsize=25)
    ax4.set_ylabel('Queuing Delay (us)', fontsize=25)
    ax4.set_title('(d) Queuing Delay in Spine-Leaf Network', fontsize=25, y=-0.3)
    ax4.grid()

    plt.show()


if __name__ == '__main__':
    main()

