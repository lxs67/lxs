# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 18:47:35 2024

@author: Lenovo
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import fontManager

# 添加字体和设置全局字体
fontManager.addfont(r"C:\\Users\\Lenovo\\Desktop\\lmroman10.otf")
plt.rcParams['font.family'] = 'Latin Modern Roman'
plt.rcParams['text.usetex'] = True  # 注释掉以防 LaTeX 环境问题

# 横纵坐标标签
x_labels = [r'$a_{\mathrm{p,1}}^{(3)}$', r'$a_{\mathrm{p,2}}^{(3)}$', r'$a_{\mathrm{p,3}}^{(3)}$', r'$a_{\mathrm{p,4}}^{(3)}$', r'$\cdots$', r'$a_{\mathrm{p},n}^{(3)}$']
y_labels = [r'$a_{\mathrm{c,1}}^{(3)}$', r'$a_{\mathrm{c,2}}^{(3)}$', r'$a_{\mathrm{c,3}}^{(3)}$', r'$a_{\mathrm{c,4}}^{(3)}$', r'$\cdots$', r'$a_{\mathrm{c},n}^{(3)}$']

# 数据
z_values = [
    [0.672327, 1.9902, 2.24, 2.24, 2.24, 0.7412],
    [0.7412, 0.672327, 1.9902, 2.24, 2.24, 2.24],
    [2.24, 0.7412, 0.672327, 1.9902, 2.24, 2.24],
    [2.24, 2.24, 0.7412, 0.672327, 1.9902, 2.24],
    [2.24, 2.24, 2.24, 0.7412, 0.672327, 1.9902],
    [1.9902, 2.24, 2.24, 2.24, 0.7412, 0.672327]
]

# 转换为 numpy 数组
z = np.array(z_values)

# 创建图形
fig, ax = plt.subplots(figsize=(10, 8))

# 绘制黑白棋框
for i in range(z.shape[1]):
    for j in range(z.shape[0]):
        color = 'black' if z[j, i] > 1 else 'white'
        line_color = 'white' if color == 'black' else 'black'  # 黑框用白线，白框用黑线
        ax.add_patch(plt.Rectangle((i, j), 1, 1, color=color, ec=line_color))  # 添加边界线条
        ax.text(i + 0.5, j + 0.5, f'{z[j, i]:.2f}',
                color='black' if color == 'white' else 'white',  # 文字颜色与背景对比
                ha='center', va='center', fontsize=15)

# 设置刻度和标签
ax.set_xticks(np.arange(len(x_labels)) + 0.5)
ax.set_yticks(np.arange(len(y_labels)) + 0.5)
ax.set_xticklabels(x_labels, fontsize=30)
ax.set_yticklabels(y_labels, fontsize=30)  # 保持 y 轴标签顺序为 ap1 到 ap5

# 调整网格和边界
ax.set_xlim(0, len(x_labels))
ax.set_ylim(0, len(y_labels))
ax.set_aspect('equal')
ax.grid(visible=False)  # 隐藏默认网格线

# 添加标题

# 显示图像
plt.tight_layout()
plt.savefig('等高图.svg', format='svg', dpi=300,bbox_inches='tight') 
plt.show()

