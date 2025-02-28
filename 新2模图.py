# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 19:37:17 2024

@author: Lenovo
"""

import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager
fontManager.addfont(r"C:\Users\Lenovo\Desktop\lmroman10.otf")
plt.rcParams['font.family'] = 'Latin Modern Roman'
plt.rcParams['text.usetex'] = True  
# 定义数据
x1 = [1, 2, 3, 4]
y1 = [0.23560482938119215,
0.23560482938119184,
0.23560482938119195,
0.23560482938119182]
x2 = [5, 6, 7]
y2 = [0.35100040032031965,
0.14749180832948278,
0.420204102886729]

# 创建散点图
plt.scatter(x1, y1, s=50, marker='o', color='blue', edgecolors='black', linewidths=0.5, label=r'1 $\vert$ 3')
plt.scatter(x2, y2, s=50, marker='^', color='green', edgecolors='black', linewidths=0.5, label=r'2 $\vert$ 2')

# 自定义x轴刻度和标签
plt.xticks([1, 2, 3, 4, 5, 6, 7], 
           ['1', '2', '3', '4', '5', '6', '7'], 
           fontsize=15, fontweight='bold')

# 自定义y轴刻度和标签
plt.yticks([0.2, 0.3, 0.4, 0.52], ['0.2', '0.3', '0.4', '0.5'],fontsize=15, fontweight='bold')

# 添加标题和标签，并设置字体
plt.title(r'$n = 2$', fontsize=25)
plt.xlabel('Bipartitions', fontsize=20)
plt.ylabel('PPT  value', fontsize=20)

# 添加图例并设置字体
plt.legend(title_fontsize='10', fontsize='12', loc='upper center', bbox_to_anchor=(0.88,1), ncol=1)
plt.savefig('2mode.svg', format='svg', dpi=300,bbox_inches='tight') # 显示图形
plt.show()