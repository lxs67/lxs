# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 14:26:33 2024

@author: Lenovo
"""

import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager
fontManager.addfont(r"C:\Users\Lenovo\Desktop\lmroman10.otf")
plt.rcParams['font.family'] = 'Latin Modern Roman'


# 定义数据
x1 = [1, 2, 3, 4, 5,6]
y1 = [0.23560482938119207,
0.23560482938119198,
0.2356048293811922,
0.23560482938119212,
0.23560482938119223,
0.23560482938119215

]
x2= [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
y2 = [0.3510004003203206,
0.1810710621680045,
0.3338277829656551,
0.1810710621680044,
0.23725938933127572,
0.23725938933127597,
0.18107106216800453,
0.33382778296565474,
0.18107106216800406,
0.35100040032032,
0.18107106216800425,
0.3338277829656548,
0.23725938933127555,
0.18107106216800473,
0.3510004003203198
]
x3=[22,23,24,25,26,27,28,29,30,31]
y3=[0.20307009233246415,
0.3332508581533009,
0.3332508581533016,
0.2030700923324643,
0.3332508581533011,
0.1474918083294831,
0.20161375320818936,
0.20161375320818908,
0.2016137532081891,
0.20307009233246442]

# 创建散点图，调整点的大小和样式
plt.scatter(x1, y1, s=50, marker='o', color='blue', edgecolors='black', linewidths=0.5,label=r'1 $\vert$ 5')
plt.scatter(x2, y2, s=50, marker='^',  color='green',edgecolors='black', linewidths=0.5, label=r'2 $\vert$ 4')
plt.scatter(x3, y3, s=50, marker='D',  color='Purple',edgecolors='black', linewidths=0.5, label=r'3 $\vert$ 3')
# 自定义x轴刻度和标签
plt.xticks([5, 10, 15, 20, 25,30], ['5', '10', '15', '20', '25','30'], fontsize=15, fontweight='bold')
# 自定义y轴刻度和标签
plt.yticks([0.2, 0.3, 0.4, 0.5], ['0.2', '0.3', '0.4', '0.5'],  fontsize=15, fontweight='bold')

# 添加标题和标签
plt.title(r'$n = 3$',fontsize=25)
plt.xlabel('Bipartitions',fontsize=20)
plt.ylabel('PPT value',fontsize=20)
# 添加图例并设置字体
plt.legend(title_fontsize='10', fontsize='12', loc='upper center', bbox_to_anchor=(0.88,1), ncol=1)
plt.savefig('3mode.svg', format='svg', dpi=300,bbox_inches='tight') # 显示图形
plt.show()